#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def contar_a(texto):
    return texto.lower().count('a')

texto = input("Informe uma string: ")

quantidade = contar_a(texto)
print(f"A letra 'a' ocorre {quantidade} vezes na string.")
