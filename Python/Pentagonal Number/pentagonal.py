def pentagonal(n):
    print(int((3 * n * n - n) / 2))

if __name__ == '__main__':
    while True:
        try:
            pentagonal(int(input('How many layers do you want to calculate?: ')))
            break
        except ValueError:
            print('Value Error, Try again')

