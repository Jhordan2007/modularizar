def registrar_participante(data):
    print("**************************************************")
    participante = {}
    doc = input("Ingrese el documento: ")    
    if data["participantes"].get(doc, None) == None:
        participante["Nombre"] = input("Ingrese el nombre: ")
        participante["Edad"] = int(input("Ingrese la edad: "))
        participante["Cargo"] = input("Ingrese el cargo: ")
        participante["Pago"] = False
        data[doc] = participante
    else:
        print("Participante ya existe!")
    print("**************************************************")
    
def pagar_participante(data):
    print("**************************************************")
    doc = input("Ingrese el documento: ")
    participante = data["participantes"].get(doc, None)
    if participante != None and participante["Pago"] == False:
        data["participantes"][doc]["Pago"] = True
        print("Pago existoso!")
    else:
        print("Participante no existe o ya pagó!")
    print("**************************************************")
    
def eliminar_participante(data):
    print("**************************************************")
    doc = input("Ingrese el documento: ")
    participante = data["participantes"].get(doc, None)
    if participante != None and participante["Pago"] == False:
        data["participantes"].pop(doc)
        print("Eliminación existosa!")
    else:
        print("Participante no existe o ya perdió!")
    print("**************************************************")

def saber_cuantos_empleados_no_han_pagado(data):
    print("**************************************************")
    cont = 0
    for valor in data["participantes"].values():
        if valor["Pago"] == False:
            cont += 1
    print("Existen", cont, "Participantes por pagar")
    print("La deuda total es:", cont*50000)
    print("**************************************************")
    
def saber_cuales_empleados_no_han_pagado(data):
    print("**************************************************")
    print("Los participantes que no han pagado son:")
    for valor in data["participantes"].values():
        if valor["Pago"] == False:
            print("-",valor["nombre"], "que tiene el cargo de",valor["Cargo"])    
    print("**************************************************")