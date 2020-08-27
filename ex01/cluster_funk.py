"""This program calculates t1-t4 with the inputs, r0 and t0."""
__author__= "Andy Chen"
"730344991"

r0 = float(input("Enter R0: "))
t0 = int(input("Enter t0 Cluster Size: "))

new = round(t0 * r0)
total = (t0 + new)
print("t1 - new: " + str(new) +  " - Total: " + str(total))

new = round(new * r0)
total = new + total
print("t2 - new: " + str(new)  +  " - Total: " + str(total))

new = (round(new * r0))
total = (new + total)
print("t3 - new: " + str(new)  +  " - Total: " + str(total))

new = round(new * r0)
total = new + total
print("t4 - new: " + str(new)  +  " - Total: " + str(total))

