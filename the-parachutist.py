from matplotlib import pyplot as plt

G = 9.81 # constant acceleration (m/s)
B = 14 # mass flow rate (kg/s)
m = 77 # system mass (kg)
h0 = 1200 # initial altitude of system (m)
h_parachute = 800 # activation height of parachute (m)
dt = 0.01 # time step

# internal

h = h0
v = 0 # initial velocity
t = 0 # initial time

time_data = []
velocity_data = []
height_data = []

parachute_time = 0
parachute_velocity = 0
parachute_height = h_parachute

def plot_data():
    plt.subplot(1, 2, 1)
    plt.plot(time_data, velocity_data, linewidth = '2.5')
    plt.scatter(parachute_time, parachute_velocity, color = 'red', label='Parachute Opened')
    plt.title('Velocity over time')
    plt.xlabel('Time (s)')
    plt.ylabel('Absolute velocity (m/s)')
    plt.grid(axis='y', linewidth = '0.5')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(parachute_time, parachute_height, color = 'red', label='Parachute Opened')
    plt.plot(time_data, height_data, linewidth = '2.5')
    plt.title('Height over time')
    plt.xlabel('Time (s)')
    plt.ylabel('Height (m)')
    plt.grid(axis='y', linewidth = '0.5')
    plt.legend()

    plt.suptitle('Parachutist simulation data')
    plt.show()

    print(f"Total time: {time_data[-1]}s")
    print(f"Final velocity: {velocity_data[-1]}m/s")


# simulation loop
def loop():
    global h, v, t, parachute_time, parachute_velocity, parachute_height

    while h > 0:
        if h > h_parachute or G + B/m <= 0:
            v_new = v - G * dt
        else:
            v_new = v - G * dt - (B/m) * v * dt
            if parachute_time == 0:
                parachute_time = t
                parachute_velocity = abs(v)
                parachute_height = h

        v = v_new
        h += v * dt
        t += dt

        time_data.append(t)
        velocity_data.append(abs(v)) 
        height_data.append(h)


def main():
    loop()
    plot_data()

main()