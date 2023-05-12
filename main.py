from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Создание пространства для анимации
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Определение параметров пространственной кривой и геликоида
N = 100
step = 3
extension = 2 # Прямопропорциональна радиусу спирали, по которой движется мяч
size = 2 * np.pi

width = size / 2
height = size

alpha = np.linspace(size, 0, N) # Длина траектории мяча

phi = np.linspace(0, width, N) # "Ширина" поверхности
theta = np.linspace(0, height, N) # "Высота" поверхности

# Параметрическое задание пространственной кривой
x_move = extension * np.cos(alpha)
y_move = extension * np.sin(alpha)
z_move = alpha * step

# Создание анимируемых объектов
ball, = ax.plot(x_move, y_move, z_move, 'o', color='b') # Сферический объект
line, = ax.plot(x_move, y_move, z_move, '-', color='b') # Линия

# Функция подстановки координат в анимируемую траекторию и мяч
def animate(i):
    ball.set_data(x_move[i], y_move[i])
    ball.set_3d_properties(z_move[i])

    line.set_data(x_move[:i], y_move[:i])
    line.set_3d_properties(z_move[:i])

# Параметрическое задание поверхности
x_surface = np.outer(phi, np.cos(theta))
y_surface = np.outer(phi, np.sin(theta))
z_surface = np.outer(np.ones(np.size(theta)), theta * step)

ax.plot_surface(x_surface, y_surface, z_surface)

# Границы видимой зоны системы координат и названия осей

ax.set_xlim3d([-width, width])
ax.set_xlabel('X')

ax.set_ylim3d([-width, width])
ax.set_ylabel('Y')

ax.set_zlim3d([0, height * step])
ax.set_zlabel('Z')

# Подстановка координат для анимации

ani = FuncAnimation(fig, animate, N, interval=50)

# Сохранение готовой анимации

ani.save('ani.gif')
