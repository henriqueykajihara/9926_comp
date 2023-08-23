import tokens as tk

#********************************************************************************#
def teste():
    return """3 + 12 * (8 - 5)
x = 10
print("teste de codigo")
for x in range( 10 ):
    print(10.342 * x)
    if x != 9:
        print('negocio estranho')"""

#********************************************************************************#
if __name__ == "__main__":
    codigo = teste()
    
    print(codigo)
    print('\n')
    tk.processa(codigo)