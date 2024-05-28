import eventos
import participantes


eventoss = {
    "participantes": {
        "121312313": {"nombre": "Juan", "Edad": 50, "Cargo": "Contador", "Pago": False},
        "123456789": {"nombre": "Maria", "Edad": 30, "Cargo": "Secretaria", "Pago": True},
        "789456123": {"nombre": "Laura", "Edad": 40, "Cargo": "Ingeniera", "Pago": False}
    },
    "eventos2": [
        {"Nombre": "Paseo de olla", "Locacion": "Rio", "Dia": 25, "Hecho": False},
        {"Nombre": "Fiesta del mes", "Locacion": "Salón principal", "Dia": 15, "Hecho": True},
        {"Nombre": "Cumpleaños Jefe", "Locacion": "Oficinas", "Dia": 2,  "Hecho": True}
    ]
}



opc_menu = ("1. Para registrar participante", "2. Para pagar", "3. Para eliminar participante", "4. Para registrar un evento", "5. Para modificar un evento", "6. Para eliminar un evento", "7. Para marcar un evento como completado",
            "8. Para saber cuantos empleados no han cancelado aún el aporte", "9. Para saber cuales empleados (listarlos) no han cancelado.", "10. Para mostrar eventos", "11. Para salir")

while True:
    print("*********************************************************")
    print("Seleccione ->")
    for i in opc_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    if opc == len(opc_menu):
        print("Saliendo...")
        break
    elif opc == 1:
        participantes.registrar_participante(eventoss)
    elif opc == 2:
        participantes.pagar_participante(eventoss)    
    elif opc == 3:
        participantes.eliminar_participante(eventoss)
    elif opc == 4:
        eventos.registrar_evento(eventoss)
    elif opc == 5:
        print("Modificar evento")#Pendiente
    elif opc == 6:
        eventos.eliminar_evento(eventoss)
    elif opc == 7:
        eventos.completar_evento(eventoss)
    elif opc == 8:
        participantes.saber_cuantos_empleados_no_han_pagado(eventoss)
    elif opc == 9:
        participantes.saber_cuales_empleados_no_han_pagado(eventoss)
    elif opc == 10:
        eventos.mostrar_eventos(eventoss)
    elif opc == 0:
        print(eventoss["eventos2"])
    elif opc == 111:
        print(eventoss["participantes"])