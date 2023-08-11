
# 1 ----------------------------------------------------------------
def a():
    with open('source/output.txt', "r", encoding= "utf-8") as file:
            text = file.read()

            record_heads = 0

            for i in text.split('\n'):
                if i.startswith('000'):
                    record_heads += 1
            
            print("Rekord fejek:", record_heads)

            location = 0

            for i in text.split("\n"):
                if i.startswith('850'):
                    location += 1

            
            print("Lelőhely:",location)

            storage_label = 0

            for i in text.split("\n"):
                if i.startswith('852'):
                    storage_label += 1

            print("Raktári jelzet:", storage_label)

    # 2 ----------------------------------------------------------------

def b():
    with open('source/output.txt', "r", encoding= "utf-8") as file:
            text = file.read()

            records = 0
            
            for i in text.split('\n'):
                if i.startswith('001'):
                    records += 1 

            print("Rekord azonosítók:", records)

    # 3 ----------------------------------------------------------------

def c():
    with open('source/output.txt', "r", encoding= "utf-8") as file:
            lines = file.readlines()

            labels = []

            for i in lines:
                if i.count("001") > 0 and i.count(" 001") == 0 and i.count(".001") == 0:
                    i = int(i.replace("001 ", ""))
                    labels.append(i)

            labels.sort()

            print("Azonosítók:")

            for i in labels:
                print(f"{i},")

# 4 ----------------------------------------------------------------

def d():
    with open('source/output.txt', "r", encoding= "utf-8") as file:
    
        text = file.read()

        records = []
        storage_label = []

        storage_label0 = []


        file_d = open("source/datalist.txt", "w")
        file_d.write("")

        for i in text.split('\n'):
            if i.startswith ('001'):
                i = int(i.replace('001', ''))
                records.append(i)
                file.close()


            elif i.startswith('852'):
                for e in i.split('\n'):
                    e = e.replace("852", "")
                    e = e.split('m')
                    for f in e:
                        f = f.split('  ')
                        if f[0] == "":
                            del f
                        try:
                            storage_label0.append(f[0])
                            #print("Jelzet: ",f[0])                     
                        except:
                            pass

            elif i.startswith('000'):
                storage_label0.append('###')


        group = []

        for a in storage_label0:
            if a == '###':
                
                group = []
            else:
                group.append(a)
            
            storage_label.append(group)

        count = 0

        for a in records:
            file_d = open("source/datalist.txt", "a", encoding = "utf-8")
            try:
                file_d.write(f"Azonosító: {records[count]}\nJelzet: {storage_label[count][0]}, {storage_label[count][-2]}\n\n")
                print(f"Azonosító: {records[count]}\nJelzet: {storage_label[count][0]}, {storage_label[count][-1]}, {storage_label[count][-2]}\n\n")
            except:
                file_d.write(f"Azonosító: {records[count]}\nJelzet: {storage_label[count][0]}\n\n")
                print(f"Azonosító: {records[count]}\nJelzet: {storage_label[count][0]}, {storage_label[count][-1]}\n\n")
            count += 1

# 5 ----------------------------------------------------------------

def e():
        with open('source/output.txt', "r", encoding= "utf-8") as file:

            text = file.read()

            date_sorted = []

            for i in text.split('\n'):
                if i.startswith('005'):
                    i = i.replace('005', '').replace('.0', '')
                    date_sorted.append(i)
                    date_sorted.sort()

                    year = i[1:5]
                    month = i[5:7]
                    day = i[7:9]
                    hour = i[9:11]
                    minute = i[11:13]
                    second = i[13:15]

                
            print("Időrendben:\n")
            for i in date_sorted:
                
                year = i[1:5]
                month = i[5:7]
                day = i[7:9]
                hour = i[9:11]
                minute = i[11:13]
                second = i[13:15]

                print(f"{year}. {month}. {day}. {hour}:{minute}:{second}")




y = int(input("Adjon meg egy számot 1-6-ig:\n\n"))


def function():


    x = int(input("Adjon meg egy számot 1-6-ig:\n\n"))


    if x == 1:
        a()
    elif x == 2:
        b()
    elif x == 3:
        c()
    elif x == 4:
        d()
    elif x == 5:
        e()
    elif x == 6:
        print("Kilépés")
    else:
        function()

if y == 1:
    a()
elif y == 2:
    b()
elif y == 3:
    c()
elif y == 4:
    d()
elif y == 5:
    e()
elif y == 6:
    print("Kilépés")
else:
    function()