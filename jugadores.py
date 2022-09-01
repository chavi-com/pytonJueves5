opcion=100
print("empanadas Inteligentes***")
print("1. Agregar Cliente")
print("0. salir")
print("3. buscar usuario po cedula")
clientes=[]

#diccionario
cliente={}

while(opcion !=0):
    #pedimos la opcion deseada
    opcion=int(input("Digite la opcion preferida"))
    #caminos del menu
    if opcion==1:
        cliente['cedula']=input("dijite su cedula")
        cliente['nombre']=input("dijite su nombre")
        clientes.append(cliente)
        print(cliente)
    elif(opcion==0)  :
    
        print("adios")
        break

    elif(opcion==3):
        cedu= input("dijita una cedula")
        
        cedu=""
        for cliente in clientes:
            if cliente["cedula"]==cedu:
                cedu=f"cliente encontrado: {cliente['cedula']}"
                print(cedu)
            else:
                cedu="cliente no encontrado"
                print(cedu)

    else:
        print("dijite una opcion valida")  


else:
    print("adios")