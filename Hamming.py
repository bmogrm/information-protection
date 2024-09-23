import math

def calculate_parity_bit(binary_message, parity_position, parity_bits):
    count = 0
    # Проверяем каждый бит, начиная с позиции parity_position
    for i in range(parity_position - 1, len(binary_message), 2 * parity_position):
        # Проходим по всем битам, которые покрывает текущий проверочный бит
        count += sum(int(bit) for bit in binary_message[i:i + parity_position])
    # Если количество единиц нечетное, проверочный бит будет 1, иначе 0
    test = '1' if count % 2 != 0 else '0'
    parity_bits.append(int(test))
    return test

def array_count_bits(c_bit, binary_message):
    parity_bits = []
    for i in range(c_bit):
        parity_position = 2 ** i
        parity_bit = calculate_parity_bit(binary_message, parity_position, parity_bits)
        # Обновляем проверочный бит в строке
        binary_message = binary_message[:parity_position-1] + parity_bit + binary_message[parity_position:]
    return binary_message, parity_bits

def binary_transform(message):
    binary_message = ''
    # Преобразуем сообщение в бинарный вид
    for char in message:
        binary_message += format(ord(char), '08b')
    return binary_message

def hamming_code(binary_message):
    c_bit = math.floor(math.log2(len(binary_message))) + 1

    # Проходим по каждому проверочному биту
    for i in range(c_bit):
        position = 2 ** i
        # Вставляем проверочный бит на нужную позицию
        binary_message = binary_message[:position-1] + '0' + binary_message[position-1:]
    
    binary_message, parity_bits = array_count_bits(c_bit, binary_message)

    return binary_message, parity_bits

def hamming_decode(error_encoded_message, c_bit):
    # Находим позицию ошибки
    error_position = 0
    for i in range(c_bit):
        if first_message[i] != second_message[i]:
            error_position += 2**i
    print('Ошибка найдена: позиция ошибки =', error_position)
    # Исправление ошибки
    inverted_bit = '0' if error_encoded_message[error_position-1] == '1' else '1'
    error_encoded_message = error_encoded_message[:error_position-1] + inverted_bit + error_encoded_message[error_position:]
    # Удаление контрольных битов
    for i in range(c_bit, -1, -1):
        error_encoded_message = error_encoded_message[:2**i-1] + error_encoded_message[2**i:]
    # Декодирование сообщения
    new_message = ''
    for i in range(0, len(error_encoded_message), 8):
        byte = error_encoded_message[i:i+8] # Вырезаем байт
        char = chr(int(byte,2)) # Байт в десятичное по аски, затем в символ
        new_message += char
    return new_message

# Пример использования
message = "cat"
binary_message = binary_transform(message)
encoded_message, first_message = hamming_code(binary_message)

c_bit = math.floor(math.log2(len(binary_message)))+1

error_position = int(input("Введите позицию ошибки: "))
if error_position <= len(encoded_message) and error_position > 0:
    inverted_bit = '0' if encoded_message[error_position-1] == '1' else '1'
    error_encoded_message = encoded_message[:error_position-1] + inverted_bit + encoded_message[error_position:]

    for i in range(c_bit, -1, -1): # удаление контрольных битов
            error_encoded_message = error_encoded_message[:2**i-1] + error_encoded_message[2**i:]

    error_encoded_message, second_message = hamming_code(error_encoded_message)
    print('Исходное сообщение', encoded_message, " --- ", 'Сообщение с ошибкой',error_encoded_message)

    new_message = hamming_decode(error_encoded_message, c_bit)
    print('Исходное сообщение', message, '---', 'Исправленное сообщение', new_message)
else:
    print("Позиция ошибки не соответствует длине сообщения")