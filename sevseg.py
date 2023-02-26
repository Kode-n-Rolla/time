
def getSevSegStr(numb, min_width=0):
    """ Return a seven-segment display string of numbers
    The returned string will be padded with zerros if it`s smaller then min_width. """

    # Convert number to string in case it`s an int or float:
    numb = str(numb).zfill(min_width)

    rows = ['', '', '']
    for i, elem in enumerate(numb):
        if elem == '.':     # Condition for decimal point
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue        # To skip space between digits
        elif elem == '-':   # Condition for negative sign
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif elem == '0':    # Condition for display 0
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif elem == '1':   # Condition for display 1
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif elem == '2':   # Condition for display 2
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif elem == '3':   # Condition for display 3
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif elem == '4':   # Condition for display 4
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif elem == '5':   # Condition for display 5
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif elem == '6':   # Condition for display 6
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif elem == '7':   # Condition for display 7
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif elem == '8':   # Condition for display 8
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif elem == '9':   # Condition for display 9
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # Add a space between elements if isn`t the last numeral
        if i != len(numb) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    return '\n'.join(rows)

# If this programm isn`t being imported, display the numbers from 00 to 99
if __name__ == '__main__':
    print('I can display seven-segment number')
    print('For example, this code:')
    print('import sevseg')
    print('my_numb = sevseg.getSevSegStr(420, 3)')
    print('print(my_numb\n')
    print('You can see your number, zero-padded to three digits:')
    print('      __   __ ')
    print('|__|  __| |  |')
    print('   | |__  |__|')
