country = []
country_code = []
year = []
life_expectancy = []

min_year = 99999
min_country = ''
max_country = ''
min_exp = 99999
max_exp = 0
yearmax_expectancy = -1
yearmax_country = ''
yearmin_expectancy = 99999
yearmin_country = ''

year_interest_expectancy_sum = 0
year_interest_count = 0

year_interest = int(input('Enter the year of interest: '))
print()

with open('life-expectancy.csv') as life_expectanc:
    # Skipping the header (First line of the CSV)
    next(life_expectanc)
    for line in life_expectanc:
        line = line.strip()
        parts = line.split(",")
        country = parts[0]
        country_code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        if life_expectancy > max_exp:
            max_exp = life_expectancy
            max_country = country

        elif life_expectancy < min_exp:
            min_exp = life_expectancy
            min_country = country
            min_year = year

        if year == year_interest:
            # How many times it enters if condition
            year_interest_count += 1  # 1 is a contador
            # Adding the expectancy for this line
            year_interest_expectancy_sum += life_expectancy

            if life_expectancy > yearmax_expectancy:
                yearmax_expectancy = life_expectancy
                yearmax_country = country

            elif life_expectancy < yearmin_expectancy:
                yearmin_expectancy = life_expectancy
                yearmin_country = country

    average = year_interest_expectancy_sum / year_interest_count

    print(
        f'The overall max life expectancy is: {max_exp} from {max_country} in {year}')
    print(
        f'The overall min life expectancy is: {min_exp} from {min_country} in {min_year}')
    print()

    print(f'For the year {year_interest}:')
    print(
        f'The average life expectancy across all countries was {average:.2f}')
    print(
        f'The max life expectancy was in {yearmax_country} with {yearmax_expectancy}')
    print(
        f'The min life expectancy was in {yearmin_country} with {yearmin_expectancy}')
    print()


country = []
life_expectancy = []

max_country_interest = -1
min_country_interest = 99999
country_interest_expectancy_sum = 0
country_interest_count = 0


country_interest = str(input('Enter the country of interest: '))
print()

with open('life-expectancy.csv') as life_expectanc:
    next(life_expectanc)
    for line in life_expectanc:
        line = line.strip()
        parts = line.split(",")
        country = parts[0]
        country_code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        if country == country_interest:
            country_interest_count += 1
            country_interest_expectancy_sum += life_expectancy

            if life_expectancy > max_country_interest:
                max_country_interest = life_expectancy

            elif life_expectancy < min_country_interest:
                min_country_interest = life_expectancy

country_average = country_interest_expectancy_sum / country_interest_count

print(f'For {country_interest}:')
print(f'The average life expectancy was {country_average:.2f}')
print(
    f'The max life expectancy was {max_country_interest}')
print(
    f'The min life expectancy was {min_country_interest}')
