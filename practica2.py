import time # Se necesita para dormir el programa
import random # Se necesita para obtener la distancia aleatoria a avanzar

participantes = [] # Lista de los participantes de la carrera
distancia_de_meta = 40 # Tamaño de la pista de carreras en metros

class Vehiculo:
    tam_tanque = 0 # Tamaño del tanque de gasolina
    min_distancia = 0 # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 0 # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0 # Distancia recorrida por el vehículo
    aux= tam_tanque

    def __init__(self):
        """Inicializa la clase padre del vehículo"""
        self.tanque = self.tam_tanque # Llena el tanque del vehículo

    def avanzar(self):
        if self.tanque == 0:
                self.tanque = self.tam_tanque
        else:
            self.distancia_recorrida += random.randint(self.min_distancia, self.max_distancia)
            self.tanque-= 1
        """
        Avanza el vehículo una cantidad aleatoria entre
        su distancia mínima y máxima reduciendo 1 unidad
        en su tanque de gasolina. Si este se encuentra vacio
        entonces el vehículo no avanza pero rellena su tanque.
        Si el vehículo ha llegado a la meta este ya no avanza.
        """



class motocicleta(Vehiculo):
    tam_tanque = 3# Tamaño del tanque de gasolina
    min_distancia = 2 # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 5 # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0 # Distancia recorrida por el vehículo
    def __init__(self):
         self.tanque = self.tam_tanque

    def __str__(self):
        return "🚲"

class velero(Vehiculo):
    tam_tanque = 6 # Tamaño del tanque de gasolina
    min_distancia = 2 # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 7 # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0 # Distancia recorrida por el vehículo

    def __init__(self):
        self.tanque = self.tam_tanque

    def __str__(self):
        return "⛵"



class lambo(Vehiculo):
    tam_tanque = 5 # Tamaño del tanque de gasolina
    min_distancia = 1 # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 9 # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0 # Distancia recorrida por el vehículo
    def __init__(self):
        self.tanque = self.tam_tanque

    def __str__(self):
        return "🚕"


class microbus(Vehiculo):
    tam_tanque = 2 # Tamaño del tanque de gasolina
    min_distancia = 3 # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 5 # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0 # Distancia recorrida por el vehículo
    def __init__(self):
        self.tanque = self.tam_tanque

    def __str__(self):
        return "🚃"

class bolt(Vehiculo):
    tam_tanque = 2 # Tamaño del tanque de gasolina
    min_distancia = 3 # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 15 # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0 # Distancia recorrida por el vehículo
    def __init__(self):
        self.tanque = self.tam_tanque

    def __str__(self):
        return "🚶"



def imprime_carrera():
    """Imprime el estado de la carrera"""
    len_pista = 60 # Longitud en ascii del circuito de carreras
    pistas = ""
    for x in range(len(participantes)): # Itera sobre los vehículos
        vehiculo = participantes[x]
        pista = "-"*len_pista
        posicion = (vehiculo.distancia_recorrida * len_pista) // distancia_de_meta
        posicion = min(len_pista,posicion)
        pista = pista[:posicion] + str(participantes[x]) + pista[posicion:]
        pistas += '\n{:2d} '.format(x) + pista
    print(pistas)


def avanza_carrera():
    for p in participantes:
        p.avanzar()
    """Avanza cada coche"""


def juego_terminado():
    """Indica si en el estado actual de la carrera hay al menos un ganador"""
    for x in participantes:
        if x.distancia_recorrida >= distancia_de_meta:
            return True
    return False

def inicializa_participantes(x):
    """Le pregunta al usuario la cantidad y tipos de participantes
    que habrá en la carrera"""
    if x == 1:
        participantes.append(motocicleta())
    elif x == 2:
        participantes.append(velero())
    elif x == 3:
        participantes.append(lambo())
    elif x == 4:
        participantes.append(microbus())
    elif x == 5:
        participantes.append(bolt())


def main():
    print("Juego comenzado.")
    print("Cuantos concusantes quieres?")
    numero = input()
    print(str.format("Tipos de vehiculos:\n"
                      "1. Motocicleta\n"
                      "2. velero\n"
                      "3. Lamborghini\n"
                      "4. Micobus\n"
                      "5. Usain Bolt\n"
                      "*escribe solo el numero*\n"))
    for i in range(int(numero)):
        inicializa_participantes(int(input()))
    print(participantes)

    imprime_carrera()
    while not juego_terminado():
        imprime_carrera()
        time.sleep(1)
        avanza_carrera()

    imprime_carrera()
        # Se encarga de dormir el programa un segundo
    print("Juego terminado.")


main()
