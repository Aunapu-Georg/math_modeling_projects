import numpy as np

G = 6.67 * 10**(-11)
earth_mass = 5.9742 * 10**(24)
earth_gravitational_parameter = G * earth_mass
# moon_mass = 7.3477 * 10**(22)
# moon_gravitational_parameter = G * moon_mass
geostationary_orbit_length = 42164000
moon_earth_length = 384400000

a_s = (geostationary_orbit_length + moon_earth_length) / 2
t_flight = 2 * np.pi * np.sqrt(a_s ** 3 / earth_gravitational_parameter)
moon_velocity = np.sqrt(earth_gravitational_parameter / moon_earth_length)
moon_orbit_length = 2 * np.pi * moon_earth_length
Ts_moon = moon_orbit_length / moon_velocity
w_moon = 360 / Ts_moon
beta = w_moon * t_flight

print(beta)
