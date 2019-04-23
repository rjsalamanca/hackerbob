saved_password = 'cnffjbeq'

def encode(unhashed_password):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded = ''

    for letter in unhashed_password:
        if letter.isalpha():
            get_index_of_letter = alphabet.index(letter)
            if get_index_of_letter < 12:
                decoded += alphabet[get_index_of_letter+13]
            else:
                decoded += alphabet[get_index_of_letter+13-26]
        else:
            decoded += letter
    return decoded

def crack_password(password_crack):
    guess_password = input('Guess the password: ')
    hashed_password = encode(guess_password)
    count_index = 0
    cracked = True

    for letter in hashed_password:

        if letter == password_crack[count_index]:
            print('Character Matched: %s at position %d' % (letter,count_index+1))
        else:
            print('Character Failed: %s at position %d' % (letter, count_index+1))
            cracked = False

        count_index += 1
    
    if cracked:
        return print('1337 H4X0R')
    else:
        return print('womp womp')

"""     
    for letter in hashed_password:
        if letter.isalpha() and count < len(saved_password):
            get_index_of_letter = alphabet.index(letter)
            if get_index_of_letter < rot-1:
                if alphabet[get_index_of_letter+rot] == saved_password[count]:
                    print('Character Matched: %s at index %d' % (letter,count+1))
                    decoded += alphabet[get_index_of_letter+rot]
                else:
                    print('Character Failed: %s at index %d' % (letter, count+1))
                    decoded += '*'
            else:
                if alphabet[get_index_of_letter+rot-26] == saved_password[count]:
                    print('Character Matched: %s at index %s' % (letter,count+1))
                    decoded += alphabet[get_index_of_letter+rot-26]
                else:
                    print('Character Failed: %s at index %d' % (letter, count+1))
                    decoded += '*'
        else:
            # add stars if password is too long
            decoded += '*'
        count += 1

    if len(cipher) < len(saved_password):
        decoded += '*' * (len(saved_password)-len(cipher))
        print('HINT: The password is longer')
    elif len(cipher) > len(saved_password):
        print('HINT: Try using a shorter password')

    if decoded == saved_password:
        return '1337 H4X0R'
    else:
        print('Secret so far is: %s ' % decoded)
        return 'womp womp' 
"""

crack_password(saved_password)