import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x_m, v_x_m, y_m, v_y_m, x_s, v_x_s, y_s, v_y_s = z
    dx_mdt = v_x_m
    dv_x_mdt = - G * M_e * x / (x**2 + y**2)**1.5
    dy_mdt = v_y_m
    dv_y_mdt = 0
    dx_sdt = 0
    dv_x_stdt = v_x_s
    dy_sdt = 0
    dv_y_sdt = v_y_s
    return dx_mdt, dv_x_mdt, dy_mdt, dv_y_mdt, dx_sdt, dv_x_stdt, dy_sdt, dv_y_sdt

G = 6.67 * 10 ** -11
M_e = 5.9742 * 10 ** 24
M_m = 7.36 * 10 ** 22
m_s = 425800
R_e_m = 384403000
Ts_m = 27.322 * 24 * 60 ** 2
v_m = 2 * np.pi * R_e_m / Ts_m

x0_m = 0
v_x0_m = 0
y0_m = 0
v_y0_m = 0
x0_s = 0
v_x0_s = 0
y0_s = 0
v_y0_s = 0

z0 = x0_m, v_x0_m, y0_m, v_y0_m, x0_s, v_x0s, y0_s, v_y0_s

def solve_func(i, key):
    sol = odeint(move_func, z0, t)
    if key == 'moon':
        x = sol[:i, 0]
        y = sol[:i, 2]
    else:
        x = sol[:i, 4]
        y = sol[:i, 6]
    return  x, y
  
fig, ax = plt.subplots()

moon, = plt.plot([], [], 'o', color='y')
satellite, = plt.plot([], [], 'o', color='r')
earth = plt.plot(0, 0, 'o', color='g')

def animate(i):
    moon.set_data(solve_func(i, 'moon'))
    satellite.set_data(solve_func(i, 'satellite'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 0
ax.set_xlim(-edge, edge)
ax.set_ylim(edge, edge)

ani.save('ani.gif')
