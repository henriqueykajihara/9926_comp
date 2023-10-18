import ply.yacc as yacc
from lexer import tokens, gera_tokens


class Node:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        self.children = children if children is not None else []
        self.leaf = leaf

# Guarda as variáveis e o tipo
# Aqui na análise sintática os tipos são inicializados como ""
variables = {}


# Regras gramaticais

def p_programa(p):
    '''
    lista_statement : lista_statement statement
                    | statement
    '''
    if len(p) == 3:
        p[0] = Node("programa", [p[1], p[2]])
    else:
        p[0] = p[1]


def p_statement_expr(p):
    '''
    statement : expressao_identifier ATRIBUI expressao_logica PONTO_VIRGULA
              | PRINT L_PARENTESES expressao_string R_PARENTESES PONTO_VIRGULA
              | expressao_enquanto 
    '''
    #print(len(p))#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    tamanho = len(p)
    if tamanho == 5:
        variables[p[1].leaf] = ""
        p[0] = Node(p[2], [p[1], p[3]]) 
    elif tamanho == 6:
        p[0] = Node(p[1], [p[3]])
    else:
        p[0] = p[1]

def p_expressao_enquanto(p):
    '''
        expressao_enquanto : WHILE expressao_logica lista_statement ENDWHILE
    '''
    p[0] = Node(p[1], [p[2], p[3]])


def p_expressao_logica(p):
    '''
        expressao_logica : expressao_logica AND expressao_relacional
                         | expressao_logica OR expressao_relacional
                         | expressao_relacional
    '''

    if len(p) > 2:
        p[0] = Node(p[2], [p[1], p[3]])
    else:
        p[0] = p[1]


def p_expressao_relacional(p):
    '''
    expressao_relacional : expressao_relacional MAIOR expressao_aritmetica
                         | expressao_relacional MENOR expressao_aritmetica
                         | expressao_relacional MAIOR_IGUAL expressao_aritmetica
                         | expressao_relacional MENOR_IGUAL expressao_aritmetica
                         | expressao_relacional DIFERENTE expressao_aritmetica
                         | expressao_relacional EQUIVALENTE expressao_aritmetica
                         | expressao_aritmetica    
    '''

    if len(p) > 2:
        p[0] = Node(p[2], [p[1], p[3]])
    else: p[0] = p[1]    
    

def p_expressao_aritmetica(p):
    '''
    expressao_aritmetica : expressao_aritmetica SOMA termo
                         | expressao_aritmetica SUBTRAI termo
                         | termo
    '''

    if len(p) > 2:
        p[0] = Node(p[2], [p[1], p[3]])
    else:
        p[0] = p[1]


def p_termo(p):
    '''
    termo : termo MULTIPLICA fator
          | termo DIVIDE fator
          | fator
    '''

    if len(p) > 2:
        p[0] = Node(p[2], [p[1], p[3]])
    else:
        p[0] = p[1]


def p_fator(p):
    '''
    fator : L_PARENTESES expressao_logica R_PARENTESES
          | expressao_string
          | expressao_inteiro
          | expressao_identifier
          | expressao_float
    '''

    if p[1] == '(':           
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_expressao_string(p):
    '''
    expressao_string : STRING
    '''
    p[0] = Node("STRING", leaf=p[1])


def p_expressao_inteiro(p):
    '''
    expressao_inteiro : INTEIRO
    '''
    p[0] = Node("INTEIRO", leaf=int(p[1]))


def p_expressao_float(p):
    '''
    expressao_float : FLOAT
    '''
    p[0] = Node("FLOAT", leaf=float(p[1]))


def p_expressao_identifier(p):
    '''
    expressao_identifier : IDENTIFIER
    '''
    p[0] = Node("IDENTIFIER", leaf=p[1])


# Regra para lidar com erros de sintaxe
def p_error(p):
    print(f"Erro de sintaxe na linha {p.lineno}: '{p.value}'")


def debuga(nome,p):
    print(nome)
    for elemento in p:
        print(elemento)
    print(nome + ' final')


# Função para imprimir a AST
def print_ast(node, level=0):
    print("   " * level + node.type)
    if node.leaf is not None:
        print("   " * (level + 1) + str(node.leaf))
    for child in node.children:
        print_ast(child, level + 1)


def parse_code(code):
    parser = yacc.yacc()
    return parser.parse(code), variables