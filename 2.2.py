from collections import deque

# Считываем зашифрованное сообщение из файла
with open('shifr.txt', 'r') as f:
    encrypted_message = f.read().strip()

deck = deque(['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в',
             'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'])
# Создаем пустую строку для расшифрованного сообщения
decrypted_message = ''

# Применяем правило замены символов на следующий по часовой стрелке через один в деке
for i in range(len(encrypted_message)):
    if (encrypted_message[i] == ' '):
        decrypted_message += encrypted_message[i]
    else:
        encrypted_char = encrypted_message[i]
        deck_index = deck.index(encrypted_char)
        decrypted_char = deck[(deck_index - 2) % len(deck)]
        decrypted_message += decrypted_char

# Выводим расшифрованное сообщение
print(decrypted_message)
