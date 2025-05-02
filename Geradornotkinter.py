import tkinter as tk
import string
import random

# Função que gera a senha, igual à sua
def gerar_senha(tamanho, modo):
    if modo == 1:
        caracteres = string.digits
    elif modo == 2:
        caracteres = string.ascii_letters
    elif modo == 3:
        caracteres = string.ascii_letters + string.digits
    elif modo == 4:
        caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Função que será chamada ao clicar no botão
def ao_clicar_gerar():
    try:
        modo = int(tipo_var.get())
        tamanho = int(entry_tamanho.get())

        if modo < 1 or modo > 4:
            resultado_var.set("❌ Tipo inválido (1 a 4)")
            return
        if tamanho < 4:
            resultado_var.set("❌ Mínimo: 4 caracteres")
            return

        senha = gerar_senha(tamanho, modo)
        resultado_var.set(f"{senha}")
    except ValueError:
        resultado_var.set("❌ Entrada inválida")

# Interface gráfica
janela = tk.Tk()
janela.title("Gerador de Senhas Fortes")
janela.geometry("400x300")

tk.Label(janela, text="Tamanho da senha:").pack()
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

tk.Label(janela, text="Tipo de senha:").pack()

tipo_var = tk.StringVar(value="4")

tk.Radiobutton(janela, text="1 - Apenas números", variable=tipo_var, value="1").pack(anchor='w')
tk.Radiobutton(janela, text="2 - Apenas letras", variable=tipo_var, value="2").pack(anchor='w')
tk.Radiobutton(janela, text="3 - Letras e números", variable=tipo_var, value="3").pack(anchor='w')
tk.Radiobutton(janela, text="4 - Letras, números e símbolos", variable=tipo_var, value="4").pack(anchor='w')

tk.Button(janela, text="Gerar Senha", command=ao_clicar_gerar).pack(pady=10)

resultado_var = tk.StringVar()
tk.Entry(janela, textvariable=resultado_var, width=30).pack()

janela.mainloop()
