def counter():

    with open('source/output.txt', "r", encoding= "utf-8") as file:
    
        text = file.read()

        records = text.count("\n001")

        print("Rekord azonosítók:", records)

        record_heads = text.count("\n000")
        
        print("Rekord fejek:", record_heads)

        location = text.count("\n850")
        
        print("Lelőhely:",location)

        storage_label = text.count("852")

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
        print("Jelzetek:", labels)

counter()

label()







