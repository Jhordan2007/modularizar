def registrar_evento(data):
    print("**************************************************")
    evento = {}
    evento["Nombre"] = input("Ingrese el nombre del evento: ")
    evento["Locacion"] = input("Ingrese la locacion del evento: ")
    evento["Dia"] = int(input("Ingrese el dia del evento: "))
    evento["Hecho"] = False
    data["eventos"].append(evento)
    print("Evento registrado")
    print("**************************************************")
    
def modificar_evento(data):
    print("**************************************************")
    cont = 1
    print("Ingrese el numero del evento a modificar ->")
    for i in data["eventos"]:
        print(cont,"-", i["Nombre"], "que será el dia", i["Dia"])
        cont += 1
    opc = int(input("Ingrese su elección: "))
    evento = data["eventos"][opc-1] #Falta validar que el indice sea válido
    if evento["Hecho"] == False:
        data["eventos"].pop(opc-1)
        print("Evento eliminado!!")
    else:
        print("Evento ya realizado, no se puede eliminar!")
    print("**************************************************")

def eliminar_evento(data):
    print("**************************************************")
    cont = 1
    print("Ingrese el numero del evento a eliminar ->")
    for i in data["eventos"]:
        print(cont,"-", i["Nombre"], "que será el dia", i["Dia"])
        cont += 1
    opc = int(input("Ingrese su elección: "))
    evento = data["eventos"][opc-1] #Falta validar que el indice sea válido
    if evento["Hecho"] == False:
        data["eventos"].pop(opc-1)
        print("Evento eliminado!!")
    else:
        print("Evento ya realizado, no se puede eliminar!")
    print("**************************************************")

def mostrar_eventos(data):
    print("**************************************************")
    print("Los eventos son:")
    for valor in data["eventos"]:
        print("-",valor["Nombre"], ", con locación",valor["Locacion"], ", el dia", valor["Dia"])    
    print("**************************************************")

def completar_evento(data):
    print("**************************************************")
    cont = 1
    print("Ingrese el numero del evento a completar ->")
    for i in data["eventos"]:
        print(cont,"-", i["Nombre"], "que será el dia", i["Dia"])
        cont += 1
    opc = int(input("Ingrese su elección: "))
    evento = data["eventos"][opc-1] #Falta validar que el indice sea válido
    if evento["Hecho"] == False:
        data["eventos"][opc-1]["Hecho"] = True
        print("Evento completado!!")
    else:
        print("Evento ya realizado, no se puede completar de nuevo!")
    print("**************************************************")