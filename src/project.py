
with open('source/output.txt', "r", encoding= "utf-8") as file:
    
    lines = file.readlines()

    count = 0

    for i in lines:
        count += 1

    print("Sorok száma:",count)


with open('source/output.txt', "r", encoding= "utf-8") as file:
   
    text = file.read()
    records = text.count("\n001")

    print("Rekordok:", records)


