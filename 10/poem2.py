with open('second-poem.txt', mode='w', encoding='utf-8') as file_: # kontext manager
    print('Naše staré hodiny', file=file_)
    print('Bijí', 2 + 2, 'hodiny', file=file_)

with open('second-poem.txt', encoding='utf-8') as file_: # kontext manager
    content = file_.read()
print(content) 