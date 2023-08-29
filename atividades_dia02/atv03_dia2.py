''' crie um programa que leia a velocidade de uma carro e multe se passar com velocidade maior que 80km/h.
mostre que ele foi multado. a multa é de 7R$ por cada km acima do limite'''

velocidade = input('Digite a velocidade do carro: ')
velocidade_int = 0
try:
    velocidade_int = int(velocidade)
except ValueError:
    raise ValueError("Digite a velocidade usando números.")

if velocidade_int < 80:
    print('Você está dentro do limite da via.')
elif velocidade_int == 80:
    print('Você atingiu a velocidade limite')
else:
    print(f"você está acima do limite da via e sua multa foi de {(velocidade_int - 80)*7},00 Reais")
