# Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA); Ao final do processamento, qual será o valor da variável SOMA?

## RESPOSTA: O valor final de SOMA será 91 (incluindo o incremento inicial de 1).

def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 0
    while K <= INDICE:
        K = K + 1
        SOMA = SOMA + K
    return SOMA

resultado = calcular_soma()
print(f"O valor final de SOMA é: {resultado}")
