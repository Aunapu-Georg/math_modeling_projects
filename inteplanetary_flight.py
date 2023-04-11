# Импортируем необходимые библиотеки
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
hours = np.pi * np.sqrt()
seconds_in_hour = 60 ** 2
frames = 500
t = np.linspace(0, hours * seconds_in_hour, frames)

# Определяем функцию для системы дифференциальных уравнений
def move_func(s, t):
    x_s, v_x_s, y_s, v_y_s = s
    
    dx_sdt = v_x_s
    dv_x_sdt = - G * moon_mass * x_s / (x_s**2 + y_s**2)**1.5
    dy_sdt = v_y_s
    dv_y_sdt = - G * moon_mass * y_s / (x_s**2 + y_s**2)**1.5
    
    return dx_sdt, dv_x_sdt, dy_sdt, dv_y_sdt

# Определение постоянных и начальных параметров
G = 6.67 * 10**(-11)
moon_mass = 7.3477 * 10**(22)
moon_gravitational_parameter = G * moon_mass
moon_radius = 1737400
satellite_orbit_length = moon_radius + 15000

x_s0 = 0
v_x_s0 = -np.sqrt(moon_gravitational_parameter / satellite_orbit_length)
y_s0 = satellite_orbit_length
v_y_s0 = 0

s0 = (x_s0, v_x_s0, y_s0, v_y_s0)

# Решение системы дифференциальных уравнений
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    x = sol[i, 0]
    y = sol[i, 2]
    return x, y

# Построение решения в виде графика и анимация
fig, ax = plt.subplots()

launch_vehicle, = plt.plot([], [], 'o', color='red', ms=2, label='"Чанчжэн-3В"')
launch_trajectory = odeint(move_func, s0, t)
plt.plot(t, launch_trajectory[:,:], '-', color='tomato', lw=1, label='Траектория ракетоносителя')
plt.plot([0], [0], 'o', color='darkgrey', ms=200)

def animate(i):
    launch_vehicle.set_data(solve_func(i, 'launch_vehicle'))
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

# Оформление координатной плоскости
plt.axis('equal')
edge = 1.5 * satellite_orbit_length
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_xlabel('Ось абсцисс, м')
ax.set_ylabel('Ось ординат, м')
ax.legend(loc='lower right')
plt.title('"Чанчжэн-3В" на окололунной орбите')

ani.save('moon_orbit_flight.gif')

