import secrets
import string

def get_user_input():
    length = int(input("Qual o comprimento desejado da senha? "))
    upper_count = int(input("Quantas letras maiúsculas? "))
    lower_count = int(input("Quantas letras minúsculas? "))
    number_count = int(input("Quantos números? "))
    symbol_count = int(input("Quantos símbolos? "))
    
    personal_questions = []
    personal_questions.append(input("Qual o nome do seu pet? (opcional) "))
    personal_questions.append(input("Qual a sua cidade natal? (opcional) "))
    personal_questions.append(input("Qual a sua comida favorita? (opcional) "))
    
    return length, upper_count, lower_count, number_count, symbol_count, personal_questions

def generate_password(length, upper_count, lower_count, number_count, symbol_count, personal_questions):
    all_chars = []
    all_chars.extend(secrets.choice(string.ascii_uppercase) for _ in range(upper_count))
    all_chars.extend(secrets.choice(string.ascii_lowercase) for _ in range(lower_count))
    all_chars.extend(secrets.choice(string.digits) for _ in range(number_count))
    all_chars.extend(secrets.choice(string.punctuation) for _ in range(symbol_count))

    # Incorporar respostas pessoais na senha
    for answer in personal_questions:
        if answer:
            all_chars.extend(answer)
    
    # Garantir que a senha tenha o comprimento desejado
    if len(all_chars) < length:
        additional_chars = [secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - len(all_chars))]
        all_chars.extend(additional_chars)
    
    secrets.SystemRandom().shuffle(all_chars)
    password = ''.join(all_chars[:length])
    
    return password

def main():
    length, upper_count, lower_count, number_count, symbol_count, personal_questions = get_user_input()
    
    if upper_count + lower_count + number_count + symbol_count > length:
        print("Erro: A soma de todos os tipos de caracteres não pode exceder o comprimento total da senha!")
        return
    
    password = generate_password(length, upper_count, lower_count, number_count, symbol_count, personal_questions)
    
    print(f"Sua senha gerada: {password}")

if __name__ == "__main__":
    main()
