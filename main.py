try:
    print(open('chat.txt', encoding='utf-8').read())
except FileNotFoundError:
    print("The file 'chat.txt' was not found.")

