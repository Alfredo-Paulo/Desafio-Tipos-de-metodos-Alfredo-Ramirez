import random
from personaje import Personaje

class Juego:
    def __init__(self):
        print("¡Bienvenido a Gran Fantasía!")
        nombre_personaje = input("Por favor indique nombre de su personaje: ")
        self.jugador = Personaje(nombre_personaje)
        print(self.jugador.obtener_estado())

    def comenzar(self):
        orco = Personaje("Orco")
        probabilidad = Personaje.calcular_probabilidad(self.jugador, orco)
        opcion = Personaje.dialogo_enfrentamiento(self.jugador, orco, probabilidad)

        while opcion == 1:  # Atacar
            resultado = random.uniform(0, 1)
            if resultado <= probabilidad / 100:
                print("¡Le has ganado al orco, felicidades!")
                print("¡Recibirás 50 puntos de experiencia!")
                self.jugador.asignar_estado(50)
                orco.asignar_estado(-30)
            else:
                print("¡Has perdido contra el orco!")
                print("Perderás 30 puntos de experiencia.")
                self.jugador.asignar_estado(-30)
                orco.asignar_estado(50)
            print(self.jugador.obtener_estado())
            print(orco.obtener_estado())

            probabilidad = Personaje.calcular_probabilidad(self.jugador, orco)
            opcion = Personaje.dialogo_enfrentamiento(self.jugador, orco, probabilidad)

        if opcion == 2:  # Huir
            print("Has decidido huir. ¡El orco ha quedado atrás!")

juego = Juego()
juego.comenzar()
