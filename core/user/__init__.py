#// Lib
from random import choice
from string import ascii_letters,digits
#// Function

#// El nombre del usuario expecifico
def user_name():
    carracter = ascii_letters + "_-" + digits
    return ''.join(choice(carracter) for _ in range(12))


if __name__ == '__main__':
    print(user_name())
    pass