
nombre = input("Hola, bienvenido a mi restaurante, por favor, introduzca su nombre: ") # Solicita al usuario que introduzca su nombre

print(f"Hola {nombre}, te voy a mostrar nuestra lista de cinco menús disponibles para escoger:") # Saluda al usuario y muestra los menús disponibles

print("MENÚS:")  # Imprime los menús disponibles
print("   1. Primer menú (Precio: 14,99€) \n         Primer plato: Ensalada completa | Segundo plato: Entrecot de ternera")
print("   2. Segundo menú (Precio: 12,50€)\n         Primer plato: Gazpacho | Segundo plato: Ternera con crema de champiñones")
print("   3. Tercer menú (Precio: 10,70€) \n         Primer plato: Habitas baby con chipirones | Segundo plato: Picantones rellenos")
print("   4. Cuarto menú (Precio: 15,00€)\n         Primer plato: Arroz a la cubana | Segundo plato: Merluza en salsa verde ")
print("   5. Quinto menú (Precio: 13,50€) \n         Primer plato: Ensalada de arroz | Segundo plato: Butifarra con berenjena asada")


menu_escogido = int(input("Seleccione un menú introduciendo el número identificativo (1-5): ")) # Solicita al usuario que seleccione un menú

if menu_escogido < 1 or menu_escogido > 5: # Verificamos que la opción esté dentro del rango permitido
    print("Error: Opción no válida.")
    exit()
numero_personas = int(input("Introduzca el número de personas que habrá que servir: ")) # Solicita al usuario que introduzca el número de personas que serán servidas
postres = input("Introduzca Si/No si quieres postres. Tiene un precio de 3€ por persona: ") # Pregunta al usuario si quiere postres

if postres not in ['Si', 'No']: # Comprueba si la respuesta del usuario es 'Si' o 'No'
    print("Error: Valor no válido.")
    exit()
cafe = input("Seleccione Si/No si quieres café. Tiene un precio de 1€ por persona : ") # Pregunta al usuario si quiere café

if cafe not in ['Si', 'No']: # Comprueba si la respuesta del usuario es 'Si' o 'No'
    print("Error: Valor no válido.")
    exit()

# Se inicializa las variables precio_menu y nombre_menu
precio_menu = 0
nombre_menu = ""

# Dependiendo del menú escogido, asigna el precio y el nombre del menú
if menu_escogido == 1:
    precio_menu = 14.99
    nombre_menu = "Primer plato: Ensalada completa | Segundo plato: Entrecot de ternera"
elif menu_escogido == 2:
    precio_menu = 12.50
    nombre_menu = "Primer plato: Gazpacho | Segundo plato: Ternera con crema de champiñones"
elif menu_escogido == 3:
    precio_menu = 10.70
    nombre_menu = "Primer plato: Habitas baby con chipirones | Segundo plato: Picantones rellenos"
elif menu_escogido == 4:
    precio_menu = 15.00
    nombre_menu = "Primer plato: Arroz a la cubana | Segundo plato: Merluza en salsa verde"
elif menu_escogido == 5:
    precio_menu = 13.50
    nombre_menu = "Primer plato: Ensalada de arroz | Segundo plato: Butifarra con berenjena asada"

# Si el usuario quiere postres, asigna el precio de los postres y si dice que no el precio de los postres es 0
if postres == "Si":
       precio_postres = 3
else:
       precio_postres = 0

# Si el usuario quiere café, asigna el precio del café y si dice que no el precio del café es 0
if cafe == "Si":
       precio_cafe = 1
else:
       precio_cafe = 0

# Calcula el precio total
precio_total = numero_personas * (precio_menu + precio_postres + precio_cafe)

# Dependiendo de si el usuario quiere postres y/o café, imprime el resumen y el precio total
if postres == "No" and cafe == "No":
    print(f"{nombre}, has consumido {numero_personas} unidades del menú \"{nombre_menu}\". El total a pagar es de: {precio_total} €")

elif postres == "Si" and cafe == "No":
    print(f"{nombre}, has consumido {numero_personas} unidades del menú \"{nombre_menu}\" y también {numero_personas if postres == 'Si' else 0} unidades de \"postres\". El total a pagar es de: {precio_total} €")

elif postres == "No" and cafe == "Si":
    print(f"{nombre}, has consumido {numero_personas} unidades del menú \"{nombre_menu}\" y también {numero_personas if cafe == 'Si' else 0} unidades de \"café\". El total a pagar es de: {precio_total} €")

elif postres == "Si" and cafe == "Si":
    print(f"{nombre}, has consumido {numero_personas} unidades del menú \"{nombre_menu}\" y también {numero_personas if postres == 'Si' else 0} unidades de \"postres\" y también {numero_personas if cafe == 'Si' else 0} unidades de \"café\". El total a pagar es de: {precio_total} €")



