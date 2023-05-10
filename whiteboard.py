# Given a string 
# after every 'y' or 'Y' add an !  
# after every 's' add a peroid but not after 'S'
# and make every 'w' and 'g' capital W and G

# Make a Function that takes a string as input
# and returns the adjusted string.
s="Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"
#output= Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!

def solution(string):
    new_string = ''
    for letter in string:
        if letter.lower() == 'y':
            new_string += letter + '!'
        elif letter == 's':
            new_string += letter + '.'
        elif letter in {'w', 'g'}:
            new_string += letter.upper()
        else:
            new_string += letter
    return new_string
