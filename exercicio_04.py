#Descubra a lógica e complete o próximo elemento:
##a) 1, 3, 5, 7, ___
## b) 2, 4, 8, 16, 32, 64, ____
##c) 0, 1, 4, 9, 16, 25, 36, ____
##d) 4, 16, 36, 64, ____
##e) 1, 1, 2, 3, 5, 8, ____
##f) 2,10, 12, 16, 17, 18, 19, ____

def completar_sequencias():
    sequencia_a = [1, 3, 5, 7]  # sequência de números ímpares
    sequencia_b = [2, 4, 8, 16, 32, 64]  # cada número é o dobro do anterior
    sequencia_c = [0, 1, 4, 9, 16, 25, 36]  # quadrados perfeitos
    sequencia_d = [4, 16, 36, 64]  # quadrados pares
    sequencia_e = [1, 1, 2, 3, 5, 8]  # sequência de Fibonacci
    sequencia_f = [2, 10, 12, 16, 17, 18, 19]  # sequência com padrão alternado

    proximo_a = sequencia_a[-1] + 2  # próximo número ímpar
    proximo_b = sequencia_b[-1] * 2  # próximo é o dobro do anterior
    proximo_c = (len(sequencia_c)) ** 2  # próximo quadrado perfeito
    proximo_d = (len(sequencia_d) * 2) ** 2  # próximo quadrado par
    proximo_e = sequencia_e[-1] + sequencia_e[-2]  # próximo Fibonacci
    proximo_f = 20  # padrão para sequência f

    return proximo_a, proximo_b, proximo_c, proximo_d, proximo_e, proximo_f

resultados = completar_sequencias()
print(f"Próximos números: \n"
        f"a) {resultados[0]} \n"
        f"b) {resultados[1]} \n"
        f"c) {resultados[2]} \n"
        f"d) {resultados[3]} \n"
        f"e) {resultados[4]} \n"
        f"f) {resultados[5]}")
