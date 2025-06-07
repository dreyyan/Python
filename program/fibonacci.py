print("Fibonacci Sequence")

n = int(input("# of Terms: "))
current_number = 1
next_number = 1
sum = 0
total_sum = 2
counter = 2

print(f'  {current_number}\n+ {next_number}')

while counter < n:
    sum = current_number + next_number
    total_sum += sum
    print(f'+ {sum}')
    current_number = next_number
    next_number = sum
    sum = 0
    counter += 1

print(f' = {total_sum}')