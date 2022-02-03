base = input("Digite a o que deseja Descriptografar: ")

password = ""

for char in base:
    if char in '4': password = password + 'a'
    elif char in '#': password = password + 'b'
    elif char in '&': password = password + 'c'
    elif char in '#': password = password + 'd'
    elif char in '!': password = password + 'e'
    elif char in '3': password = password + 'f'
    elif char in '9': password = password + 'g'
    elif char in '6': password = password + 'g'
    elif char in '%': password = password + 'i'
    elif char in '|': password = password + 'o'
    elif char in '?': password = password + 'p'
    elif char in '_': password = password + 'r'
    elif char in '~': password = password + 's'
    elif char in '$': password = password + 't'
    else: password = password + char

print(password)