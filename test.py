from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Создание пространства для анимации
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Определение параметров пространственной кривой и геликоида
N = 100 # Количество шагов для расчёта параметров (больше = точнее)
step = 5 # Регулирует высоту всей поверхности (прямопропорционально)

alpha = np.linspace(2 * np.pi, 0, N) # Длина траектории мяча

# Параметрическое задание пространственной кривой
x_move = np.cos(alpha) + np.sin(alpha)
y_move = np.sin(alpha) + np.cos(alpha)
z_move = alpha * step

# Создание анимируемых объектов
ball, = ax.plot(x_move, y_move, z_move, 'o', color='b') # Мяч
line, = ax.plot(x_move, y_move, z_move, '-', color='b') # Траектория

# Функция подстановки координат в анимируемую траекторию и мяч
def animate(i):
    ball.set_data(x_move[i], y_move[i])
    ball.set_3d_properties(z_move[i])

    line.set_data(x_move[:i], y_move[:i])
    line.set_3d_properties(z_move[:i])

# Границы видимой зоны системы координат и названия осей
"""
ax.set_xlim3d([np.pi, 2 * np.pi])
ax.set_xlabel('X')

ax.set_ylim3d([-2 * np.pi, 2 * np.pi])
ax.set_ylabel('Y')

ax.set_zlim3d([0, 2 * np.pi * step])
ax.set_zlabel('Z')
"""
# Подстановка координат для анимации

ani = FuncAnimation(fig, animate, N, interval=50)

# Сохранение готовой анимации

ani.save('test.gif')
