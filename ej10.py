def filtrar(lista):
    minusculas = [a for a in lista if a.islower()]
    return minusculas

# Ejemplo de uso:
words = ["HolaAAA", "world", "Python", "progr", "is", "fun"]
lowercase_words = filtrar(words)
print("Palabras en minúsculas:", lowercase_words)
