import re

def clean_float(n: str):
    new = n
    if "." in n:
        if re.match(r"0+j?", n.split(".")[1]):
            if "j" in n:
                new = int(n.replace("j", "").split(".")[0] + "." + n.replace("j", "").split(".")[1].rstrip("0") + "j")
            else:
                new = int(float(n))

    return new

if __name__ == "__main__":
    while True:
        a = input("Enter number of light years: ")

        print(f"{clean_float(a)} light years is {clean_float(str(float(a) * (9.461 * 1e12)))} kilometers or {clean_float(str(float(a) * (5.879 * 1e12)))} miles.")