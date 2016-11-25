file_name = "static_1x4_letters_T_1.txt"
label = ',3'

with open(file_name, 'r') as f :
    file_lines = [''.join([x.strip(), label, '\n']) for x in f.readlines()]
with open(file_name, 'w') as f:
    f.writelines(file_lines) 
