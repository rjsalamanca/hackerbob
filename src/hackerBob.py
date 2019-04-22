guess_password = input('Guess the password: ')
saved_password = 'nop'

def crack_password(password,rot):
    cipher = password
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    
    for letter in cipher:
        if letter.isalpha():
            get_index_of_letter = alphabet.index(letter)
            if get_index_of_letter < rot-1:
                if(alphabet[get_index_of_letter+rot] != saved_password[count]):
                    return False
            else:
                if(alphabet[get_index_of_letter+rot-26] != saved_password[count]):
                    return False
        count += 1
    return True

print(crack_password(guess_password,13))

# input str
# convert str to rot 13
# compare encoded and saved pwd