import string as s
 
lista_caracteres = list(s.ascii_letters + s.digits + s.punctuation)

MSG = []
for i in lista_caracteres:
    MSG.append(ord(i))