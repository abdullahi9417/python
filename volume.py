n = 100
dx = 1 / n
dy = 1 / n
volume = 0

for i in range(n):
    for j in range(n):
        x = i * dx
        y = j * dy
        z = x**2 + y**2
        volume += z * dx * dy

print(f"Approximate volume under z = x² + y²: {volume:.4f}")