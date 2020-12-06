with open ('file1.txt', 'w', encoding='utf-8') as f_obj:
    while True:
        line =  input('Ввести текст: ')
        if line == '':
            break
        f_obj.write(line + '\n')
print(f_obj.closed)

