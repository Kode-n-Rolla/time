import sys, time
import sevseg   # Import sevseg.py for display seven-segment numbers

def cd():
    while True:  # Loop to get a number
        try:
            second_left = int(input('Input count of second(s) to countdown: '))
            break
        except ValueError:
            print('Entered not a number! Try again')

    try:
        while True:      # Main program loop
            # Clear the screen
            print('\n' * 10)

            # Get hour(s)/minute(s)/second(s) from second_left
            hours = str(second_left // 3600)
            minutes = str((second_left % 3600) // 60)
            seconds = str(second_left % 60)

            # Get string values from sevseg.py for hours
            hours_digits = sevseg.getSevSegStr(hours, 2)
            hour_top_row, hour_mid_row, hour_bottom_row = hours_digits.splitlines()

            # ... for minutes
            minutes_digits = sevseg.getSevSegStr(minutes, 2)
            minute_top_row, minute_mid_row, minute_bottom_row = minutes_digits.splitlines()

            # ... for seconds
            seconds_digits = sevseg.getSevSegStr(seconds, 2)
            second_top_row, second_mid_row, second_bottom_row = seconds_digits.splitlines()

            # Display countdown
            print(hour_top_row + '     ' + minute_top_row + '     ' + second_top_row)
            print(hour_mid_row + '  *  ' + minute_mid_row + '  *  ' + second_mid_row)
            print(hour_bottom_row + '  *  ' + minute_bottom_row + '  *  ' + second_bottom_row)

            # Instruction to time over
            if second_left == 0:
                print()
                print('Time is over!')
                break

            print()
            print('Press Ctrl-C to quit. (If running in cmd)\nOr Ctrl-F2 (If running in PyCharm)')

            time.sleep(1)       # Real countdown pause for 1 second
            second_left -= 1
    except KeyboardInterrupt:
        sys.exit('Thanks for running! Goodbye!')

# If this programm isn`t being imported, display countdown with entered digit
if __name__ == '__main__':
    cd()