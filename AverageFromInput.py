#Xochitl Martinez
#CS175L-01
#AverageFromInput

import sys

def main():
    total = 0.0
    i = 1

    try:
        infile = open('numbers.txt', 'r')

        for line in infile:

            num = float(line)
            total += num
            print(f'I read in {i} number(s) Current number is:  {num:.2f}', end='')
            print(f' Total is:  {total:.2f}')

            i+=1

        print(f'Average: {total / 3}')
        
    except IOError:
        sys.exit('SystemExit: File not found: numbers.txt - exiting')

    except ValueError:
        print('Bad data:',line.strip(),'skipping')

        for line in infile:

            num = float(line)
            total += num
            print(f'I read in {i} number(s) Current number is:  {num:.2f}', end='')
            print(f' Total is:  {total:.2f}')

            i+=1

        print(f'Average: {total / 3}')

if __name__ == '__main__':
    main()
