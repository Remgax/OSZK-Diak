import time

start_time = time.time()


def datas(source):
    source = str(source)
    try:
        file =  open(source, "r", encoding= "utf-8")
    
    except Exception as e:
        file =  open("source/output.txt", "r", encoding= "utf-8")
        if source != "":
            print(f"Hiba: {e}")
            del file

        print("\nForrás: Alapértelmezet forrás")
        

    
    
    
        

    try:
    
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

    except Exception as e:
        if FileExistsError == False:
            print(f"Hiba: {e}")



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

                print(f"{year}. {month}. {day}. {hour}:{minute}:{second}")
            
        print("\nIdőrendben:\n")
        for i in date_sorted:
            
            year = i[1:5]
            month = i[5:7]
            day = i[7:9]
            hour = i[9:11]
            minute = i[11:13]
            second = i[13:15]

      
            print(f"{year}. {month}. {day}. {hour}:{minute}:{second}")



def source_in():
    source = input("\nForrás:\n")
    datas(source)



source_in()








margin = 29*"-"
print(f"\n{margin}\n{(time.time() - start_time)} seconds\n{margin}\n")
