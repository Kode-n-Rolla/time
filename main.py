import countdown, digit_time        # Import modules

def main_func():     # The main func
    while True:      # Loop to get the choice
        try:
            choice = int(input('Running countdown (1) or current time (2)? - '))
            if choice == 1 or choice == 2:      # Valid correct input
                break
            else:
                print('Incorrect digit')
        except ValueError:
            print('Your input isn`t a digit')

    if choice == 1:
        countdown.cd()
    else:
        digit_time.dt()

while True:     # The main loop of project
    main_func()
    exit_or_no = input('Another one? [Y/n] - ').lower()
    if exit_or_no == 'y' or exit_or_no == 'yes':
        main_func()
    elif exit_or_no == 'n' or exit_or_no == 'no':
        print('Thanks for running! Have a nice day!')
        break