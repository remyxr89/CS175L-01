#Xochitl Martinez
#CS175L
#expensePieChart

import sys
import matplotlib.pyplot as plt

def main():
    try:
        infile = open('expenses.txt', 'r')

    except IOError:
        sys.exit('SystemExit: File not found: expenses.txt - exiting')

    labels_list = []
    cost_list = []

    for row in infile:
        row = row.strip('\n')
        label, value = row.split('\t')

        try:
            cost = int(value)
            labels_list.append(label)
            cost_list.append(value)

        except ValueError:
            print('Error', '\"', row.strip(), '\"', 'skipping')
    
    plt.pie(cost_list, labels = labels_list)
    plt.pie(cost_list, colors = ('b', 'c', 'm', 'y', 'r', 'g'))
    plt.title('Monthly Expenses')
    plt.show()

if __name__ == '__main__':
    main()
