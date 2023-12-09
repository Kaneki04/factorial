import os
def factorial():
    os.system("cls")
    num = int(input("Ingrese Numero de la forma +n!: "))
    if 0 < num:
        resultado = 1
        for i in range(1, (num+1)):
            resultado*=i
        print(resultado)
   
    elif num == 0:
        print(1)

    else:
        print("Tiene que ser mayor o igual a 0")
        factorial()

factorial()

    