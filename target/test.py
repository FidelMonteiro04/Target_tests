#Primeira questão:

'''
A variável "SOMA" exibirá o valor 91. 
'''

#Segunda questão:

def fibonacci(number):
    fib = []
    for i in range(number):
        if i == 0 or i == 1: fib.append(i)
        else: fib.append(fib[i-1] + fib[i-2])
    return number in fib
print(fibonacci(10))

#Terceira questão:

'''
a - 9;
b - 128;
c - 49;
d - 100;
e - 13;
f - 20;
'''
# Quarta questão:
'''
O problema nos pede para determinar qual dos veículos (um carro que sai de Ribeirão Preto em direção a Franca ou um 
caminhão que sai de Franca em direção a Ribeirão Preto) estará mais próximo da cidade de Ribeirão Preto 
quando eles se cruzarem na mesma rodovia.

Para solucionar esse problema, utilizamos a ideia de que a distância percorrida por cada veículo até o ponto de cruzamento é igual. 
Chamamos de "x" a distância percorrida pelo carro e de "y" a distância percorrida pelo caminhão, 
contando a partir das respectivas cidades de origem. Sabemos que a distância entre as cidades é de 100 km e,
portanto, temos a equação x + y = 100.
Além disso, utilizamos a equação de velocidade, que relaciona a distância percorrida, a velocidade e o tempo.
Para o carro, sabemos que a velocidade é constante a 110 km/h e, portanto, x = 110t, 
onde "t" é o tempo que ele leva para chegar ao ponto de cruzamento. Para o caminhão, consideramos que ele 
leva mais tempo devido a dois pedágios ao longo do caminho, e assim a equação de y é dada por y = 80(t + 10/60) + 80(t + 15/60).

Substituindo as equações de x e y na equação x + y = 100, encontramos o tempo "t"
 necessário para os dois veículos se cruzarem. Utilizando a equação de x = 110t, encontramos a 
 distância percorrida pelo carro até o ponto de cruzamento e, utilizando a equação de y, 
 encontramos a distância percorrida pelo caminhão.

Descobrimos que o carro percorre uma distância menor até o ponto de cruzamento e, portanto, 
estará mais próximo da cidade de Ribeirão Preto. 
Ele estará a cerca de 38,55 km da cidade de Ribeirão Preto e a cerca de 61,45 km da cidade 
de Franca no momento em que os dois veículos se cruzarem na rodovia.
'''

#Quinta questão:

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def inverse(list):
    return list[::-1]
print(inverse(list))