#Xochitl Martinez
#CS175L-01
#restaurant

yes = 'yes'
while yes == 'yes':

    vegetarian = False
    vegan = False
    gluten_free = False

    vegetarian_response = input("Is anyone in your party vegetarian?: ")
    vegan_response = input("Is anyone in your party vegan?: ")
    gluten_free_response = input("Is anyone in your party gluten-free?: ")
    print('')

    if vegetarian_response == "yes":
        vegetarian = True
    if vegan_response == "yes":
        vegan = True
    if gluten_free_response == "yes":
        gluten_free = True

    print('Here are your restaurant choices: ')

    if vegetarian == False and vegan == False and gluten_free == False:
        print('Joe\'s Gourment Burgers')

    if vegan == False and gluten_free == False:
        print('Mama\'s Fine Italian')

    if vegan == False:
        print('Main Street Pizza Company')
    
    print('Corner Café')
    print('The Chef\'s Kitchen')

    yes = input('Enter \'yes\' if you would like to do another ' +
      'restaurant search (enter \'no\' to end): ')
