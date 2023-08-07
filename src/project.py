import time

start_time = time.time()


def record():
    with open('source/output.txt', "r", encoding= "utf-8") as file:
    
        text = file.read()

        records = 0
        
        for i in text.split("\n"):
            if i.startswith('001'):
                records += 1

        print(f"\nRekordok száma: {records}")


def record_counter():
    with open('source/output.txt', "r", encoding= "utf-8") as file:
        lines = file.readlines()

        label = []

        for i in lines:
            if i.count("001 ") > 0 and i.count(" 001") == 0 and i.count(".001") == 0:
                i = int(i.replace("001 ", ""))
                label.append(i)

        label.sort()

    print(f"\nAzonosítók:")
    for i in label:
        print(f"{i},")


record()

record_counter()


print(f"\n[ {(time.time() - start_time)} seconds ]\n")




