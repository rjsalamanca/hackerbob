guess_password = input('Guess the password: ')
saved_password = 'cnffjbeq'

def crack_password(password,rot):
    cipher = password
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    decoded = ''

    for letter in cipher:
        if letter.isalpha() and count < len(saved_password):
            get_index_of_letter = alphabet.index(letter)
            if get_index_of_letter < rot-1:
                if(alphabet[get_index_of_letter+rot] == saved_password[count]):
                    print('Characters Matched: %s at index %d' % (letter,count+1))
                    decoded += alphabet[get_index_of_letter+rot]
                else:
                    decoded += '*'
            else:
                if(alphabet[get_index_of_letter+rot-26] == saved_password[count]):
                    print('Characters Matched: %s at index %s' % (letter,count+1))
                    decoded += alphabet[get_index_of_letter+rot-26]
                else:
                    decoded += '*'
        else:
            decoded += '*'
        count += 1

    if(len(cipher) < len(saved_password)):
        decoded += '*' * (len(saved_password)-len(cipher))
        print('HINT: The password is longer')
    else:
        print('HINT: Try using a shorter password')

    return 'Secret password is: %s ' % decoded

print(crack_password(guess_password,13))