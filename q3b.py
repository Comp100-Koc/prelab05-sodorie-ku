def add_binary(a, b):
    if a.startswith("0b"):
        a = a[2:]
    
    if b.startswith("0b"):
        b = b[2:]
    
    a = a[::-1]
    b = b[::-1]

    calc_a = 0
    for i in range(len(a)):
        calc_a += (2**i) * int(a[i])

    calc_b = 0
    for i in range(len(b)):
        calc_b += (2**i) * int(b[i])

    int_sum = calc_a + calc_b
    if int_sum == 0:
        return "0b0"
    
    base_number = ""
    while int_sum > 0:
        base_number = str(int_sum % 2) + base_number
        int_sum = int_sum // 2

    return "0b"+base_number
