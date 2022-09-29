# 4a)

def rotate_left_str(s: str, n: int) -> str:
    return s[n:] + s[:n]


for i in range(10):
    print(rotate_left_str("Hello World", i))

# 4b)

def move2_str(s: str) -> str:
    return s[1::2] + s[::2]


print(move2_str('abcdefgh'))