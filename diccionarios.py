diccionario ={
    'nombre':"Edison",
    'edad':27,
    'estatuta':1.68,
    'genero':"masculino",
    'ocupacion':"estudiante",
    'direccion':"carrera23#102c40",
    'telefono':3052102814,
    'estadoSivi':"soltero"
}
#print(diccionario['nombre'])
print(diccionario.get('nombre'))

#tambien puedo recorrer el diccionario o objeto
for clave,valor in diccionario.items():
    print(clave,valor)

    