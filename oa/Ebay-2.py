def reduceTheNumber(number, k):
    while len(number) > k:
        next = ""
        for i in range(len(number) // k + 1):
            group = 0
            for q in range(i*k, min(i*k+k, len(number))):
                group += int(number[q])
            next += str(group)
        number = next
    return number

print(reduceTheNumber("1111122222", 9))