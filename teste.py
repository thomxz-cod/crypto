import string as s
 
lista_caracteres = list(s.ascii_letters + s.digits + s.punctuation)

lista_enc = 'ad28a31e99148f0a85007bf671ec67e25dd853ce49c43fba35b04dc843be39b42faa25a01b96118c0782fd78f36ee964df5ad550229d18930e89047ffa75ed68e35ed954cf4ac540bb36b12ca7f06be661dc57d2cb46c13cb7322ba6219c'

lista_enc_sep = []
for i in range(0, len(lista_enc), 2):
    lista_enc_sep.append(f'{lista_enc[i]}{lista_enc[i+1]}')


dic = {}
for i in range(len(lista_enc_sep)):
    dic[lista_enc_sep[i]] = lista_caracteres[i]

for key, value in dic.items():
    print(key, value)