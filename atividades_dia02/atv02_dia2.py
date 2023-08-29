#programa que recebe a idade e retorna p/ obter uma cnh

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
idade_int = 0
try:
    idade_int = int(idade)
except ValueError:        
        raise ValueError('Digite a idade em numeros')
         
if idade_int <18:
    print(f"Desculpe {nome} mas você ainda tem {idade} anos de idade e a idade mínima é 18.")
else:
    print(f'Parabéns {nome}, você tem {idade} anos de idade, pode ter carteira de motorista.')
    