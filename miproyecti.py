usuario = input("Ingrese el nombre con el que desea registrarse: ")
import sys
import random
nrandom = random.randint(0, 1001)
print(f"Su nuevo numero de cuenta es: {nrandom}")
saldo_inicial = 0
print(f"Saldo inicial de la cuenta: {saldo_inicial}")

def depositar():
    global saldo_inicial
    try:
        cantidad_deposito = input("Ingrese la cantidad que desee ingresar: ")
        cantidad = float(cantidad_deposito)
        if cantidad > 0:
            saldo_inicial += cantidad
            print(f"Depósito de {cantidad} realizado.")
            print(f"Saldo actual: {saldo_inicial}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el depósito.")

def retirar():
    global saldo_inicial
    try:
        retiro = float(input("Ingrese la cantidad que desea retirar: "))
        saldo_inicial = saldo_inicial - retiro
        if retiro <= saldo_inicial and retiro > 0:
            print(f"El retiro de {retiro} realizado.")
            print(f"Saldo actual: {saldo_inicial}")
        elif retiro <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        else:
            print("La cuenta no posee fondos suficientes para realizar la operación.")
    except ValueError:
        print("Error. Vuelve a intentarlo")

def generar_ticket():
    print("\n--- TICKET / ESTADO DE LA CUENTA ---")
    print(f"  Cliente:          {usuario}")
    print(f"  Número de Cuenta: {nrandom}")
    print(f"  Saldo Actual:     {saldo_inicial}")
    sys.exit(1)


def mostrar_menu():
    print("\n Menu ")
    print("1. Ingresar un deposito")
    print("2. Ingresa un retiro")
    print("3. Salir")
    #hola

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            depositar()
        elif opcion == '2':
            retirar()
        elif opcion == '3':
            generar_ticket()
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")
if __name__ == "__main__":
    main()