# Считываем дек из файла
with open('deck.txt', 'r') as f:
    deck = f.read().strip()

# Считываем зашифрованное сообщение из файла
with open('shifr.txt', 'r') as f:
    encrypted_message = f.read().strip()

# Создаем пустую строку для расшифрованного сообщения
decrypted_message = ''

# Применяем правило замены символов на следующий по часовой стрелке через один в деке
for i in range(len(encrypted_message)):
    if (encrypted_message[i]==' '):
        decrypted_message += encrypted_message[i]
    else:
        encrypted_char = encrypted_message[i]
        deck_index = deck.find(encrypted_char)
        decrypted_char = deck[(deck_index - 2) % len(deck)]
        decrypted_message += decrypted_char

# Выводим расшифрованное сообщение
print(decrypted_message)