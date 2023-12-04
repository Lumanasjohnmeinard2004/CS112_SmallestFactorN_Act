def find_smallest_factor(n):
    # Check if n is less than 2
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    # Find the smallest factor other than 1 using a for loop
    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            break

# Main program
while True:
    # Get user input
    user_input = int(input("Enter an integer >=2: "))
    find_smallest_factor(user_input)

    # Ask the user if they want to continue or not.
    user_choice = input("Do you want to continue? (yes/no): ").lower()
    if user_choice != 'yes':
        break
