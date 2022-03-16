

while True:
    p1 = str(input("P1 select option r, p or s: ").lower())
    if p1 in ["r", "p", "s"]: break
    print("Please select the right option")
        

while True:
    p2 = str(input("P1 select option r, p or s: ").lower())
    if p2 in ["r", "p", "s"]: break
    print("Please select the right option")


if p1 == p2:
    print("Draw")
elif p1 == "r" and p2 == "s":
    print("P1 wins")
elif p1 == "p" and p2 == "r":
    print("P1 wins")
elif p1 == "s" and p2 == "p":
    print("P1 wins")
else : print("P2 wins")