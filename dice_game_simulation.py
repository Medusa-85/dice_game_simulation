import random
import numpy as np

# Este código simula um jogo de lançamento de dados de seis lados. 
# O objetivo é analisar a justiça do jogo, trazer possíveis resultados e fazer previsões sobre jogos futuros, 
# utilizando para isso dados estatísticos relacionados a estes eventos.


# Parte 1: Simulação de dados. Foi definida uma função que simula o lançamento de 
# dois dados de seis lados e retorna a soma dos resultados de cada um.

def dice_roll():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    # print(f'dice_1: {dice_1}') #Descomente essa linha se quiser verificar a variável dice_1
    # print(f'dice_2: {dice_2}') #Descomente essa linha se quiser verificar a variável dice_2
    return dice_1 + dice_2

#print(dice_roll())