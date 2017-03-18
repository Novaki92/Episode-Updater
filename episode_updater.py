import re, os, sys, time
from random import random

print("\nType 'help' for a list of user actions\n")


# Functions
def updateFile(strInfo):
    new_text = 'Last Episode: ' + str(nums[0]) + '\n' + 'Next Episode: ' + str(
        nums[1]) + '\n' + 'Episodes Left: ' + str(nums[2]) + '\n'
    file.seek(0)
    file.truncate()
    file.write(new_text)
    file.close()
    print('Information ' + strInfo + ': ' + str(nums) + '\n')


def createFile():
    slow_type('Creating file...', faster)
    file = open(file_name, 'r+')
    last_episode = int(input('Last Episode Watched: '))
    next_episode = last_episode + 1
    episodes_left = int(input('Number of Episodes: ')) - last_episode
    new_text = 'Last Episode: ' + str(last_episode) + '\n' + 'Next Episode: ' + str(
        next_episode) + '\n' + 'Episodes Left: ' + str(episodes_left) + '\n'
    file.write(new_text)
    file.close()
    slow_type('File created...\n', faster)


slower = 25
slow = 50
fast = 75
faster = 100
fastAF = 4000


def slow_type(t, speed):
    for letter in t:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random() * 10.0 / speed)
    print('')


# Main Loop
exit = False
file_name = 'episode.txt'
try:
    file = open(file_name)
    file.close()
except IOError:
    file = open(file_name, 'w+')
    file.close()

while exit != True:

    file = open(file_name, 'r+')
    text = file.read()
    if text == '':
        createFile()
    nums = re.findall('\d+', text)  # Find digits
    nums = list(map(int, nums))  # Convert to ints

    prompt = input('Select user action: ').lower()
    if prompt == 'help':
        slow_type('Command list: print, increase, decrease, readme, about, exit\n', fastAF)
    elif prompt == 'print':
        file = open(file_name, 'r+')
        text = file.read()
        slow_type(text, 300)
    elif prompt == 'increase':
        nums[0] += 1
        nums[1] += 1
        nums[2] -= 1
        updateFile('increased')
    elif prompt == 'decrease':
        nums[0] -= 1
        nums[1] -= 1
        nums[2] += 1
        updateFile('decreased')
    elif prompt == 'readme':
        slow_type(
            '\nIf this is your first time using this program it will automatically create a file in the folder \nwhere the program is located called ' + file_name + '.\n',
            fastAF)
        slow_type('Here you will be asked to enter the last episode you watched and the total number of episodes.\n',
                  fastAF)
        slow_type(
            'From here you will be asked to make an action - a list of available actions can be found by typing \n\'help\' and pressing enter.\n',
            fastAF)
        slow_type('PRINT: prints the contents of the text file', fastAF)
        slow_type('INCREASE: updates the data to show that you have watched another episode', fastAF)
        slow_type('DECREASE: if you made a mistake and accidently increased you can always go back one', fastAF)
        slow_type('README: you\'re lookin at it mang', fastAF)
        slow_type('ABOUT: shameless advertisement for my super lucrative scripting business :^)', fastAF)
        slow_type('EXIT: closes the program\n', fastAF)
    elif prompt == 'about':
        slow_type('Novaki - 2017', slow)
        slow_type('https://github.com/Novaki92\n', slow)
    elif prompt == 'exit':
        slow_type('Exiting...', slower)
        file.close()
        exit = True
    else:
        print('Not a valid input\n')
