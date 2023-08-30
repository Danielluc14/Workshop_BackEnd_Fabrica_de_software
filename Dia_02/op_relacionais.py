#operadores relacionais são os operadores 



# exemplos
x = 5
y = 3 
menor_que = x < y
maior_que = x > y
igual_a  = x == y
diferente_de = x != y
menor_igual_que = x <= y
maior_igual_que = x >= y

print(f"{menor_que=}")
print(f"{maior_que=}")
print(f"{igual_a=}")
print(f"{diferente_de=}")
print(f"{menor_igual_que=}")
print(f"{maior_igual_que=}")


if x > y:
    print('x é maior que y')
elif x < y:
    print('y é maior que x')
else:
    print('números iguais')
