# meu programa inicia aqui 

name = input("Digite o seu nome: ")
age = int(input("Digite a sua idade: "))

if age >= 18:
    print(f"Bem vindo; {name.capitalize()} e você tem {age} anos")
else:
    print(f"Infelizmente não pode entrar, jovem {name.capitalize()}")

#fim do programa