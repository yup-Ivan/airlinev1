class Flight:

    def __init__(self, num, ruta, hsalida, hllegada, asientos):

        self.numero_vuelo = num
        self.ruta = ruta
        self.hsalida = hsalida
        self.hllegada = hllegada
        self.asientos = asientos

    def __str__(self):
        return f'Numero Vuelo: {self.numero_vuelo}, Ruta: {self.ruta}, HSalida: {self.hsalida}, HLlegada: {self.hllegada}, Asientos Disponibles: {self.asientos}'
    
class Customer:

    def __init__(self, nombre, pasaporte):
        self.nombre = nombre
        self.pasaporte = pasaporte
        self.lista_reservaciones = []

    def __str__(self):
        return f'Nombre: {self.nombre}, Pasaporte: {self.pasaporte}, Reservaciones: {self.lista_reservaciones}'

class Airline:

    def __init__(self):
        self.lista_vuelos = []
        self.lista_clientes = []

    def add_flight(self, num, ruta, hsalida, hllegada, asientos):
        self.lista_vuelos.append(Flight(num, ruta, hsalida, hllegada, asientos))
        return f'Vuelo (con numero de vuelo: {num}) añadido.'

    def remove_flight(self, num):
        for vuelo in self.lista_vuelos:
            if vuelo.numero_vuelo == num:
                self.lista_vuelos.remove(vuelo)
                return 'Vuelo removido.'
        return 'No existe ese vuelo.'

    def add_customer(self, nombre, pasaporte):
        self.lista_clientes.append(Customer(nombre, pasaporte))
        return f'Cliente (con nombre {nombre}) añadido.'

    def remove_customer(self, pasaporte):
        for cliente in self.lista_clientes:
            if cliente.pasaporte == pasaporte:
                self.lista_clientes.remove(cliente)
                return f'Cliente con pasaporte {pasaporte} eliminado.'
        return f'El cliente especificado con pasaporte {pasaporte} no se ha encontrado.'

    def make_reservation(self, num_vuelo, numero_pasaporte, cantidad_asientos):
        for vuelo in self.lista_vuelos:
            if vuelo.numero_vuelo == num_vuelo:
                if vuelo.asientos < cantidad_asientos:
                    return f'No hay suficientes asientos disponibles en el vuelo {num_vuelo}.'
                for cliente in self.lista_clientes:
                    if cliente.pasaporte == numero_pasaporte:
                        cliente.lista_reservaciones.append((vuelo, cantidad_asientos))
                        vuelo.asientos -= cantidad_asientos
                        return f'Reservación realizada para {cantidad_asientos} asientos en el vuelo {num_vuelo}.'
                return f'Cliente no encontrado con el pasaporte ({numero_pasaporte}) especificado.'
        return f'Vuelo con el ID {num_vuelo} no encontrado.'

    def cancel_reservation(self, num_vuelo, num_pasaporte):
        for cliente in self.lista_clientes:
            if cliente.pasaporte == num_pasaporte:
                for reserva in cliente.lista_reservaciones:
                    if reserva[0].numero_vuelo == num_vuelo:
                        cliente.lista_reservaciones.remove(reserva)
                        return f'Reservación cancelada para el vuelo {num_vuelo}.'
                return f'No se encontró ninguna reserva para el vuelo {num_vuelo}.'

        return f'Cliente con pasaporte {num_pasaporte} no encontrado.'