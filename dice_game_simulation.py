import random
import numpy as np
import matplotlib.pyplot as plt

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

# Parte 2: Multiplas simulações. Foi criado um loop com um número grande de repetições 
# que executa a função 'dice_roll' e armazena seu resultado num array NumPy.

simulations = 10000

total_moves = np.array([dice_roll() for i in range(simulations)])

# print(f'total_moves: {total_moves}') #Descomente essa linha se quiser verificar a variável total_moves

# Parte 3: Análise dos dados:

print(f'Média dos resultados: {total_moves.mean().round(2)}') # Média dos resultados
print(f'Lançamento máximo: {total_moves.max()}') # Lançamento máximo
print(f'Lançamento mínimo: {total_moves.min()}') # Lançamento mínimo

# Calcular a contagem de ocorrências de cada soma
unique_values, counts = np.unique(total_moves, return_counts=True)

print(f'Número de ocorrência para cada possível resultado: ')
for value, count in zip(unique_values, counts):
    print(f'Valor {value}: {count}')

# Plotagem de gráfico de barras dos resultados utilizando matplotlib:
plt.bar(unique_values, counts )

plt.xticks(range(2, 13), labels=range(2, 13))       # Rótulos dos ticks do eixo X

plt.xlabel('Soma')                                  # Rótulo do eixo X
plt.ylabel('Frequência')                            # Rótulo do eixo Y
plt.title('Frequência das Somas dos Lançamentos')   # Título do gráfico

plt.show()