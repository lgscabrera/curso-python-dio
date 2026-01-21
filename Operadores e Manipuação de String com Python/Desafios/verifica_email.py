#entrada de usuario
email = input().strip()
#

if ' ' in email:
    print("E-mail inválido")

elif '@' not in email:
    print("E-mail inválido")

else:
    partes = email.split('@')
    
    if len(partes) == 2 and partes[0] and partes[1]:
        print("E-mail válido")
    else:
        print("E-mail inválido")