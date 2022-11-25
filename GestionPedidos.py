class Producto:
  def __init__ (self, ref_prod, nom_prod, precio, existencias): 
       self.ref_prod = ref_prod
       self.nom_prod = nom_prod
       self.precio = precio
       self.existencias = existencias

# Producto <--- Factura
# Una factura, se compone de varios productos más algunos parametros adicionales
# como puede ser la cantidad de cada producto comprado. Por lo cual va a heredar la Clase producto

class Factura (Producto):
    def __init__ (self, ref_prod, nom_prod, precio, existencias, cantidad, subtotal, tasas, total):
        super().__init__ (ref_prod, nom_prod, precio, existencias)
        self.cantidad = cantidad
        self.subtotal = subtotal
        self.tasas = tasas
        self.total = total

class Cliente:
  def __init__ (self, nombrecli, direccioncli, nifcli, telfcli, mailcli, tasascli ):
    self.nombrecli = nombrecli
    self.direccioncli = direccioncli
    self.nifcli = nifcli
    self.telfcli = telfcli
    self.mailcli= mailcli
    self.tasascli = tasascli

i=0
Lista_productos=[] #todavía no se utilizar ficheros o una BBDD en py, entonces guardo los productos en una lista.
def consultar_catalogo():
    k = 0
    while k < len(Lista_productos):
        print (Lista_productos[k].ref_prod, " ", Lista_productos[k].nom_prod, " ", "El precio unidad es:", Lista_productos[k].precio, "€", "disponibles:", Lista_productos[k].existencias)
        k+=1

Lista_clientes=[] 
def mostrar_cliente():
  j = 0
  while j < len(Lista_clientes):
    print ("Bienvenido" , Lista_clientes[j].nombrecli, " ",Lista_clientes[j].mailcli,"\n")
    j+=1

Lista_factura=[]
def componer_factura():
    x = 0
    total_factura = 0
    print("--- Desglose de factura ---") 
    while x < len(Lista_factura):
        print(Lista_factura[x].nom_prod, " precio:",Lista_factura[x].precio,"€ cant:",
        Lista_factura[x].cantidad, "Subtot:",Lista_factura[x].subtotal, "€ - IVA",Lista_factura[x].tasas, "€ -TOTAL: ", 
        Lista_factura[x].total,"€")
        total_factura = total_factura + Lista_factura[x].total
        x+=1
    print("----------------------------------------------------------")
    print('EL TOTAL A PAGAR :........................................',total_factura,'€')
    print("Se envia la factura por correo :")
    print('Se manda un SMS a tu telefono:')


while i==0:
  print("---- ***** Menu de mi Aplicación ***----\n")
  print("1.- Registrar un Cliente")
  print("2.- Registrar un Producto")
  print("3.- Consultar Catálogo Productos")
  print("4.- Seleccionar producto y Comprar")
  print("5.- Salir")
  opcion = int(input())
  if opcion==1:
    print ("--- Registrar un Cliente ---")
    nom = input("introduzca su nombre de Cliente:")
    dir = input("introduce su direccion de Cliente:")
    nif = input("introduce su NIF:")
    telf = input("escriba el telefono móvil:")
    mail = input("introduce la dirección de correo electronico:")
    tax = input("por favor indique el porcentaje que debemos aplicar a sus facturas (iva o igic):")
    cli = Cliente(nom, dir, nif, telf, mail, tax)
    Lista_clientes.append(cli) # Añadimos el cliente a una lista (en la ultima posición)
    print ("\n\n -- El Cliente se ha registrado en la Aplicación con éxito -- \n")
    mostrar_cliente()
  elif opcion==2:
    print ("\n--- Registrar un Producto ---")
    ref = input("introduce la referencia del producto:")
    nom = input("introduce el nombre del producto:")
    pre = input("introduce el precio del producto:")
    stock = input("introduce la cantidad de existencias del producto:")
    articulo = Producto(ref, nom, pre, stock)
    Lista_productos.append(articulo) # Añadimos el producto a una lista que será nuestro catalogo
    print ("\n El Producto se ha guardado en el catálogo correctamente \n")
  elif opcion==3:
    print ("\n --- Consultar Catálogo Productos --")
    consultar_catalogo() 
  elif opcion==4:
    print("\n -- Seleccionar productos del catalogo y comprar --\n") 
    print("-- Los productos disponibles en el catalogo son: --\n") 
    consultar_catalogo()

   # Aquí empezaríamos a llenar el carro. 
   # Pregunta al cliente si desea comprar mas articulos hasta que este diga que no
   # ¿Desea seguir comprando? S/N (los añadimos a la lista)
    continuar = "S"
    while continuar == "S":
        autoref=1
        print("indica el nombre del producto que desea comprar:")
        prod = input()
        print("indica la cantidad a comprar de:", prod)
        cant_pedido= int(input())
        print("indica el precio de catalogo del producto de:", prod)
        prod_pre = float(input())
        prod_subtotal = prod_pre * cant_pedido
        IVA = prod_subtotal * 0.21
        total_articulo = prod_subtotal + IVA 
        linea_fra = Factura(autoref, prod, prod_pre, None, cant_pedido, prod_subtotal, IVA, total_articulo)
        Lista_factura.append(linea_fra)
        print("\n Su producto se añadio al carro,  ¿Desea seguir comprando? S/N ")
        autoref=+1
        continuar = input()
        
    componer_factura()    
    
    #
   
  #

   

  elif opcion==5:
    print ("Salir de la Aplicación")
    exit()
  else:
    print ("Opcion invalida")    