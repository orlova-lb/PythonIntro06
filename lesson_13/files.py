
# import os

# print(os.sep)

"""
.       current folder
..      parent folder

win     \r\n
linux   \n
mac     \r

    open(file_name [,mode])
mode:
r       read
w       write
x       exclusive
a       append

t       text            tw, tr
b       binary          br, bw, bx, ba
"""

# file_r = open('func_format.py')
# file_w = open('func_format_copy.py', 'x')
#
# # data = file.read()
# while True:
#     data = file_r.readline()
#     if data == '':
#         break
#
#     print(data, end='')
#     file_w.write(data)
#
# file_r.close()
# file_w.close()

buffer_size = 32
with open('rekursiya.jpg', 'rb') as src, open('rekursiya_copy.jpg', 'wb') as dst:
    if not src.closed:
        print('Source file opened')

    if not dst.closed:
        print('Destination file opened')

    while True:
        data = src.read(buffer_size)
        if data:
            dst.write(data)
        else:
            break

if src.closed:
    print('Source file closed')

if dst.closed:
    print('Destination file closed')



















