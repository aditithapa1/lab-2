#step one ask the user to enter the number of years
num_years = int(input("Enter the number of years:"))
#step two initialize variables for tpotal rainfall and average monthly rainfall
total_rainfall_per_year = []
avg_monthly_rainfall_per_year = []
#step 3 loop for each year and get the rainfall amount for each month
for year in range(1, num_years +1):
    print(f"For year {year}:")
    yearly_rainfall = 0
    monthly_rainfall = []
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall in centimeters for month {month}: "))
        yearly_rainfall += rainfall
        monthly_rainfall.append(rainfall)
    total_rainfall_per_year.append(yearly_rainfall)
    avg_monthly_rainfall_per_year.append(yearly_rainfall / 12)
    print()
    # Step 4: Display the total and average rainfall for each year
for year in range(num_years):
    print(f"Year {year+1}: Total rainfall = {total_rainfall_per_year[year]} cm, Average monthly rainfall = {avg_monthly_rainfall_per_year[year]} cm")  
    
