def adddigits(num):
    while len(str(num)) > 1:
        num = sum(int(x) for x in str(num))
    return num
print(adddigits(56))