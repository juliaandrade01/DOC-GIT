def filtrar(lista):
    minusculas = [a for a in lista if a.islower()]
    return minusculas

# Ejemplo de uso:
words = ["Hol", "woAYYY", "Python", "XSUprogr", "is", "fun"]
lowercase_words = filtrar(words)
print("Palabras en minúsculas:", lowercase_words)
print("Palabras en minúsculas:", lowercase_words)