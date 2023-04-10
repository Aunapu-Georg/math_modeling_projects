# Импортируем необходимые библиотеки
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
days = 27.5
seconds_in_day = 24 * 60 * 60
frames = 500

t = np.linspace(0, days * seconds_in_day, frames)

# Определяем функцию для системы дифференциальных уравнений
def move_func(s, t):
    x_m, v_x_m, y_m, v_y_m, x_s, v_x_s, y_s, v_y_s = s
    
    dx_mdt = v_x_m
    dv_x_mdt = - G * earth_mass * x_m / (x_m**2 + y_m**2)**1.5
    dy_mdt = v_y_m
    dv_y_mdt = - G * earth_mass * y_m / (x_m**2 + y_m**2)**1.5
    dx_sdt = v_x_s
    dv_x_sdt = - G * earth_mass * (x_s - earth_focal_length) / ((x_s - earth_focal_length)**2 + y_s**2)**1.5
    dy_sdt = v_y_s
    dv_y_sdt = - G * earth_mass * y_s / ((x_s - earth_focal_length)**2 + y_s**2)**1.5
    
    return dx_mdt, dv_x_mdt, dy_mdt, dv_y_mdt, dx_sdt, dv_x_sdt, dy_sdt, dv_y_sdt

# Определяем постоянные и начальные параметры
G = 6.67 * 10**(-11)
earth_mass = 5.9742 * 10**(24)
earth_gravitational_parameter = G * earth_mass
moon_mass = 7.3477 * 10**(22)
moon_gravitational_parameter = G * moon_mass

average_earth_moon_distance = 384400000
moon_semi_major_axis = 384748000
moon_perigee = 362600000
moon_apogee = 405400000
moon_eccentricity = 0.0549006
earth_focal_length = moon_semi_major_axis * moon_eccentricity
moon_radius = 1737400
satellite_orbit_length = moon_radius + 15000

x_m0 = moon_semi_major_axis
v_x_m0 = 0
y_m0 = 0
v_y_m0 = np.sqrt(earth_gravitational_parameter * (2 / moon_apogee - 1 / moon_semi_major_axis))
x_s0 = moon_semi_major_axis + satellite_orbit_length
v_x_s0 = 0
y_s0 = 0
v_y_s0 = np.sqrt(moon_gravitational_parameter / satellite_orbit_length)

s0 = (x_m0, v_x_m0, y_m0, v_y_m0, x_s0, v_x_s0, y_s0, v_y_s0)

# Решаем систему дифференциальных уравнений
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'moon':
        x = sol[i, 0]
        y = sol[i, 2]
    elif key == 'moon_trajectory':
        x = sol[:i, 0]
        y = sol[:i, 2]
    elif key == 'launch_vehicle':
        x = sol[i, 4]
        y = sol[i, 6]
    else:
        x = sol[:i, 4]
        y = sol[:i, 6]
    return x, y

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

moon, = plt.plot([], [], 'o', color='darkgrey', ms = 3.5)
moon_trajectory, = plt.plot([], [], '-', color='lightgrey', lw=1)
launch_vehicle, = plt.plot([], [], 'o', color='red', ms=1.5)
launch_vehicle_trajectory, = plt.plot([], [], '-', color='tomato', lw=0.1)
plt.plot([earth_focal_length], [0], 'o', color='royalblue', ms=14)

def animate(i):
    moon.set_data(solve_func(i, 'moon'))
    moon_trajectory.set_data(solve_func(i, 'moon_trajectory'))
    launch_vehicle.set_data(solve_func(i, 'launch_vehicle'))
    launch_vehicle_trajectory.set_data(solve_func(i, 'launch_vehicle_trajectory'))
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 1.5 * x_m0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_xlabel('Ось абсцисс, метры')
ax.set_ylabel('Ось ординат, метры')
plt.title('"Чанчжэн-3В" совершает перлёт с Земной орбиты на Лунную')

ani.save('ani.gif')
