def rotate_left_str(s: str, n: int) -> str:
    return s[n:] + s[:n]


for i in range(10):
    print(rotate_left_str("Hello World", i))
