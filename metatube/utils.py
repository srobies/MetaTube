def strtobool (string):
    if str(string) in ['y', 'yes', 't', 'true', 'on', '1']:
        return True
    elif str(string) in ['n', 'no', 'f', 'false', 'off', '0']:
        return False
    else:
        return ValueError(f'{string} is not a valid input')
