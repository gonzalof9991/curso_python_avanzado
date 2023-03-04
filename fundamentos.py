user = {"name": "Gonzalo", "edad": 33}
# Operador ternario
es_mayor = True if user["edad"] > 18 else False
print(es_mayor)


# x args
def suma(*numeros):
    result = 0
    for numero in numeros:
        result += numero
    print(result)


suma(3, 4, 5, 6, 7)


# kwargs

def get_product(**datos):
    print(datos)


get_product(id=5, name="Gonzalo")

# map

nombres = ["Gonza", "Jose"]

nombresMap = list(map(lambda nombre: {"name": nombre}, nombres))

print(nombresMap)

# filter

nombresFilter = list(filter(lambda nombre: len(nombre["name"]) >= 5, nombresMap))

print(nombresFilter)

# Set

segundo = set(nombres)

print(segundo)
