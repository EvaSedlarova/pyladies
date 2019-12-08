print("I heard this poem:\n")

with open('poem.txt', encoding='utf-8') as file_: # kontext manager
    for line in file_:
        line = line.rstrip()
        print(' ' + line)
    
print("\nDO you like it?")