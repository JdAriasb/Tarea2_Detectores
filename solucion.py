import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("datos.dat")


datoslog = np.log10(datos)


c = np.polyfit(datoslog[:,0],datoslog[:,1],2)
print("a = {}, b = {}, c = {}".format(c[0], c[1], c[2]))

def curvalog(x):
    return c[0]*x**2 + c[1]*x + c[2]

def curva(x):
    return(x**(c[1]+c[0]*np.log10(x))*10**(c[2]))

x = np.linspace(datos[0,0],datos[-1,0],1000)

plt.figure()
plt.loglog()
plt.scatter(datos[:,0],datos[:,1], label = "Datos reportados")
plt.grid()
plt.title("dE/dx en función de la energía de los protones")
plt.xlabel("Energía [MeV]")
plt.ylabel("dE/dx [keV/mm]")
plt.savefig("Gráfica0.eps")

plt.figure()
plt.loglog()
plt.scatter(datos[:,0],datos[:,1], label = "Datos reportados")
plt.plot(x, curva(x), label="Curva", c = "red")
# plt.plot(x, curva2(x), label="Curva2", c = "green")
plt.grid()
plt.legend()
plt.title("dE/dx en función de la energía de los protones")
plt.xlabel("Energía [MeV]")
plt.ylabel("dE/dx [keV/mm]")
plt.savefig("Gráfica.eps")


deltaX = 0.001
ener0 = 100
n = 100
de = curva(100)

profundidad = np.zeros((40000,2))
profundidad[0,:]= 0, ener0
deltaE = np.zeros(len(profundidad[:,0]))

for i in range(1,len(profundidad[:,0])):
    Nprof = profundidad[i-1,0] + deltaX
    if profundidad[i-1,1] <= 0 :
        print("El alcance máximo es de {} mm".format(profundidad[i-1,0]))
    Nener = profundidad[i-1,1] - curva(profundidad[i-1,1])*deltaX
    deltaE[i] = curva(profundidad[i-1,1])*deltaX
    profundidad[i] = Nprof, Nener

plt.figure()
plt.plot(profundidad[:,0],profundidad[:,1])
plt.grid()
plt.title("Alcance en x de los protones incidentes")
plt.xlabel("Profundidad en x [mm]")
plt.ylabel("Energía de los protones [MeV]")
plt.savefig("Gráfica2.eps")

plt.figure()
plt.plot(profundidad[:,0],deltaE)
plt.grid()
plt.title("ΔE en función de la profundidad")
plt.xlabel("Profundidad en x [mm]")
plt.ylabel("ΔE [MeV]")
plt.savefig("Gráfica3.eps")
