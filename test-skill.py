# -------------------- NARCISSISTIC NUMBER
def narcissistic(nomor):
    panjang = len(str(nomor))
    jumlah = 0
    for x in str(nomor):
        jumlah += pow(int(x), panjang)
    if jumlah == nomor:
        return True
    return False

print (narcissistic(153))
print (narcissistic(111))

# -------------------- PARITY OUTLIER
def parity_outliter(integers):
    x = []
    y = []
    for i in integers:
        if i % 2 > 0:
            y.append(i)
        if i % 2 == 0:
            x.append(i)
    if len(x) > len(y):
        if y:
            return (str(y[0]) + ' (the only odd number)')
        else:
            return False
        # return y[0]
    else:
        if x:
            return (str(x[0]) + ' (the only even number)')
        else:
            return False
        # return x[0:]

print ( parity_outliter( [2, 4, 0, 100, 4, 11, 2602, 36] ) )
print ( parity_outliter( [160, 3, 1719, 19, 11, 13, -21] ) )
print ( parity_outliter( [11, 13, 15, 19, 9, 13, -21] ) )

# -------------------- NEEDLE IN THE HAYSTACK
def findNeedle(haystack , needle):
    count = 0
    if needle in haystack:
        index = haystack.index(needle)
        string1 = haystack[index:len(needle) + index]
        for position in range(0,len(haystack)):
            if haystack[position:len(needle) + position] == string1:
                count += 1
    return count
# findNeedle([“red”, “blue”, “yellow”, “black”, “grey”], “blue”)
print (findNeedle(['red', 'blue', 'yellow', 'black', 'grey'], 'blue'))

# -------------------- THE BLUE OCEAN REVERSE
def blueOcean(list_order, hapus):
    n = len(list_order)
    for i in range(n - 1, -1, -1):
        if list_order[i] in hapus:
            del list_order[i]
    return list_order

print (blueOcean( [1,2,3,4,6,10], [1]))
print (blueOcean([1,5,5,5,5,3], [5]))

blueOcean([1,2,3,4,6,10], [1])
blueOcean([1,5,5,5,5,3], [5])
