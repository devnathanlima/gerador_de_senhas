import random
import string

n_letters = int(input("Quantas letras você quer?: "))
n_numbers = int(input("Quantos números você quer?: "))
n_symbols = int(input("Quantos símbolos você quer?: "))


letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%¨&*()_+?:;.,"

rnd = random.SystemRandom()

rand_letters = ''.join(rnd.choice(letters) for i in range(n_letters))
rand_numbers = ''.join(rnd.choice(numbers) for i in range(n_numbers))
rand_symbols = ''.join(rnd.choice(symbols) for i in range(n_symbols))

elements = rand_letters+rand_numbers+rand_symbols
senha = ''.join(random.sample(elements, len(elements)))
print(senha)
