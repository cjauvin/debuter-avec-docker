# import sys

# name = sys.argv[1] if len(sys.argv) > 1 else 'Stranger'

# print(f'Hello {name}!')

import sys
import datetime as dt
import cowsay

name = sys.argv[1] if len(sys.argv) > 1 else 'stranger'

wd = dt.datetime.today().strftime('%A')

#cowsay.cow(f'Hello {name}!')
cowsay.cow(f'Hello {name}, today is {wd}!')
