
with open('source/output.txt', "r", encoding= "utf-8") as file:
   
    text = file.read()

    records = []
    storage_label = []

    # Temporary variable
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



file_d = open("source/datalist.txt", "r",encoding = "utf-8")
print(file_d.read())