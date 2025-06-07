def listGenerateCartestianProduct(lst1, lst2) -> None:
    cartesianProduct = []
    sublist = []

    for i in lst1:
        for j in lst2:
            sublist.append((i, j))

    cartesianProduct.append(sublist)
    print(cartesianProduct)

listGenerateCartestianProduct([1, 2], ['x', 'y'])
