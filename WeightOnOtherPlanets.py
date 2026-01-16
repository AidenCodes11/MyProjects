# Earth gravity constant
EARTH_GRAVITY = 9.80665  # m/s²

GRAVITY_MAP = {
    "sun": 274.0,
    "moon": 1.62,
    "mercury": 3.7,
    "venus": 8.87,
    "earth": EARTH_GRAVITY,
    "mars": 3.721,
    "ceres": 0.27,
    "jupiter": 24.79,
    "saturn": 10.44,
    "uranus": 8.69,
    "neptune": 11.15,
    "pluto": 0.62,
    "sedna": 0.02,      # Estimated
    "eris": 0.82        # Estimated
}

def weight_on(world: str, earth_weight: float) -> str:
    world = world.lower()
    if world not in GRAVITY_MAP:
        return f"Unknown world: {world}. No gravity ritual available."

    gravity = GRAVITY_MAP[world]
    converted = earth_weight * (gravity / EARTH_GRAVITY)
    return f"On {world.title()}, you'd weigh approximately {converted:.2f} kg."

# Example usage
if __name__ == "__main__":
    your_weight = float(input("Enter your Earth weight in kg: "))
    target_world = input("Enter a celestial body: ")
    print(weight_on(target_world, your_weight))