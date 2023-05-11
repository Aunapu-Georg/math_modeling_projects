from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Создание пространства для анимации
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Определение параметров пространственной кривой
N = 100
alpha = np.linspace(10, 0, N)

# Параметрическое задание пространственной кривой
x_move = np.cos(alpha)
y_move = np.sin(alpha)
z_move = alpha * 0.1

# Создание анимируемых объектов
ball, = ax.plot(x_move, y_move, z_move, 'o', color='b') # Сферический объект
line, = ax.plot(x_move, y_move, z_move, '-', color='b') # Линия

# Функция подстановки координат в анимируемую траекторию и мяч
def animate(i):
    ball.set_data(x_move[i], y_move[i])
    ball.set_3d_properties(z_move[i])

    line.set_data(x_move[:i], y_move[:i])
    line.set_3d_properties(z_move[:i])

# Анимирование траектории мяча и него самого
ani = FuncAnimation(fig, animate, N, interval=50)

# Определение параметров поверхности
phi = np.linspace(10, 0, N)
theta = alpha

# Параметрическое задание поверхности
x_surface = np.outer(phi, np.cos(theta))
y_surface = np.outer(phi, np.sin(theta))
z_surface = np.outer(np.ones(np.size(theta)), theta * 0.1)

ax.plot_surface(x_surface, y_surface, z_surface)

# Границы видимой зоны системы координат и названия осей
ax.set_xlim3d([-1.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-1.0, 1.0])
ax.set_zlabel('Z')

# Сохранение итоговой гифки

ani.save('ani.gif')
