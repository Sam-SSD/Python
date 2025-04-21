# Sistema de validación

# Función para validar que el valor ingresado sea un número positivo
def validar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un número positivo")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. por favor, ingrese un número válido.")

#Función para validar que el descuento esté entre 0 y 100
def validar_descuento(mensaje):
    while True:
        try:
            descuento = float(input(mensaje))
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. por favor, ingrese un número válido.")

#Módulo principal para calcular el precio total

#Datos de entrada
print("----------Bienvenido al sistema de validación de productos----------")
nombreProducto = input("Ingrese el nombre del producto: ")
precioUnitario = validar_numero_positivo("Ingrese el precio unitario del producto: ")
cantidad = validar_numero_positivo("Ingrese la cantidad de productos adquiridos: ")
descuento = validar_descuento("Ingrese el porcentaje de descuento (0-100): ")

#Se calcúla el costo sin descuento

costo_total = precioUnitario * cantidad

# Aplicar descuento si corresponde
if descuento > 0:
    costo_total -= costo_total * (descuento / 100)

# Se muestra el resultado formateado
print(f"\nEl costo total de la compra de {nombreProducto} es: ${costo_total:.2f}")
print("--------------------------------------------------------------------")

