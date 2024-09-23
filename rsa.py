import random

def prime_generator(x):
    primes = []
    is_prime = [True] * x
    is_prime[0] = is_prime[1] = False  # 0 и 1 не являются простыми числами

    for p in range(2, x):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * p, x, p):
                is_prime[multiple] = False

    return primes

primes = [i for i in prime_generator(200) if i >= 100]

# Выбор случайных простых чисел p и q
p = random.choice(primes)
q = random.choice(primes)

# Вычисление n и функции Эйлера
n = p * q
euler_phi = (p - 1) * (q - 1)

print("Простые числа от 100 до 200:", *primes)
print("Случайные p и q:", p, q)
print("n (p*q):", n)
print("Функция Эйлера (φ(n)):", euler_phi)

# Выбор случайного целого, простого числа е
e = random.choice([i for i in prime_generator(n) if 1 < i < euler_phi and i != p and i !=q])
print("Случайное простое число e:", e)

# Вычисление числа d
d = pow(e, -1, euler_phi)
print("d:", d)

public_key, private_key = [e, n], [d, n] # Публичный и приватный ключ
print("Публичный ключ:", public_key, "\nПриватный ключ:", private_key)

# Шифрование сообщения
message = 15
m = pow(message, d) % n
print("Исходное сообщение:", message)
print("Шифрованное сообщение:", m)

# Дешифрование сообщения
c = pow(m, e) %n
print("Дешифрованное сообщение:", c)