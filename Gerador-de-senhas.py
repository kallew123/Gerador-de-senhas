import string
import random
import tkinter as tk


def gerar_senha(tamanho, modo):
    if modo == 1:
        caracteres = string.digits
    elif modo == 2:
        caracteres = string.ascii_letters
    elif modo == 3:
        caracteres = string.ascii_letters + string.digits
    elif modo == 4:
        caracteres = string.ascii_letters + string.punctuation + string.digits

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def ao_clicar_gerar():
    try:
        modo = int(tipo_var.get())
        tamanho = int(entry_tamanho.get())

        if tamanho < 4:
            resultado_var.set("Tamanho de senha invalida! (Menor que 4)")
            return
        
        senha = gerar_senha(tamanho, modo)
        resultado_var.set(f"{senha}")

    except ValueError:
        resultado_var.set("Digite números válidos.")


janela = tk.Tk()
janela.title("Gerador de senha")
janela.geometry("600x450")

tk.Label(janela, text="Tamanho da senha").pack()
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

tk.Label(janela, text="Tipo de senha").pack()
tipo_var = tk.StringVar(value= 0)

tk.Radiobutton(janela, text="1 - Apenas números", variable=tipo_var, value="1").pack(anchor='w')
tk.Radiobutton(janela, text="2 - Apenas letras", variable=tipo_var, value="2").pack(anchor='w')
tk.Radiobutton(janela, text="3 - Letras e números", variable=tipo_var, value="3").pack(anchor='w')
tk.Radiobutton(janela, text="4 - Letras, números e símbolos", variable=tipo_var, value="4").pack(anchor='w')

tk.Button(janela, text="Gerar Senha", command=ao_clicar_gerar).pack(pady=10)

resultado_var = tk.StringVar()
tk.Entry(janela, textvariable=resultado_var, state="readonly", width=40, justify="center").pack()

janela.mainloop()

# Nickklb
