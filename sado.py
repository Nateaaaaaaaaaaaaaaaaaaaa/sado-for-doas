import os
e = input('What would you like to run as root?')
cmd = "doas "
cmde = cmd + e
os.system(cmde)

