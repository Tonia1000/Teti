from user import Ususario

user = Ususario()
user.name = "Ze"
user.password = "123"

validation = user.validate()
if validation==True:
    print("Validado com Sucesso")
    
else:
    print("Ususario e/ou senha incorreto")
    
# ----------------------------------------------------------------
