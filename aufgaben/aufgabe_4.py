def rotate_string(string, n):
    return string[n:] + string[:n]


for i in range(10):
    print(rotate_string("Hello World", i))
