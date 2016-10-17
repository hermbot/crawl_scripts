#!/usr/bin/env python
# morgue_downloader.py
# Michael Hermes

# First we want to read the HTML source for the page, making a list of all the
# lines that contain what we're looking for: morgue text files. We strip all
# of the characters that aren't part of the file name, and then download our
# list of files to the current directory.

from urllib import request
from sys import exit

no_connection = True
while no_connection:
    try:
        url = input('Please enter the url of your morgue directory: ')
        response = request.urlopen(url)
        no_connection = False
    except:
        print('No connection, please check your url.')

page_source = response.readlines()

character_list = []
for line in page_source:
    if 'morgue' in line and '.txt' in line:
        line = line.split('.txt">')[1]
        line = line.split('</A>')[0]
        character_list.append(line)

if len(character_list) == 0:
    print('No valid character files in directory.')
    exit_var = input('Press any key to exit.')
    exit()

for character in character_list:
    print('Downloading ' + character)
    urllib.urlretrieve(url + character, character)
    print(character + ' downloaded successfully.')

print('Script completed successfully.')
