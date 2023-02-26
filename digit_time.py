import sys, time
import sevseg # Import sevseg.py for display seven-segment numbers


def dt():
    while True:  # Loop to get a gradation time
        try:
            gradation_time = int(input('Are you want to chose 12 or 24 gradation? - '))
            if gradation_time == 12 or gradation_time == 24:       # Valid correct input
                break
            else:
                print('Incorrect digit')
        except ValueError:
            print('Your input isn`t a digit')

    try:
        while True:      # Main program loop
            # Clear the screen
            print('\n' * 5)

            # Get the current time from the computers`s clock
            current_time = time.localtime()
            # Get an hour with selected gradation time
            hours = str(current_time.tm_hour % gradation_time)
            if gradation_time == 12:
                if hours == '0':
                    hours = '12'    # Cause 12-hour clocks show 12:00, but 00:00
            minutes = str(current_time.tm_min)
            seconds = str(current_time.tm_sec)

            # Get string values from sevseg.py for hours
            hour_digits = sevseg.getSevSegStr(hours, 2)
            hour_top_row, hour_mid_row, hour_bottom_row = hour_digits.splitlines()

            # ... for minutes
            minutes_digits = sevseg.getSevSegStr(minutes, 2)
            minute_top_row, minute_mid_row, minute_bottom_row = minutes_digits.splitlines()

            # ... for seconds
            seconds_digits = sevseg.getSevSegStr(seconds, 2)
            second_top_row, second_mid_row, second_bottom_row = seconds_digits.splitlines()

            # Display current clocks
            print(hour_top_row + '     ' + minute_top_row + '     ' + second_top_row)
            print(hour_mid_row + '  *  ' + minute_mid_row + '  *  ' + second_mid_row)
            print(hour_bottom_row + '  *  ' + minute_bottom_row + '  *  ' + second_bottom_row)

            print()
            print('Press Ctrl-C to quit. (If running in cmd)\nOr Ctrl-F2 (If running in PyCharm)')

            # Keep looping until the second changes:
            while True:
                time.sleep(0.01)
                if time.localtime().tm_sec != current_time.tm_sec:
                    break
    except KeyboardInterrupt:
        sys.exit('Thanks for running! Hasta la vista!')

# If this programm isn`t being imported, display the current time
if __name__ == '__main__':
    dt()