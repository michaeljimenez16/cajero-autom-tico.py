saldo = 1000
pin_secreto = "1234"

print("Bienvenido a TechBank Riwi Digital")
pin = input("Ingrese su Pin: ")

if pin == pin_secreto:
    print("¡Acceso concedido!")
    
    while True: 
        print("\n MENÚ PRINCIPAL")
        print("1. Saldo | 2. Retiro | 3. Depósito | 4. Salir")
        
        op = input("Seleccione (1-4): ")

        if op == "1":
            print(f"Su saldo es: ${saldo}")

        elif op == "2":
            monto = float(input("¿Cuánto retirar?: "))
            if monto > saldo:
                print("Error: Fondos insuficientes.")
            elif monto <= 0:
                print("Error: Monto inválido.")
            else:
                saldo -= monto
                print(f"Retiro exitoso. Saldo: ${saldo}")
        elif op == "3":
            monto = float(input("¿Cuánto depositar?: "))
            if monto <= 0:
                print("Error: Monto inválido.")
            else:
                saldo += monto
                print(f"Depósito exitoso. Saldo: ${saldo}")

        elif op == "4":
            print("Gracias por usar el cajero automático")
            break
            
        else:
            print("Opción no válida.")

else:
    print("PIN incorrecto.")
  
