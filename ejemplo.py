def saludar(nombre):
    """Funcion que saluda al usuario"""
    return f"hola,{nombre} bienvenido al mundo de phyton."

print(saludar("Estudiante"))

numeros=[ 1,2,3,4,5 ]
print("lista de numeros")
for num in numeros:
    print(f" -{num}al cuadrado es{num**2}")

edad=20
if edad >=18:
    print("eres matyor de edad")
else:
    print(""eres menor de edad)