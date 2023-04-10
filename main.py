# Импортируем необходимые библиотеки
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
days = 28
frames = days * 24
seconds_in_day = 24 * 60 * 60

t = np.linspace(0, days * seconds_in_day, frames)

# Определяем функцию для системы дифференциальных уравнений
def move_func(s, t):
    x_m, v_x_m, y_m, v_y_m = s
    
    dx_mdt = v_x_m
    dv_x_mdt = - G * earth_mass * x_m / (x_m**2 + y_m**2)**1.5
    dy_mdt = v_y_m
    dv_y_mdt = - G * earth_mass * y_m / (x_m**2 + y_m**2)**1.5
    
    return dx_mdt, dv_x_mdt, dy_mdt, dv_y_mdt

# Определяем постоянные и начальные параметры
G = 6.67 * 10**(-11)
earth_mass = 5.9742 * 10**(24)
average_earth_moon_distance = 384400000
moon_semi_major_axis = 384748000
moon_perigee = 362600000
moon_apogee = 405400000
moon_gravitational_parameter = G * earth_mass
moon_eccentricity = 0.0549006
moon_focal_length = moon_semi_major_axis * moon_eccentricity

x_m0 = moon_semi_major_axis
v_x_m0 = 0
y_m0 = 0
v_y_m0 = np.sqrt(moon_gravitational_parameter * (2 / moon_apogee - 1 / moon_semi_major_axis))

s0 = (x_m0, v_x_m0, y_m0, v_y_m0)

# Решаем систему дифференциальных уравнений
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'satellite':
        x_m = sol[i, 0]
        y_m = sol[i, 2]
    else:
        x_m = sol[:i, 0]
        y_m = sol[:i, 2]
    return x_m, y_m

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

moon, = plt.plot([], [], 'o', color='darkgrey')
moon_trajectory, = plt.plot([], [], '-', color='lightgrey')
plt.plot([moon_focal_length], [0], 'o', color='royalblue', ms=20)

def animate(i):
    moon.set_data(solve_func(i, 'satellite'))
    moon_trajectory.set_data(solve_func(i, 'trajectory'))
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2 * x_m0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('ani.gif')
