import matplotlib.pyplot as plt

# Temperature readings
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Plot
plt.plot(days, temperatures, marker='o', linestyle='-', color='green')
plt.title('Weekly Temperature Readings')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()