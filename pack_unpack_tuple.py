def pack_unpack_tuple(pstring, pbool, pnumber):
    new_tuple = (pstring, pbool, pnumber)
    pstring, pbool, pnumber = new_tuple
    print(pstring)
    print(pnumber)
    print(pbool)

str = "Apple"
isTrue = True
num = 21
pack_unpack_tuple(str, isTrue, num)