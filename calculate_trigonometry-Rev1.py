import math

sx1 = float(input("First sx value: " + "\n"))
sx2 = float(input("Second sx value: " + "\n"))
sy1 = float(input("First sy value:" + "\n"))
sy2 = float(input("Second sy value" + "\n"))

a = (sx2 - sx1)**2
b = (sy2 - sy1)**2
c = (math.sqrt((a + b)))

print("The answer is: " + "\n" "{:0.2f}".format(c))
