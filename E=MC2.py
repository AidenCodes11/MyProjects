c = 299_792_458

while True:
    try:
        a = float(input("Enter mass of object (in kgs): "))
        print(f"The energy of that object in joules is: {a * (c ** 2)}")
    except Exception:
        print("Invalid mass")
