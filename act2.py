from abc import ABC, abstractmethod

class Habitacion:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def reservar(self):
        print(f"Habitación {self.numero} con capacidad para {self.capacidad} personas reservada.")

class ServicioAdicional(ABC):
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    @abstractmethod
    def ofrecer(self):
        pass

class Restaurante(ServicioAdicional):
    def ofrecer(self):
        print(f"Restaurante '{self.nombre}', costo adicional: ${self.costo} por persona.")

class Spa(ServicioAdicional):
    def ofrecer(self):
        print(f"Spa '{self.nombre}', costo adicional: ${self.costo} por día.")

class Hotel:
    def __init__(self, nombre_hotel, habitacion, servicios):
        self.nombre_hotel = nombre_hotel
        self.habitacion = habitacion
        self.servicios = servicios

    def generar_reserva(self):
        print(f"Generando reserva en el hotel '{self.nombre_hotel}'")
        self.habitacion.reservar()
        for servicio in self.servicios:
            servicio.ofrecer()

habitacion = Habitacion(13, 3)
restaurante = Restaurante("Sirenita", 100)
spa = Spa("Don Chuy", 50)

hotel_california = Hotel("Hotel California", habitacion, [restaurante, spa])
hotel_california.generar_reserva()