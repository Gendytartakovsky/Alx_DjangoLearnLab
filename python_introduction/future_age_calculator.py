while True:
    age_input = input("How old are you? ").strip()
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter your age as a whole number (e.g., 25).")

age_in_2050 = age + 27
print(f"In the year 2050, you will be {age_in_2050} years old.")
