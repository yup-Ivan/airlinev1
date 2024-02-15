from utiles.funciones import Airline

if __name__ == "__main__":
    airline = Airline()

    airline.add_flight(101, "New York - Los Angeles", "08:00", "11:00", 200)
    airline.add_flight(102, "Los Angeles - Chicago", "12:00", "15:00", 150)

    airline.add_customer("John Doe", "AB123456")
    airline.add_customer("Jane Smith", "CD987654")

    print(airline.make_reservation(101, "AB123456", 2)) 
    print(airline.make_reservation(102, "CD987654", 1))

    print(airline.cancel_reservation(101, "AB123456"))

    print("\nInformación actualizada:")
    for flight in airline.lista_vuelos:
        print(flight)
    
    for customer in airline.lista_clientes:
        print(customer)