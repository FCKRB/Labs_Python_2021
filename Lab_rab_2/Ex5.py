str_str = ""
with open("input_ex5.txt", "r") as file:
    str_str += file.read()
file.close()
s1 = "".join(c for c in str_str if c.isalpha())
s1 = s1.lower()
s1 = sorted(s1)
s_output = []
for c in s1:
    if 'a' <= c <= 'z':
        k = s1.count(c)
        s_output.append([c, k])
        while c in s1:
            s1.remove(c)

s_output = sorted(s_output, key=lambda i: i[1])
with open("output_ex5.txt", "w") as file:
    for i in s_output:
        file.write("%s\n" % str(i))
file.close()
print(s_output)