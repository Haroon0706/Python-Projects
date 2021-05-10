#Building a simple weight converter from Kgs to Lbs and vice versa using if statements

#Write code as a function as a means of allowing someone to run the program multiple times

def main():
    weight = float(input ("Weight: "))
    print(weight)

    print("Enter unit as either K or L")
    unit = input ("(K)gs or (L)bs: ")


    if unit.upper() == "K":
        converted = weight / 0.45
        print ("Weight in Lbs: " + str(converted))

    else:
        converted = weight * 0.45
        print ("Weight in Kgs: " + str(converted))

while True:
    main()
    if input("Convert again? (Y/N)").strip().upper() != "Y":
        break