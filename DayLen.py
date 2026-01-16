from decimal import Decimal, getcontext

getcontext().prec = 100

PI = Decimal("3.14159265358979323846264338327950288419716939937510")

def day_len(v: int | float | Decimal, r: int | float | Decimal) -> int | float | Decimal:
    """v is in m/s and r is in meters. Returned value is in hours."""
    return ((Decimal("2") * PI * r) / v) / Decimal("3600")

v = Decimal("465.1013")       # refined equatorial speed
r = Decimal("6378137")        # equatorial radius

print(day_len(v, r))