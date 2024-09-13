from num2words import num2words

print(num2words(42))  # Выведет forty-two
print(num2words(42, to='ordinal')) # Выведет forty-second
print(num2words(42, lang='fr'))  # Выведет quarante-deux