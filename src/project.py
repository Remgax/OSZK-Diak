# 1 ----------------------------------------------------------------
with open('source/output.txt', "r", encoding= "utf-8") as file:
  
    text = file.read()
    records = text.count("\n001")

    print("Rekordok száma:", records)

# 2 ----------------------------------------------------------------

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

label()

# 3 ----------------------------------------------------------------

import time

start_time = time.time()

def label():
    with open('source/output.txt', "r", encoding= "utf-8") as file:
        lines = file.readlines()

        labels = []

        for i in lines:
            if i.count("001") > 0 and i.count(" 001") == 0 and i.count(".001") == 0:
                i = int(i.replace("001 ", ""))
                labels.append(i)

        labels.sort()

label()

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