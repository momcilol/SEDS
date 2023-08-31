import random
from datetime import datetime, timedelta
import csv
import math

domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'yandex.ru', 'mail.ru', 'yandex.ru']    

current_year = 2023

address_count = 2_436_790
address_order_number = set()
addresses = []

set_of_usernames = set()
male_names = []
female_names = []
last_names = []

low = 10000
  
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


def createUsername(first,last):

    username = first + last

    if len(username) > 15 or username in set_of_usernames: 
        username = first+last[:15-len(first)-4]+str(random.randint(0,low-1)) 
        username = username.lower()

    while True:
        if username not in set_of_usernames:
            set_of_usernames.add(username)
            return username

        username = first+last[:15-len(first)-4]+str(random.randint(0,low-1)) 
    


def read_names(file_name, array):
    with open(file_name,'r', encoding='utf-8') as file:
        for line in file:
            array.append(line.strip())


def address_read_randoms(high, count):
    while len(address_order_number) < count:
        address_order_number.add(random.randint(1,high))
    
    with open('Sifarnici/adrese.csv','r',encoding='utf-8') as file:
        reader = csv.reader(file)
        i = 0
        next(reader)
        for row in reader:
            i += 1
            if i in address_order_number:
                addresses.append(row)
        
def sigmoid(x):
    return 1 / (1 + pow(math.e, -(x-60)/10))

          
file_males = 'Sifarnici/muska_imena.txt'
file_females = 'Sifarnici/zenska_imena.txt'
file_last_names = 'Sifarnici/prezimena_ic_lat.txt'

read_names(file_males, male_names)
read_names(file_females, female_names)
read_names(file_last_names, last_names)

address_read_randoms(address_count, 1000)

file_in = 'Sifarnici/CustomerStupid.csv'
file_out = 'Sifarnici/CustomerSmart.csv'

with open(file_in, 'r', newline='\n', encoding='utf-8') as input_file, open(file_out, 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()

    i = 0
    
    for row in reader:
        gender = row[fieldnames[5]]
        name, last_name = '', last_names[random.randint(0,len(last_names)-1)]

        if gender == 'M':
            name = male_names[random.randint(0,len(male_names)-1)]
        else:
            name = female_names[random.randint(0,len(female_names)-1)]

        username = createUsername(name, last_name)
        birth_date = generate_random_date()
        email = ''
        if random.random() > sigmoid(current_year - birth_date.year):
            email = username + '@' + domains[random.randint(0, len(domains)-1)]

        jmbg = generate_jmbg(birth_date, gender)

        phone = f'+381 6{random.randint(0,9)} {row[fieldnames[8]].strip()[6:].replace("-"," ")}'
        
        address, settlement = addresses[i]
        
        output_data = {
            fieldnames[0]:row[fieldnames[0]],
            fieldnames[1]:username,
            fieldnames[2]:jmbg,
            fieldnames[3]:name,
            fieldnames[4]:last_name,
            fieldnames[5]:gender,
            fieldnames[6]:birth_date.strftime("%Y-%m-%d"),
            fieldnames[7]:address,
            fieldnames[8]:phone,
            fieldnames[9]:email,
            fieldnames[10]:settlement
        }
        writer.writerow(output_data)
        i += 1
        if i % 100 == 99:
            print(i)
