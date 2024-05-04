class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def asignar_estado(self, experiencia):
        temp_exp = self.experiencia + experiencia
        
        if experiencia > 0:
            self.nivel += temp_exp // 100
        elif experiencia < 0:
            if temp_exp < 0 and self.nivel > 1:
                self.nivel -= (-temp_exp) // 100
        
        self.experiencia = max(temp_exp, 0)

    def __lt__(self, otro):
        return self.nivel < otro.nivel

    def __gt__(self, otro):
        return self.nivel > otro.nivel

    def __eq__(self, otro):
        return self.nivel == otro.nivel

    @staticmethod
    def calcular_probabilidad(jugador, orco):
        if jugador < orco:
            return 33
        elif jugador > orco:
            return 66
        else:
            return 50

    @staticmethod
    def dialogo_enfrentamiento(jugador, orco, probabilidad):
        print("¡Oh no!, ¡Ha aparecido un Orco!")
        print(f"Con tu nivel actual, tienes {probabilidad}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        opcion = int(input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n"))
        return opcion
