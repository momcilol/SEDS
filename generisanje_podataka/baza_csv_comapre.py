
first_file = 'Sifarnici/naselja_baza.csv'
second_file = 'Sifarnici/Sifarnik_naseljenih_mesta_Republike_Srbije_po_opstinama_lat.csv'

with open(first_file, 'r', newline='', encoding='utf-8') as file:
    first_data = {line.strip().split(',')[0]: line.strip() for line in file}

with open(second_file, 'r', newline='', encoding='utf-8') as file:
    i = 0
    opstine = set()
    for line in file:
        data = line.strip().split(',')
        idnaselje = data[0]
        if idnaselje not in first_data:
            opstine.add(data[2])
            print(f"Data in second file but not in first: {line.strip()}")
            i += 1

    print(i)
    print("Opstine: ", opstine)
