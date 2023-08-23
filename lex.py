import ply.lex as lex

tokens = ('MULTIPLICA',
    'SOMA',
    'SUBTRAI',
    'DIVIDE',
    'MENOR',
    'MAIOR',
    'IGUAL',
    'DIFERENTE',
    'L_PARENTESES',
    'R_PARENTESES',
    'DOIS_PONTOS',
    'PONTO',
    'VIRGULA',
    'IF',
    'WHILE',
    'FOR',
    'IN',
    'RANGE',
    'DEF',
    'LEN',
    'PRINT',
    'ESPACO',
    'VARIAVEL',
    'NOVA_LINHA',
    'STRING',
    'FLOAT',
    'INTEGER')

t_MULTIPLICA   = r'\*'
t_SOMA         = r'\+'
t_SUBTRAI      = r'\-'
t_DIVIDE       = r'\/'
t_MENOR        = r'\>'
t_MAIOR        = r'\<'
t_IGUAL        = r'\='
t_DIFERENTE    = r'\!='
t_L_PARENTESES = r'\('
t_R_PARENTESES = r'\)'
t_DOIS_PONTOS  = r'\:'
t_PONTO        = r'\.'
t_VIRGULA      = r'\,'
t_IF           = r'if'
t_WHILE        = r'while'
t_FOR          = r'for'
t_IN           = r'in'
t_RANGE        = r'range'
t_DEF          = r'def'
t_LEN          = r'len'
t_PRINT        = r'print'

#********************************************************************************#
def t_VARIAVEL(token):
    r'[a-zA-Z_][a-zA-Z09_]*'
    return token

#********************************************************************************#
def t_NOVA_LINHA(token):
    r'\n+'
    #token.lexer.lineno += len(token.value)
    print('\n')
    #token.type = 'NOVA_LINHA'
    return token

#********************************************************************************#
def t_STRING(token):
    r'(\'[^\']*\'|"[^"]*")'
    token.value = token.value[1:-1]
    return token

#********************************************************************************#
def t_FLOAT(token):
    r'\d+\.\d+([eE][-+]?\d+)?'
    token.value = float(token.value)
    return token

#********************************************************************************#
def t_INTEGER(token):
    r'\d+'
    token.value = int(token.value)
    return token

#********************************************************************************#
#t_ignore = ' \t\n\r'
t_ignore = ' \t\r'
#********************************************************************************#
def t_error(token):
    print(f"Caractere inválido: '{token.value[0]}' na linha {token.lineno}, posição {token.lexpos}")
    token.lexer.skip(1)

#********************************************************************************#
def processa(codigo):

    lexer = lex.lex()
    lexer.input(codigo)
    while True:
        token = lexer.token()
        if not token:
            return
        print(token)
        #print(token.value)
        #print(token.type)
        