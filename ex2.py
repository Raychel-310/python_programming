import matplotlib.pyplot as plt

m, k, d = 0.2, 1.0, 0.2
t, t_end = 0.0, 10
dt = 0.1

x0, v0 = 1.0, 0.0
v1, x1 = v0, x0
v2, x2 = v0, x0

times1 = []
positions1 = []
times2 = []
positions2 = []

while t < t_end:
    times1.append(t)
    positions1.append(x1)
    v1_next = -k / m * dt * x1 + (1 - d / m * dt) * v1
    x1_next = x1 + dt * v1
    v1 = v1_next
    x1 = x1_next

    v2_next = v2 + dt * (1 / m * (-k * (x2 + dt * v2 / 2)) - d * (v2 + dt * (-k * x2 - d * v2) / (2 * m)))
    x2_next = x2 + dt * (v2 + dt * (-k * x2 - d * v2) / (2 * m))
    v2 = v2_next
    x2 = x2_next

    times2.append(t)
    positions2.append(x2)

    t += dt

plt.plot(times1, positions1, label="E_method")
plt.plot(times2, positions2, label="RK_method")
plt.xlabel('time [s]')
plt.ylabel("x [m]")
plt.grid(True)
plt.legend()
plt.show()