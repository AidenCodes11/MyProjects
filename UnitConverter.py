from decimal import Decimal, getcontext
from typing import Literal

getcontext().prec = 45

Unit = Literal["mm", "cm", "dm", "m", "km", "in", "ft", "yd", "mi", "oz", "lb", "tn", "t", "mg", "g", "kg", "ltn", "c", "f", "k", "sec", "min", "hr", "day"]

length_units = {
    "mm": Decimal("0.001"),
    "cm": Decimal("0.01"),
    "dm": Decimal("0.1"),
    "m": Decimal("1.0"),
    "km": Decimal("1000.0"),
    "in": Decimal("0.0254"),
    "ft": Decimal("0.3048"),
    "yd": Decimal("0.9144"),
    "mi": Decimal("1609.34")
}

weight_units = {
    "mg": Decimal("0.001"),
    "g": Decimal("1.0"),
    "kg": Decimal("1000.0"),
    "t": Decimal("1_000_000.0"),
    "oz": Decimal("28.3495"),
    "lb": Decimal("453.592"),
    "tn": Decimal("907_184.7"),
    "ltn": Decimal("1_016_046.9")
}

temp_units = {
    "c": None,
    "f": None,
    "k": None,
}

def unit_type(unit: str) -> dict[str, Decimal] | None:
    if unit in length_units.keys():
        return length_units
    elif unit in weight_units.keys():
        return weight_units
    elif unit in temp_units.keys():
        return temp_units
    else:
        return None

def convert_temperature(value: Decimal, from_unit: str, to_unit: str) -> Decimal:
    # Convert to Celsius first
    if from_unit == "f":
        celsius = (value - Decimal("32")) * Decimal("5") / Decimal("9")
    elif from_unit == "k":
        celsius = value - Decimal("273.15")
    else:
        celsius = value

    # Convert from Celsius to target
    if to_unit == "f":
        return celsius * Decimal("9") / Decimal("5") + Decimal("32")
    elif to_unit == "k":
        return celsius + Decimal("273.15")
    else:
        return celsius

def convert(value: Decimal, from_unit: Unit, to_unit: Unit, used_dict: dict) -> Decimal:
    if used_dict == temp_units:
        return convert_temperature(value, from_unit, to_unit)

    base = value * used_dict[from_unit]
    return base / used_dict[to_unit]

if __name__ == "__main__":
    print("Enter units as their abbriviations. Like \"centimeter\" = \"cm\".", end="\n\n")
    while True:
        try:
            unit_1 = input("Enter unit to convert from: ").lower().strip()
            val = Decimal(input("Enter amount of that unit: "))
            unit_2 = input("Enter unit to convert to: ").lower().strip()
            if unit_type(unit_1) != unit_type(unit_2):
                raise NameError

            print(f"{val} {unit_1} = {convert(val, unit_1, unit_2, unit_type(unit_1))} {unit_2}")

        except Exception:
            print("Unsupported Conversion")