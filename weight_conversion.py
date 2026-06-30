while True:
    try:
        weight=float(input("Enter the weight: "))
        if weight<=0:
            print("Weight must be greater than zero!")
            continue
    except ValueError:
        print("Invalid weight!")
        continue
    unit=input("Kilograms or Pounds(K/L): ").lower().strip()
    if unit=='k':
        weight=weight*2.205
        unit="lbs"
        print(f"Your weight is: {round(weight,1)} {unit}.")
        
    elif unit=='l':
        weight=weight/2.205
        unit="kg"
        print(f"Your weight is: {round(weight,1)} {unit}.")
        
    else:
        print("Invalid unit!")
        continue

    while True:
        ch=input("Do you want to continue? (y/n): ").lower().strip()
        if ch=='n':
            print("Exit!")
            exit()
        elif ch=='y':
            break
        else:
            print("Enter y or n!")
            continue

