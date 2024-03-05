def sort_a(input):
    array_odd = []
    array_even = []
    array = list(input)
    
    for i in range(len(array)):
        if int(array[i]) % 2 == 0:
            array_even.append(array[i])
        else:
            array_odd.append(array[i])
    
    array_odd=sorted(array_odd, reverse=True)
    array_even=sorted(array_even)

    return ''.join(array_odd + array_even)

print(sort_a("417324689435"))