def evaluar_temperatura (temperatura):
    if temperatura < 26:
        return "Temperatura baja"
    elif temperatura <= 34:
        return "Temperatura normal"
    else:
        return "Temperatura alta"

temperatura = float(input("Ingrese la temperatura: "))
print(evaluar_temperatura(temperatura)) 