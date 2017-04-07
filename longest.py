def long_ans(element):
    length = []
    for i in range(3,len(element)):
        length.append(element[1])
    m = length.index(max(length))
    m=m+3
    if element[0] == element[m]:
        return 1
    else:
        return 0