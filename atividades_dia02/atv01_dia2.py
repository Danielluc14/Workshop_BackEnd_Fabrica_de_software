#meu modo de resolver
'''
num = int(input("escolha um numero: "))
print ('o número antecessor é: ',num -1,' e o sucessor é:',num +1)
'''

#modo que o instrutor resolveu o problema 
num1 = input('Qual numero deseja ? ') 

antecessor = 0
sucessor=0

try:
    antecessor = int(num1) - 1
    sucessor = int(num1) + 1

except ValueError:
    raise ValueError("Digite um número válido")
    print("Digite um número válido")

print(f"o numero digitado foi {num1} e seu antecessor é {antecessor} e o sucessor {sucessor}")

print(type(num1))
print(type(antecessor))
print(type(sucessor))



