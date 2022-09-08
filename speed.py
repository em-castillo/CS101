import math
mass = float(input("Mass (in kg): "))
earth_gravity = float(input("Gravity (in m/s^2, 9.8 for Earth): "))
jupiter_gravity = float(input("Gravity (in m/s^2, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
p_density = float(
    input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A_area = float(input("Cross sectional area (in m^2): "))
C_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()
c = (1/2) * p_density * A_area * C_constant
print(f'The inner value of c is: {c:.3f}')
v_earth = math.sqrt(mass * earth_gravity / c) * \
    (1 - math.exp((-math.sqrt(mass * earth_gravity * c) / mass) * time))
v_jupiter = math.sqrt(mass * jupiter_gravity / c) * \
    (1 - math.exp((-math.sqrt(mass * jupiter_gravity * c) / mass) * time))
print(f'The velocity for Earth after {time} seconds is: {v_earth:.3f} m/s')
print(f'The velocity for Jupiter after {time} seconds is: {v_jupiter:.3f} m/s')
# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
