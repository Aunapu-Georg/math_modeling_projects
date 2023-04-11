# Импортируем необходимые библиотеки
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определение постоянных и вычисление необходимых параметров на их основе
G = 6.67 * 10**(-11)
earth_mass = 5.9742 * 10**(24)
earth_gravitational_parameter = G * earth_mass
moon_mass = 7.3477 * 10**(22)
moon_gravitational_parameter = G * moon_mass
geostationary_orbit_length = 42164000
moon_earth_length = 384400000

a_s = (geostationary_orbit_length + moon_earth_length) / 2
t_flight = 2 * np.pi * np.sqrt(a_s ** 3 / earth_gravitational_parameter)
moon_velocity = np.sqrt(earth_gravitational_parameter / moon_earth_length)
moon_orbit_length = 2 * np.pi * moon_earth_length
Ts_moon = moon_orbit_length / moon_velocity
w_moon = 360 / Ts_moon
beta = w_moon * t_flight

frames = 500
t = np.linspace(0, t_flight, frames)

# Определяем функцию для системы дифференциальных уравнений
def move_func(s, t):
    x_s, v_x_s, y_s, v_y_s = s
    
    dx_sdt = v_x_s
    dv_x_sdt = - G * moon_mass * x_s / (x_s**2 + y_s**2)**1.5
    dy_sdt = v_y_s
    dv_y_sdt = - G * moon_mass * y_s / (x_s**2 + y_s**2)**1.5
    
    return dx_sdt, dv_x_sdt, dy_sdt, dv_y_sdt

# Определение начальных параметров

x_m0 = -???
v_x_m0 = 0
y_m0 = +-???
v_y_m0 = 0
x_s0 = 0
v_x_s0 = -np.sqrt(earth_gravitational_parameter * (2 / geostationary_orbit_length - 1 / a_s))
y_s0 = -geostationary_orbit_length
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

moon, = plt.plot([], [], 'o', color='darkgrey', ms=8, label='Луна')
moon_trajectory, = plt.plot([], [], '-', color='lightgrey', label='Траектория Луны')
launch_vehicle, = plt.plot([], [], 'o', color='red', ms=2, label='"Чанчжэн-3В"')
launch_vehicle_trajectory, = plt.plot([], [], '-', color='tomato', lw=1, label='Траектория ракетоносителя')
plt.plot([0], [0], 'o', color='royalblue', ms=32)

def animate(i):
    moon.set_data(solve_func(i, 'moon'))
    moon_trajectory.set_data(solve_func(i, 'moon_trajectory'))
    launch_vehicle.set_data(solve_func(i, 'launch_vehicle'))
    launch_vehicle_trajectory.set_data(solve_func(i, 'launch_vehicle_trajectory'))
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

# Оформление координатной плоскости
plt.axis('equal')
edge = 1.5 * moon_earth_length
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_xlabel('Ось абсцисс, м')
ax.set_ylabel('Ось ординат, м')
ax.legend(loc='lower right')
plt.title('Перелёт "Чанчжэн-3В" с Земной орбиты на Лунную')

ani.save('interplanetary_flight.gif')

