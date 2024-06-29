#brother address  officer

with open('C:\\Users\\dimon\\Documents\\GitHub\\testapp\Python_lesson\\file.txt', 'r') as f:
    for line in f:
        #print(line)



        #if 'brother' in line:
           # print(line)
        #elif 'address' in line:
            #print(line)
       # elif 'officer' in line:
       #     'officer' in line
       
        if 'brother' in line or 'address' in line or 'officer' in line:
            print(line)