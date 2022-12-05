import os
PR = 1

if not os.path.exists("input.txt"):
    print("Файл не существует")
    exit(1)

print("Указанный файл существует")

with open("input.txt", "r") as file_obj:
    nums = file_obj.readline().split()
    for i in range(len(nums)):
        nums[i] = int(nums[i])

print(nums)

for num in nums:
    PR *= num

with open("output.txt", "w") as somefile:
    somefile.write(str(PR))

with open("output.txt", "r") as somefile:
    result = somefile.readline()

print("Result = ", result)


