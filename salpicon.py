print("***** Venta de salpicones Mi Dulce ******")
print("1. Ingresar frutas")
print("2. Mostrar costo total del salpicon")
print("3. Mostrar todas las frutas")
print("4. Mostrar cual es la fruta más barata y más cara")
print("5. SALIR")

frutas = []
opc = 0

def costoTotalSalpi(precioUnitario, cantidad):
    totalCosto = precioUnitario * cantidad
    return totalCosto

def obtenerPrecioUnitario(fruta):
    return fruta['precioUnitario']

def ordenFrutas(frutas):
    frutasOrdenadas = sorted(frutas, key=obtenerPrecioUnitario, reverse=True)
    for fruta in frutasOrdenadas:
        print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio Unitario: {fruta['precioUnitario']}, Cantidad: {fruta['cantidad']}")

def mostrarPrecio(frutas):
    frutaBarata = min(frutas, key=obtenerPrecioUnitario)
    frutaCara = max(frutas, key=obtenerPrecioUnitario)
    print(f"La fruta más barata es: {frutaBarata['nombre']} con un precio unitario: {frutaBarata['precioUnitario']}")
    print(f"La fruta más cara es: {frutaCara['nombre']} con un precio unitario de: {frutaCara['precioUnitario']}")

while opc != 5:
    fruta = {}
    opc = int(input("Ingrese una opción: "))

    if opc == 1:
        fruta["id"] = int(input("Ingrese la identificación de la fruta: "))
        fruta["nombre"] = input("Ingrese el nombre de la fruta: ")
        fruta["precioUnitario"] = float(input("Ingrese el precio unitario de la unidad a comprar: "))
        fruta["cantidad"] = int(input("Ingrese la cantidad de frutas a comprar: "))
        frutas.append(fruta)
    elif opc == 2:
        costoTotal = sum(costoTotalSalpi(fruta['precioUnitario'], fruta['cantidad']) for fruta in frutas)
        print(f"El costo total del salpicón es: ${costoTotal}")
    elif opc == 3:
        ordenFrutas(frutas)
    elif opc == 4:
        mostrarPrecio(frutas)
    elif opc == 5:
        print("Finalizado el programa")
    else:
        print("Opción invalida, inténtalo de nuevo")

