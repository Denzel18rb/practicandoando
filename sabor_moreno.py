#la señora de la tienda quiere una aplicacion para su caja 
#que sume precios 
#e imrpima un resumen de la compra:

print("Bienvenido al menu virtual")
nombre_cliente = str(input("diganos como se llama para su recibo: "))
#numero_platos = int(input("digamos el numero de platos que desea ordenar: "))
print("############MENU##############")
print("Carapulcra: s/26 codigo(p1)")
print("arroz con pollo: s/20 codigo(p2)")
print("chicharron(pota): s/.13 codigo(p3)")
print("chicharron(chancho): s/.15 codigo(p4)")
print("arroz chaufa: s/.20 codigo(p5)")
print("##############################")

p1 = 26
p2 = 20
p3 = 13
p4 = 15
p5 = 20


carapulcra = p1

acpollo =  p2

chicharron1 = p3

chicharron2 = p4

chaufa = p5


menu = {
    "p1": {"comida":"carapulcra", "precio": 26},
    "p2": {"comida":"arroz c/ pollo", "precio": 20},
    "p3": {"comida":"chicharron(pota)", "precio": 13},
    "p4": {"comida":"chicharron(chancho)", "precio": 15},
    "p5": {"comida":"arroz chaufa", "precio": 20},
}

#almacenimientos de pedidos /// lista del diccionario "menu"
pedido = []

#solicitamos codigos de comida al cliente
while True:
    codigo = str(input("escriba el codigo del producto deseado/-/escriba 'pagar' para finalizar la compra: "))
    if codigo.lower() == 'pagar':
        break
    elif codigo in menu:
        pedido.append(menu[codigo])
    else:
        print("lo sentimos, pero el codigo ingresado no es valido")

#calcular el total de plata pa gastar
total = sum([item["precio"] for item in pedido])
#resumen de orde
orden = str([item["comida"] for item in pedido])
#mostrar los detalles del pedido y su precio
print("#____________________________________________________________________#")
print("\nSu pedido:")
print(f"{nombre_cliente}")
print(f"Resumen de compra:\n{orden}")
print(f"\nEl total es: s/.{total}")
print("#____________________________________________________________________#")











#____________________________________________#
#verificacion de codigos:
#if codigo in menu:
   # plato_elegido = menu[codigo]
    #print(f"Su pedido es {plato_elegido}")
#else:
    #print("lo sentimos, pero su codigo no es valido")



#pedido = 1 

#str(input("escriba el codigo del producto deseado: "))

#while pedido <= numero_platos:
    #comida = int(input(f"ingrese el codigo del platillo {pedido}: "))









#menu = print(f"{carapulcra}{acpollo}{chicharron1}{chicharron2}{chaufa}")