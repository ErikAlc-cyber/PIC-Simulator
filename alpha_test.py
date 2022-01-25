#Just a test, dont try to undestand what Im doing here

#Objective: Get User Input, Base on that simulate some case of decease and read the analythics of that

import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


#Create the sensors to use in the project
class Sensor(object):
    def __init__(self, name, voltaje, Sense, state):
        self.name = name
        self.voltaje = voltaje
        self.number = Sense
        self.state = state
        
    def energy(self, state, AppliedVoltaje):
        if state == "on":
            if AppliedVoltaje > self.voltaje:
                print("Burned Component: "+self.name)
            elif AppliedVoltaje < self.voltaje:
                print("Underpowered Component: "+self.name)
            else:
                print("Component alright: "+self.name)
                self.state = state
        else:
            self.state = "off"
            print("Component off "+self.name)
       
    def change(self, Senseinput):
        self.number = Senseinput
       
    def report(self):
        if self.state == "on":
            return self.number
        else: 
            return "Component off"


#Create an commponent of the circuit
class Component(object):
    def __init__(self, name, voltaje, state):
        self.name = name
        self.voltaje = voltaje
        self.state = state
    
    def energy(self, state, AppliedVoltaje):
        if state == "on":
            if AppliedVoltaje > self.voltaje:
                print("Burned Component: "+self.name)
                exit()
            elif AppliedVoltaje < self.voltaje:
                print("Underpowered Component: "+self.name)
            else:
                print("Component alright: "+self.name)
        else:
            self.state = "off"
            print("Component off "+self.name)
            
motor = Component("Motor", 5, "off")
SPresion = Sensor("Sensor de Presion", 3.3, 0, "off")
        
#What we need to do       
def simulate(opc):
    
    ploters = []
    i = 0
    plt.ion()
    figure, ax = plt.subplots()
    line, = ax.plot(ploters)
    
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Presion(mm de Mercurio)")
    
    while True:
            
        try:
            
            SPresion.energy("on", 3.3)
            if opc == 1:
                point = math.cos(i)
            elif opc == 2:
                point = math.sin(i)
            elif opc == 3:
                point = math.tan(i)
            else:
                print("Error, Opcion no encontrada")
                exit()
            
            SPresion.change(point)
        
            ploters.append(point)
            
            line, = ax.plot(ploters, "r")
            
            figure.canvas.draw()
            figure.canvas.flush_events()
        
            if point <= (math.sin(i)):
                motor.energy("on", 5)
            else:
                motor.energy("off", 0)
        
            i += 1
            time.sleep(0.1)
            
        except KeyboardInterrupt: 
            break
        
        except BufferError:
            break
            
    
    ani = FuncAnimation(figure, simulate, frames= 10, interval=50)    
    motor.energy("off", 0)
    plt.show()

    
#Main Function just to make it simpler
def main():
    print("Pruebas del Simulador de Presion Intracraneal")
    print("0) Salir")
    print("1) Funcion Coseno")
    print("2) Funcion Seno")
    print("3) Funcion Tangente")
    opc = int(input("\n*Seleccione Opcion: "))
    
    if opc != 0:
        simulate(opc)
        print("Reporte Final: \n--Presion Resultante: "+str(SPresion.report()))
        SPresion.energy("off", 0)
           
    else:
        exit()
    
#Anti-Bug State
if __name__ == "__main__":
    while True:
        main()