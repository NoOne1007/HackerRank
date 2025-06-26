def swap_case(s):
    # return s.swapcase()
    L = []
    for i in s:
        if i.isalpha():
            if i.islower():
                L.append(i.upper())
            else:
                L.append(i.lower())
        else:
            L.append(i)

    swaped_str =  ''.join(L)
    
    return swaped_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)