#! python3
# password.py - An insecure password locker program.

import pyperclip, sys

PASSWORDS = {'email': 'gabad7845_aB',
             'blog': 'caracolitos_21',
             'luggage': '0123456789'}

if len(sys.argv) < 2:
    print('Usage: py password.py [account] - copy account password.')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
