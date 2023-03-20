# Lab 06: Software Engineering
# Chrystina Woehler
# Last Edited: 3/20/2023

def encode(password):
    #converts input into list
    convert = list(password)
    #checks each value
    for i in range(0, len(password), 1):
        if int(convert[i]) <= 7:
            convert[i] = str(int(convert[i]) + 3)
        else:
            diff = 10 - int(convert[i])
            convert[i] = str(3 - diff)
    convert = ''.join(convert)
    return convert



def menu():
    print('Menu')
    print('-------------')
    print('1. Encode\n2. Decode\n3. Quit\n')
    choice = int(input('Please enter an option:'))
    return choice

if __name__ == "__main__":
    stop = False
    while stop != True:
        choice = menu()
        if choice == 1:
            password = input('Please enter your password to encode:')
            password = encode(password)
            print('Your password has been encoded and stored!\n')
        elif choice == 2:
            print()
        elif choice == 3:
            stop = True

