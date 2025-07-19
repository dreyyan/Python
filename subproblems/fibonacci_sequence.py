def fibonacci_sequence(n: int) -> None:
    x,y=1,1
    if n == 1:
        print(x, end='')
        return
    elif n == 2:
        print(f'{x}, {y}', end='')
        return

    print(f"{x}, {y}", end='') 

    for i in range(3, n+1):
        sum=x+y
        print(f", {sum}", end='')

        x=y
        y=sum

fibonacci_sequence(7)