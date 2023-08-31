

mbr_set = {80462, 80438, 80314, 80292, 90069, 80373, 80403, 80420, 80284, 80306, 80519, 80322, 90034, 80365, 80489, 80349, 90085, 80411, 80357, 80454, 90018, 90042, 80390, 80497, 80381, 90026, 80446}


with open('Sifarnici/Sifarnik_opstina_u_Republici_Srbiji_lat.csv', 'r', newline='', encoding='utf-8') as file:
    for line in file:
        mbr, opstina, mbrokrug = line.strip().split(',')
        if mbr in mbr_set:
            print(opstina)