def get_bmi(weight, height, unit="ft"):
    """Weight is in kilogarms. This function returns the body mass index (BMI) depending on weight and height."""
    if unit == "ft":
        height *= 0.3048
    elif unit == "cm":
        height *= 100
    elif unit == "in":
        height *= 0.3048 * 12
    elif unit == "m": pass
    else:
        return "Unsupported Unit!"

    return weight / (height ** 2)

if __name__ == "__main__":
    unit = input("Enter unit you want to mesure your height in (abbriviate the measurement): ").rstrip(".")
    w = float(input("What is your weight (in kilograms): "))
    h = float(input("What is your height: "))
    bmi = get_bmi(w, h, unit)
    if bmi == "Unsupported Unit!":
        print("Unsupported Unit!")
    else:
        print(f"Your body mass index (BMI) is: {get_bmi(w, h, unit)}")