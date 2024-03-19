#Xochitl Martinez
#CS175L-01
#AverageFromInput

def main():
    infile = open('numbers.txt', 'r')
    total = 0
    i = 1

    for line in infile:

        num = float(line)
        total += num
        print(f'I read in {i} number(s) Current number is:  {num:.2f}', end='')
        print(f' Total is:  {total:.2f}')

        i+=1

    print(f'Average: {total / 3}')

if __name__ == '__main__':
    main()
