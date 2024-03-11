#Xochitl Martinez
#CS175L
#TemperatureConversions

def main():
    controlLoop()

def convertToKelvin(Fahrenheit):
    Kelvin = (Fahrenheit - 32) * 5 / 9 + 273.15
    return Kelvin

def convertToCentigrade(Fahrenheit):
    Centigrade = (Fahrenheit - 32) * 5 / 9
    return Centigrade

def doConversion(Fahrenheit):
    Kelvin = convertToKelvin(Fahrenheit)
    Centigrade = convertToCentigrade(Fahrenheit)
    print(f'\nFahrenheit: {Fahrenheit:.2f}')
    print(f'\nKelvin: {Kelvin:.2f}')
    print(f'\nCentrigrade: {Centigrade:.2f}\n')

def repeat():
    submit = int(input('How many conversion would you like to do this time?: '))
    for x in range (submit):
        Fahrenheit = getFahrenheit()
        doConversion(Fahrenheit)

def controlLoop():
    while True:
        question = input('Do you want to do some conversions (Yes or No)?: ')
        if question == 'YES' or question == 'Yes' or question == 'yes':
            repeat()
        else:
            break

def getFahrenheit():
    while True:
        Fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130): '))
        if -50 <= Fahrenheit <= 130:
            return Fahrenheit
        else:
            print('Please re-enter: ')

if __name__ == '__main__':
    main()
