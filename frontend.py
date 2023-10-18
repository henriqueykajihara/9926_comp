from syntax import parse_code
from analise_semantica import analise_semantica

# Códigos de exemplo
# funciona corretamente 
code_0 = """
x = 3 + 12 * (3 / 8 + 9);
""" 

# funciona corretamente
code_1 = """
x = 3 + 12;
y = 2.45 + 3.89;
""" 

# funciona corretamente
code_2 = """
x = 3;
y = 8;
z = x + y;
""" 

# ERRO: tipos diferentes
code_3 = """
x = 2 + 3.0;
"""

# ERRO: tipos diferentes (var)
code_4 = """

while 1
print("'batata frita");
asdf = 2;
x = y;

endwhile

x = 2;
y = 3.2;
z = x + y;

"""

# ERRO: var nao inicializada
code_5 = """
x = 2;
z = x + a;
"""

# ERRO: var nao inicializada
code_6 = """
x = 2;
z = x + a;


"""
def main():
    code = code_4
    print('Codigo:')
    print(code)
    print('Iniciando...')    
    ast, variables = parse_code(code)
    analise_semantica(ast, variables)
    print("OK")

if __name__ == "__main__":
    main()
