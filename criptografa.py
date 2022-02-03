base = input("Digite a palavra que deseja Criptografar: ")

password = ""

for char in base:
    if char in 'Aa': password = password + '4'
    elif char in 'Bb': password = password + '#'
    elif char in 'Cc': password = password + '&'
    elif char in 'Dd': password = password + '@'
    elif char in 'Ee': password = password + '!'
    elif char in 'Ff': password = password + '3'
    elif char in 'Gg': password = password + '9'
    elif char in 'Hh': password = password + '6'
    elif char in 'Ii': password = password + '%'
    elif char in 'Oo': password = password + '|'
    elif char in 'Pp': password = password + '?'
    elif char in 'Rr': password = password + '_'
    elif char in 'Ss': password = password + '~'
    elif char in 'Tt': password = password + '$'
    else: password = password + char

print(password)