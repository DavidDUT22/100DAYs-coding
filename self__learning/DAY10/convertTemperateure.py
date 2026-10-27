while True: 
    print("=== Celsius to Fahrenheit converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    choice = input("Please Enter your choice (1/2): ")

    if choice == "1": 
       celsuis = float(input("Enter Temperature in celsuis: "))
       fahrinheit = (celsuis * 9 / 5) + 32
       print(f"{celsuis}°C to fahrinheit : {fahrinheit}°F ")
    elif choice == "2":
        fahrinheit = float(input("Enter Temperature in fahrinheit: "))
        celsuis = (fahrinheit - 32) * 5 / 9
        print(f"{fahrinheit}°F to fahrinheit : {celsuis}°C ")
    elif choice == "3":
        print("Goodbye!")
        break
    else :
        print("Your choice is invalid")
    
