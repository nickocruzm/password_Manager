
height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / height ** 2

if height > 3:
    raise ValueError("height is not possible")

