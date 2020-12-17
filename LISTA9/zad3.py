from matplotlib import pyplot
import numpy as np

G = 9.81
v = float(input('Proszę wprowadzić prędkość początkową [m/s]: '))
alfa = np.radians(float(input('Proszę wprowadzić kąt rzutu [stopnie]: ')))

h_max = ((v**2)*(np.sin(alfa)**2))/(2*G)
z = ((2*(v**2))*(np.sin(alfa)*np.cos(alfa)))/G
t = (2*v*np.sin(alfa))/G

print('Maksymalna wysokość obiektu wyniesie:', h_max, '[m]')
print('Zasięg obiektu wyniesie:', z, '[m]')
print('Czas lotu obiektu wyniesie:', t, '[s]')

time = np.linspace(0, t, 100)
v_x_0 = v*np.cos(alfa)
v_y_0 = v*np.sin(alfa)

ones = np.linspace(1, 1, 100)
v_y = v_y_0 - G * time
v_x = v_x_0 * ones

pyplot.subplots_adjust(hspace=1)
pyplot.subplot(3, 1, 1)
pyplot.xlabel('t [s]')
pyplot.ylabel('v [m/s]')
pyplot.grid()
pyplot.title('Predkość chwilowa w kierunku pionowym i poziomym po czasie t')
pyplot.plot(time, v_y)
pyplot.plot(time, v_x)

x_t = v_x * time
y_t = v_y_0 * time - (G * time ** 2) / 2
r = np.sqrt(np.power(x_t, 2) + np.power(y_t, 2))

pyplot.subplot(3, 1, 2)
pyplot.xlabel('t [s]')
pyplot.ylabel('r [m]')
pyplot.grid()
pyplot.title('Położenie w funkcji czasu')
pyplot.plot(time, r)

pyplot.subplot(3, 1, 3)
pyplot.xlabel('x [m]')
pyplot.ylabel('y [m]')
pyplot.grid()
pyplot.title('Tor rzutu ukośnego')
pyplot.plot(x_t, y_t)

pyplot.show()