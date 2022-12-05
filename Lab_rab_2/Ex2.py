import os

min1 = 2100
minName = ""
max1 = 1900
maxName = ""
if os.path.exists("Students.txt"):
    print("Указанный файл существует")

    with open("Students.txt", encoding="utf8") as file:
        strings = file.readlines()
        for s in strings:
            s = s.split(";")
            year = int(s[2].split()[0])
            if year > max1:
                max1 = year
                maxName = s[0] + " " + s[1]
            if year < min1:
                min1 = year
                minName = s[0] + " " + s[1]
    with open("Students_2.txt", "w") as file:
        file.write(minName + " " + str(min1))
        file.write("\n")
        file.write(maxName + " " + str(max1))
else:
    print("Файл не существует")
