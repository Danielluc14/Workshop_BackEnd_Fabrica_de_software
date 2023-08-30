#while é um loop de repetição

counter = 0 

while counter <= 10:
    if counter == 5:
        print("não quero mostrar esse número")
        # incrementar
        counter+= 1 
        continue
    print(counter)
    
    counter += 1
    
    
print('fora do escopo do while')
print(counter)

# utilizando o break

while counter >= 15:
    if counter == 1:
        print('cabou')
        counter -= 1 
        break
    print(counter)
    counter -= 1




