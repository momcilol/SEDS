import csv
import random
from datetime import datetime, timedelta

valuta_mean = [30_000, 100_000, 1_500_000, 3000]
standard_deviation = [15_000, 100_000, 2_000_000, 5000]

start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 8, 31)
time_difference = end_date - start_date

def random_date():
    random_days = random.randint(0, time_difference.days)
    return start_date + timedelta(days=random_days)

def random_stanje(x):
        result = 0
        if x == 1:
            result = random.gauss(valuta_mean[0], standard_deviation[0])
            while result < 0:
                result = random.gauss(valuta_mean[0], standard_deviation[0])
        elif x == 2 or x == 3:
            result = random.gauss(valuta_mean[x-1], standard_deviation[x-1])
            while result < -100_000:
                result = random.gauss(valuta_mean[x-1], standard_deviation[x-1])
        elif x >= 4:
            result = random.gauss(valuta_mean[3], standard_deviation[3])
            while result < -500:
                result = random.gauss(valuta_mean[3], standard_deviation[3])
        
        return result
         


fieldnames = ['IDRACUN','BROJRAC','STANJE','DATOTVARANJA','KORISNIK_IDKORISNIK','TIPRACUNA_IDTIPRAC']

in_filename = 'Sifarnici/CustomerSmart.csv'
out_filename = 'Sifarnici/accounts.csv'

with open(in_filename, 'r', newline='',encoding='utf-8') as input_file, open(out_filename, 'w', newline='',encoding='utf-8') as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.writer(output_file)

    writer.writerow(fieldnames)

    i = 0
    for row in reader:
        num_account = random.randint(0,5)
        for _ in range(num_account):
            tip_rac = 1
            year = int(row['datRodj'][:4])
            if year < 2003 and year > 1996:
                tip_rac = random.randint(1,9)
            elif year < 1996:
                tip_rac = random.randint(2,9)

            i += 1
            out_data = [i,random.randint(1_000_000_000_000,1_000_000_000_000_000_000), f'{random_stanje(tip_rac):.4f}', random_date().strftime("%Y-%m-%d"), row['idKorisnik'], tip_rac]
            writer.writerow(out_data)

