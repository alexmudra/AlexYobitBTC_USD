'''
This somewhat depends on what platform you are on. The most common way to do this is by printing ANSI escape sequences.
For a simple example, here's some python code from the blender build scripts:
'''



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)




"""
Приклади як оформити кольорами вивід
"""
# print(Colors.WARNING + "This is name: " + Colors.ENDC + Colors.OKBLUE + str(name) + Colors.ENDC)
# print(Colors.WARNING + "This is amount: " + Colors.ENDC + Colors.OKBLUE + str(amount) + Colors.ENDC)
# print(Colors.WARNING + "This is currency: " + Colors.ENDC + Colors.OKBLUE + str(currency) + Colors.ENDC)