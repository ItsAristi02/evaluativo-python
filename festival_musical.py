print("******* Festival Musical Coachella *****")
print("1. Ingresar un grupo")
print("2. Mostrar todas las bandas")
print("3. Cambiar hora de presentacion")
print("4. Retirar una agrupacion")
print("5. Salir.")

agrupaciones = []
opcion = 0
while opcion != 5:
  agrupacion = {}
  opcion = int(input("Ingrese una opcion! "))
  if opcion == 1:
    agrupacion["id"] = int(input("Ingrese el id del grupo: "))
    agrupacion["nombre"] = input("Ingrese el nombre del grupo: ")
    agrupacion["genero"] = input("Ingrese el genero musical: ")
    agrupacion["horaDePresentacion"] = input("Ingrese la hora de presentacion: ")
    agrupacion["valorDelPago"] = input("Ingrese el valor del pago: ")
    agrupacion["estado"] = input("¿El grupo ya se presento?: ")
    if agrupacion["estado"] == "SI":
      agrupacion["estado"] = True
    else:
      agrupacion["estado"] = False
    agrupaciones.append(agrupacion)

  elif opcion == 2:
    print("\n**** Agrupaciones faltantes****")
    for agrup in agrupaciones:
      if agrup["estado"] == False:
        print(f"La agrupacion {agrup} no se ha presentado")
  
  elif opcion == 3:
    for agrup in agrupaciones:
      if agrup["estado"] == False:
        nombre = agrup["nombre"]
        print(f"Se cambiara la hora de la agrupacion {nombre}")
        agrup["horaDePresentacion"] = input(f"Ingrese la nueva hora de presentacion: ")
        print(f"\nSe ha actualizado correctamente la hora de la agrupación {nombre}")

  elif opcion == 4:
    for agrup in agrupaciones:
      if agrup["estado"] == False:
        nombre = agrup["nombre"]
        agrupaciones.remove(agrup)
        print(f"Se ha retirado correctamente la agrupacion {nombre}")
  elif opcion == 5:
        print("Programa Finalizado")  
  else:
    print("Opcion incorrecta!")
