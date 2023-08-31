import csv

input_filename = 'Sifarnici/kucni_broj-sifarnik.csv'
output_filename = 'Sifarnici/adrese.csv'

columns_to_keep = ['kucni_broj_lat', 'ulica_ime_lat', 'naselje_maticni_broj']
columns_to_write = ['adresa', 'naselje_maticni_broj']

with open(input_filename, 'r', newline='', encoding='utf-8') as input_file, open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=columns_to_write)
    
    writer.writeheader()

    i = 0
    
    for row in reader:
        selected_data = {column: row[column] for column in columns_to_keep}
        output_data = {columns_to_write[0]: f"{selected_data[columns_to_keep[1]]} {selected_data[columns_to_keep[0]]}", columns_to_write[1]: selected_data[columns_to_keep[2]]}
        writer.writerow(output_data)
        i += 1
        if i % 1000 == 0:
            print(i)

