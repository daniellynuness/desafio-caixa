import secrets
import string
import tkinter as tk
from tkinter import simpledialog, messagebox

# Função para gerar senha segura
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

# Função para obter os dados do usuário através da interface gráfica
def get_user_input():
    length = simpledialog.askinteger("Input", "Qual o comprimento desejado da senha?", minvalue=1, maxvalue=128)
    upper_count = simpledialog.askinteger("Input", "Quantas letras maiúsculas?", minvalue=0, maxvalue=length)
    lower_count = simpledialog.askinteger("Input", "Quantas letras minúsculas?", minvalue=0, maxvalue=length)
    number_count = simpledialog.askinteger("Input", "Quantos números?", minvalue=0, maxvalue=length)
    symbol_count = simpledialog.askinteger("Input", "Quantos símbolos?", minvalue=0, maxvalue=length)
    
    personal_questions = []
    personal_questions.append(simpledialog.askstring("Input", "Qual o nome do seu pet? (opcional)"))
    personal_questions.append(simpledialog.askstring("Input", "Qual a sua cidade natal? (opcional)"))
    personal_questions.append(simpledialog.askstring("Input", "Qual a sua comida favorita? (opcional)"))
    
    return length, upper_count, lower_count, number_count, symbol_count, personal_questions

# Função principal
def main():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    
    length, upper_count, lower_count, number_count, symbol_count, personal_questions = get_user_input()
    
    if not all([length, upper_count, lower_count, number_count, symbol_count]):
        messagebox.showerror("Error", "Todos os campos obrigatórios devem ser preenchidos!")
        return
    
    if upper_count + lower_count + number_count + symbol_count > length:
        messagebox.showerror("Error", "A soma de todos os tipos de caracteres não pode exceder o comprimento total da senha!")
        return
    
    password = generate_password(length, upper_count, lower_count, number_count, symbol_count, personal_questions)
    
    messagebox.showinfo("Senha Gerada", f"Sua senha gerada: {password}")

if __name__ == "__main__":
    main()
