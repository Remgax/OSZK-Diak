# 1 ----------------------------------------------------------------

def counter():

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

        print("Raktári jelzet:", storage_label, "\n---------------------------------\n")

counter()
# 2 ----------------------------------------------------------------

with open('source/output.txt', "r", encoding= "utf-8") as file:
        text = file.read()

        records = 0
        
        for i in text.split('\n'):
            if i.startswith('001'):
                records += 1 

        print("Rekord azonosítók:", records, "\n---------------------------------\n")

# 3 ----------------------------------------------------------------



# 4 ----------------------------------------------------------------



# 5 ----------------------------------------------------------------

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

            
        print("\nIdőrendben:\n")
        for i in date_sorted:
            
            year = i[1:5]
            month = i[5:7]
            day = i[7:9]
            hour = i[9:11]
            minute = i[11:13]
            second = i[13:15]

            print(f"{year}. {month}. {day}. {hour}:{minute}:{second}")

date()

margin = 29*"-"