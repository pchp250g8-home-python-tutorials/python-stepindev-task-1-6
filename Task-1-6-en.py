# --coding:utf-8--
n = int(input("Enter fence length (in meters): "))  # Fence length
# --Paint consumption rate--
k = int(input("How many meters does a can of paint last for? "))
# Cost of one can of paint
c = int(input("Price of one can of paint (in rubles):"))
# Number of cans of paint for the entire length of the fence
b = n // k + n % k
p = b * c  # Cost of all cans of paint for the entire fence
# -- Display information on the screen --
print(f"{b} cans of paint are needed for {n} meters of fence.")
print(f"{p} rubles are needed for {b} cans of paint.")
