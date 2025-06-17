# Clase que representa un producto en la tienda
class Producto:
    def _init_(self, nombre, precio):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto


# Clase que representa un cliente con un carrito de compras
class Cliente:
    def _init_(self, nombre):
        self.nombre = nombre  # Nombre del cliente
        self.carrito = []     # Lista de productos en el carrito

    def agregar_al_carrito(self, producto):
        # Agrega un producto al carrito
        self.carrito.append(producto)

    def mostrar_carrito(self):
        # Muestra el contenido del carrito y el total a pagar
        print(f"Carrito de {self.nombre}:")
        total = 0
        for producto in self.carrito:
            print(f"- {producto.nombre}: ${producto.precio:.2f}")
            total += producto.precio
        print(f"Total a pagar: ${total:.2f}")


# Este bloque se ejecuta solo si este archivo se ejecuta directamente
if __name__ == "_main_":
    # Crear productos disponibles en la tienda
    pan = Producto("Pan", 0.50)
    leche = Producto("Leche", 1.20)
    arroz = Producto("Arroz", 1.00)

    # Crear un cliente
    cliente = Cliente("María")

    # Agregar productos al carrito del cliente
    cliente.agregar_al_carrito(pan)
    cliente.agregar_al_carrito(leche)
    cliente.agregar_al_carrito(arroz)

    # Mostrar el contenido del carrito del cliente
    cliente.mostrar_carrito()