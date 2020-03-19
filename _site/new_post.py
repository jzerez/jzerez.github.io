import sys
from os import listdir
import datetime
import random
def get_last_post(path, new_name):
    files = listdir(path)
    for file in files:
        if new_name in file:
            print('Project Name already exsists')
            quit()
    return len(files)

def destrip_hypens(s):
    words = s.split('-')
    new_string = ""
    for word in words:
        new_string += word[0].upper() + word[1:] + " "
    return new_string

path = './_posts/'

if len(sys.argv) == 3:
    date = sys.argv[2]
else:
    print('Error using this script. Please provide a project name (required) and a date in the format YYYY-MM-DD (required) as command line arguments. Example:')
    print('python new_post.py project-name 2020-04-20')
    quit()
project_name = sys.argv[1]

alt_images = ['pic02.jpg', 'pic03.jpg', 'pic04.jpg', 'pic05.jpg', 'pic06.jpg']
categories = ['layout', 'title', 'excerpt', 'short_desc', 'categories', 'date_string', 'image', 'alt', 'github']
months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
id = get_last_post(path, project_name) + 1;

filename = str(date)+'-'+project_name+'.md'
full_filename = path + filename
file = open(full_filename, 'x')
file.write('---\n')
for category in categories:
    if category == 'layout':
        suffix = 'post'
    elif category == 'title':
        suffix = destrip_hypens(project_name)
    elif category == 'categories':
        suffix = "[]"
    elif category == 'date_string':
        year = int(date.split('-')[0])
        month_index = int(date.split('-')[1]) - 1
        month = months[month_index]
        suffix = str(month) + ', ' + str(year)
    elif category == 'alt':
        suffix = random.choice(alt_images)
    else:
        suffix = ''
    file.write(category + ': ' + suffix + '\n')

file.write('---')
file.close()

print(filename)
print('was created successfully!')
