from read_file_to_dictionary import read_file_to_dictionary


filename = "InsertNames.txt"
d = read_file_to_dictionary(filename)
print(len(d))

total = 0
for key in d:
    student = d[key]
    total += student.age
print(total/len(d))

sorted_keys = sorted(d.keys())
for key in sorted_keys:
    print(d[key])
