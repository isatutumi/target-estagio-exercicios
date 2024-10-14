#Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

def descobrir_interruptores():
    # Simulação das lâmpadas (quente = 1, fria = 0)
    lampada_1 = 0  # desligada e fria
    lampada_2 = 0  # desligada e fria
    lampada_3 = 0  # desligada e fria
    
    # Primeiro interruptor ligado por alguns minutos
    lampada_1 = 1  # desligada mas quente após ser ligada por um tempo
    
    # Segundo interruptor ligado imediatamente antes de entrar na sala
    lampada_2 = 1  # ligada

    # Saída que mostra o estado das lâmpadas e a lógica aplicada
    if lampada_1 == 1 and lampada_2 == 1 and lampada_3 == 0:
        print("Interruptor 1 controla a lâmpada quente (desligada), "
              "Interruptor 2 controla a lâmpada ligada, "
              "Interruptor 3 controla a lâmpada fria e desligada.")
    else:
        print("Não foi possível determinar com clareza.")

descobrir_interruptores()
