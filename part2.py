def get_positive_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num > 0:
                return num
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def calculate_species_data(starting_count, avg_daily_increase, num_days):
    current_count = starting_count
    for day in range(1, num_days + 1):
        print(f"Day {day:02}: {current_count:.2f}")
        current_count *= 1 + avg_daily_increase / 100

starting_count = get_positive_number("Enter the starting number of organisms/species: ")
avg_daily_increase = get_positive_number("Enter the average daily percentage increase: ")
num_days = int(get_positive_number("Enter the number of days' worth of data to print: "))

calculate_species_data(starting_count, avg_daily_increase, num_days)