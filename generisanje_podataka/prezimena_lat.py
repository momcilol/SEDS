import csv
import cyrtranslit


file_prezimena = 'Sifarnici/prezimena_ic.csv'
file_prela = 'Sifarnici/prezimena_ic_lat.csv'

with open(file_prezimena, 'r', newline='\n', encoding='utf-8') as input_file, open(file_prela, 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    writer.writerow(['Prezime'])

    i = 0

    next(reader)
    
    for row in reader:
        writer.writerow([cyrtranslit.to_latin(row[0])])
        i += 1
        if i % 1000 == 0:
            print(i)