from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Создание пространства для анимации
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Определение параметров пространственной кривой
N = 100
alpha = np.linspace(10, 0, N)

# Параметрическое задание пространственной кривой
x = np.cos(alpha)
y = np.sin(alpha)
z = alpha * 0.1

# Создание анимируемых объектов
ball, = ax.plot(x, y, z, 'o', color='b') # Сферический объект
line, = ax.plot(x, y, z, '-', color='b') # Линия

# Функция подстановки координат в анимируемые объекты
def animate(i):
    ball.set_data(x[i], y[i])
    ball.set_3d_properties(z[i])

    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])

# Украшательсвта и масштабирование
ax.set_xlim3d([-1.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-1.0, 1.0])
ax.set_zlabel('Z')

# Анимирование
ani = FuncAnimation(fig, animate, N, interval=50)

ani.save('ani.gif')
