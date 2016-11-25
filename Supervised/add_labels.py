file_name = "static_1x4_letters_W_1.txt"
label = ',W'

with open(file_name, 'r') as f :
    file_lines = [''.join([x.strip(), label, '\n']) for x in f.readlines()]
with open(file_name, 'w') as f:
    f.writelines(file_lines) 
