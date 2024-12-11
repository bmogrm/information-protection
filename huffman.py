import sys

message = "abcdef"
print(f"Изначальное сообщение: {message}")

# Подсчет частоты символов
freq = {}
for char in message:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(f"Частота символов: {freq}")

# Класс для узлов дерева
class Node:
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node(char='{self.char}', freq={self.freq}, left={self.left}, right={self.right})"

# Создание узлов из частот
tree = [Node(char, freq_char, None, None) for char, freq_char in freq.items()]

# Построение дерева Хаффмана
while len(tree) > 1:
    # Нахождение двух минимальных узлов
    min1 = min(tree, key=lambda node: node.freq)
    tree.remove(min1)
    min2 = min(tree, key=lambda node: node.freq)
    tree.remove(min2)

    # Создание нового родительского узла
    parent = Node(None, min1.freq + min2.freq, min1, min2)
    tree.append(parent)

# Корень дерева
new_tree = tree[0]
print(f"Корень дерева: {new_tree}")

# Генерация кодов символов
codes = {}

def recursive(node, code):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code
    recursive(node.left, code + "0")
    recursive(node.right, code + "1")

recursive(new_tree, "")

print(f"Коды символов: {codes}")

# Кодирование сообщения
coded_message = "".join(codes[char] for char in message)
print(f"Закодированное сообщение: {coded_message}")

# Декодирование сообщения
decoded_message = ""
current = new_tree
for bit in coded_message:
    current = current.left if bit == "0" else current.right
    if current.char is not None:
        decoded_message += current.char
        current = new_tree

print(f"Раскодированное сообщение: {decoded_message}")

# Оценка размера исходного и закодированного сообщений
original_size = len(message) * sys.getsizeof(message[0])
coded_size = len(coded_message)
compression = original_size / coded_size

print(f"Размер исходного сообщения: {original_size} бит")
print(f"Размер закодированного сообщения: {coded_size} бит")
print(f"Степень сжатия: {compression:.2f}")
