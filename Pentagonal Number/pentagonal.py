 # * This is Function to calculate how many dots are around center of pentagon 1 dot.
result = 0
done = True
def pentagonal(n):
    global result

    for i in range(n-1):
        result += (i+1)*5
    result += 1
    return result

if __name__ == '__main__':
    while done:
        try:
            n = int(input('How many layers do you want to calculate?: '))
            done = False
        except ValueError:
            print('Value Error, Try again')
    print(pentagonal(n))
