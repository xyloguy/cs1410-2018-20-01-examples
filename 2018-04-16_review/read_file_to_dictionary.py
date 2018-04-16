import student

def read_file_to_dictionary(filename):
    f = open(filename, 'r')
    d = {}
    for line in f:
        parts = line.split()

        first = parts[1]
        last = parts[0]
        ssn = parts[2]
        email = parts[3]
        age = parts[4]

        s = student.Student(first, last, ssn, email, age)
        if ssn in d:
            print('Duplicate:', str(s), '->', str(d[ssn]))
            continue

        d[ssn] = s
    f.close()
    return d
