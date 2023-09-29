# Initialize variables
total = 0
count = 0

# Ask the user for input
while True:
    try:
        num = float(input("Enter a number (or '0' to calculate the average): "))
        if num == 0:
            break  # Exit the loop if the user enters 0
        total += num
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if the user entered any numbers
if count == 0:
    print("No numbers entered.")
else:
    # Calculate and display the average
    average = total / count
    print(f"The average of the {count} numbers is: {average:.2f}")
