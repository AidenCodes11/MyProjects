from math import sqrt

G = 6.67430 * 1e-11

def escape_velocity(mass: int | float, radius: int | float) -> int | float:
    """Mass should be in kilograms and radius should be in meters. The returned value is meters per second."""
    return sqrt(2 * G * mass / radius)

print(f"Escape velocity of earth is: {escape_velocity(5.972 * 1e24, 6_371_000)} m/s")