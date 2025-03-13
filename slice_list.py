def slice_list(start, end):
    org_list = []
    first_list = []
    second_list = []

    for i in range(start, end):
        org_list.append(i + 1)

    end_index = len(org_list) // 2

    for i in org_list[0:end_index]:
        first_list.append(i)

    for j in org_list[end_index:]:
        second_list.append(j)

    print(f'Original List: {org_list}')
    print(f'First List: {first_list}')
    print(f'Second List: {second_list}')
    
slice_list(0, 10)