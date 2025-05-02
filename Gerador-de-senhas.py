import string
import random
# String para ter lista de caracteres prontos e ramdom para gerar aleatoriamente

print("🔐 Gerador de Senhas Fortes")

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

while True:
    print("\nEscolha o seu tipo de senha:")
    print("1 - Apenas números")
    print("2 - Apenas letras (maiúsculas e minúsculas)")
    print("3 - Letras e números")
    print("4 - Letras, números e símbolos")
    
    try:
        modo = int(input("Digite o tipo desejado (1 a 4): "))  
    
        if modo < 1 or modo > 4:
            print("\n❌ Número inválido. Digite um número de 1 a 4.")
            continue

        break
    except ValueError:
        print("\n❌ Entrada inválida. Por favor, digite um número.")
        continue

while True:
    try:
        tamanho = int(input("Digite o tamanho desejado (maior que 4 caracteres): ")) 
        if tamanho < 4:
           print("\n❌ O tamanho mínimo recomendado é 4.")
           continue
        break
    except ValueError:
        print("\n❌ Entrada inválida. Digite um número.")
        continue

senha = gerar_senha(tamanho, modo)

print(f"\n✅ Senha gerada: {senha}")

