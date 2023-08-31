import random
from datetime import datetime, timedelta
    
center_year = 1990
standard_deviation = 10
start_date = datetime(1925, 1, 1)
end_date = datetime(2006, 12, 31)
time_difference = end_date - start_date

def generate_jmbg(date_of_birth, gender):
    year = date_of_birth.year % 1000 
    month = date_of_birth.month
    day = date_of_birth.day

    gender_num = random.randint(0,499);
    if gender == 'F':
        gender_num += 500

    region = random.randint(0,99)

    jmbg = f"{day:02d}{month:02d}{year:03d}{region:02d}{gender_num:03d}{random.randint(0, 9)}"
    return jmbg


def generate_random_date():

    offset_years = int(random.gauss(0, standard_deviation))
    target_year = center_year + offset_years
    
    random_days = random.randint(0, time_difference.days)
    generated_date = start_date + timedelta(days=random_days)

    if generated_date.month == 2 and generated_date.day == 29:
        return generated_date
    
    generated_date.replace(year=target_year)
    return generated_date

num_dates = 1000
with open('Sifarnici/datumi_rodjenja.txt', 'w', newline='', encoding='utf-8') as output_file:
    for _ in range(num_dates):
        random_date = generate_random_date()
        output_file.write(f'{random_date.strftime("%Y-%m-%d")}\n')
