with open('write_shit.txt', 'w') as file:
    with open('counties.txt', 'r') as counties:
        for i in range(50):
            county = counties.readline()
            datas = county.split(' ')
            file.writelines("<option value=\"https://www.google.com/maps?q=" + datas[1] + datas[2] + "\">" + datas[0][:-1] + "</option>\n")