import time

start_time = time.time()

def counter():

    with open('source/output.txt', "r", encoding= "utf-8") as file:
    
        text = file.read()

        records = 0
        
        for i in text.split('\n'):
            if i.startswith('001'):
                records += 1 

        print("Rekord azonosítók:", records)

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

def label():
    with open('source/output.txt', "r", encoding= "utf-8") as file:
        lines = file.readlines()

        labels = []

        for i in lines:
            if i.count("001") > 0 and i.count(" 001") == 0 and i.count(".001") == 0:
                i = int(i.replace("001 ", ""))
                labels.append(i)

        labels.sort()

        print("\nAzonosítók:")

        for i in labels:
            print(f"{i},")


    
def date():
    with open('source/output.txt', "r", encoding= "utf-8") as file:

        text = file.read()

        for i in text.split('\n'):
            if i.startswith('005'):
                i = i.replace('005', '').replace('.0', '')
                year = i[0:4]
                month = i[4:6]
                day = i[6:8]
                hour = i[8:10]
                minute = i[10:12]
                second = i[12:14]




                print(f"Dátum: {i}")

date()

print(f" {(time.time() - start_time)} seconds")



