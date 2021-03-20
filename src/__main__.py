#!/usr/bin/python3

import socket

class Escaner:

    def __init__(self):
        self.ip = input("OBJETIVO: ")
        self.puertosAbiertos = []

    def iniciarEscaneo(self):
        try:
            for self.puerto in range(1,6500):
                #Objeto socket
                self.escaner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                # Obteniento estado del puerto 
                self.estadoPuerto = self.escaner.connect_ex((self.ip,self.puerto))
                # No esperar mas de 1 segundo a la respuesta del puerto
                self.escaner.settimeout(0.2)
                # Verificar el estado del puerto (abierto o cerrado | 0 o 1)
                if estadoPuerto == 0:
                    self.puertosAbiertos.append(self.estadoPuerto)
                    print(f"TCP|{self.puerto} [abierto]")
                
                # Cerrar conexion con objetivo
                self.escaner.close()

        # Si se rechaza la conexión generamos la excepción
        except ConnectionRefusedError as e:
            print("Conexión rechazada")
    
    def estadoDePuertos(self):
    
        self.abiertos = len(self.puertosAbiertos)
        self.cerrados = (65535 - len(self.puertosAbiertos)) 
        print(f"""PUERTOS Abiertos: {self.abiertos} Cerrados: {self.cerrados}""")