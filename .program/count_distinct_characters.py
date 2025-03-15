def count_distinct_characters(string):
    distinct_set = set()
    for i in string:
        distinct_set.add(i)

    count = len(distinct_set)
    print(f'Unique Letter Count: {count}')

test_string = "onomatopoeia"
count_distinct_characters(test_string)