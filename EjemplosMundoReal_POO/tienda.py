# tienda.py

class Producto:
    def _init_(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        return f"{self.nombre} cuesta ${self.precio:.2f}"

class Cliente:
    def _init_(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)

    def mostrar_carrito(self):
        print(f"Carrito de {self.nombre}:")
        for p in self.carrito:
            print(p.mostrar())

# Ejecución
if __name__ == "_main_":
    pan = Producto("Pan", 0.50)
    leche = Producto("Leche", 1.20)

    cliente = Cliente("María")
    cliente.agregar_al_carrito(pan)
    cliente.agregar_al_carrito(leche)
    cliente.mostrar_carrito()