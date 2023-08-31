import csv
import random


address_count = 2_436_790
address_order_number = set()
addresses = []


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


address_read_randoms(address_count, 170)
        


with open('Sifarnici/ekspozitura.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)

    writer.writerow(['IDEKSPOZITURA','NAZIV','ADRESA','NASELJE_IDNASELJE'])

    
    for i in range(170):
        writer.writerow([i,f'PC {addresses[i][0]}',addresses[i][0],addresses[i][1]])
        i += 1
        if i % 25 == 0:
            print(i)
