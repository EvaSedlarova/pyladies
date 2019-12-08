with open('second-poem.txt', mode='w', encoding='utf-8') as file_: # kontext manager
    file_.write('Naše staré hodiny \nBijí 4 hodiny')
    

with open('second-poem.txt', encoding='utf-8') as file_: # kontext manager
    content = file_.read()
print(content) 