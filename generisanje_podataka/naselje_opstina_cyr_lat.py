import csv
import cyrtranslit


input_filename = 'Sifarnici/Sifarnik_naseljenih_mesta_Republike_Srbije_po_opstinama.csv'
output_filename = 'Sifarnici/Sifarnik_naseljenih_mesta_Republike_Srbije_po_opstinama_lat.csv'

header = ['Matični broj naseljenog mesta','Naziv naseljenog mesta','Matični broj opstine']


with open(input_filename, 'r', newline='\n', encoding='utf-8') as input_file, open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    writer.writerow(header)

    i = 0

    next(reader)
    
    for row in reader:
        mbr_opstina, _, mbr_naselje, naselje = row
        print(mbr_opstina, mbr_naselje, naselje)
        writer.writerow([mbr_naselje, cyrtranslit.to_latin(naselje), mbr_opstina])
        i += 1
        if i % 1000 == 0:
            print(i)
