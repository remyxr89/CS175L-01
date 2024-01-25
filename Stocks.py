#Xochitl Martinez
#CS175L-01
#Stocks Assignment

stock_purchase = float(input('Enter commission rate percentage ' +
                             'on stock purchase: '))
stock_sale = float(input('Enter commission rate percentage ' +
                         'on stock sale: '))
shares_purchased = float(input('Enter number of shares purchase: '))
shares_sold = float(input('Enter number of shares sold: '))
purchase_sale = float(input('Enter purchase price per share: '))
sell_share = float(input('Enter sell price per share: '))
print()

amountPaidForStock = shares_purchased * purchase_sale
purchaseCommission = stock_purchase * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = shares_purchased * sell_share
sellingCommission = stock_purchase * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print('Amount paid for stock: $', end= '')
print(f'{amountPaidForStock:,.2f}')
print('Commission paid on the purchase: $', end= '')
print(f'{purchaseCommission:,.2f}')
print('Amount the stock sold for $', end= '')
print(f'{stockSoldFor:,.2f}')
print('Commission paid on the sale: $', end= '')
print(f'{sellingCommission:,.2f}')
print('Profit (or loss if negative): $', end= '')
print(f'{profitOrLoss:,.2f}')
