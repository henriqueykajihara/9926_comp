import ply.lex as lex

reserved = {
    'and': 'AND',
    'or': 'OR',
    'print': 'PRINT',
    'while': 'WHILE',
    'endwhile': 'ENDWHILE',
    'true': 'TRUE',
    'false': 'FALSE',
}

tokens = (
    'INTEIRO',
    'FLOAT',
    'STRING',
    'SUBTRAI',
    'SOMA',
    'MULTIPLICA',
    'DIVIDE',
    'L_PARENTESES',
    'R_PARENTESES',
    'ATRIBUI',
    'AND',
    'OR',
    'IDENTIFIER',
    'MAIOR',
    'MENOR',
    'MAIOR_IGUAL',
    'MENOR_IGUAL',
    'DIFERENTE',
    'EQUIVALENTE',
    'PONTO_VIRGULA',
    'PRINT',
    'WHILE',
    'ENDWHILE',
)


t_SOMA = r'\+'
t_SUBTRAI = r'-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'/'
t_L_PARENTESES = r'\('
t_R_PARENTESES = r'\)'
t_ATRIBUI = r'='
t_MAIOR = r'>'
t_MENOR = r'<'
t_MAIOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_DIFERENTE = r'!='
t_EQUIVALENTE = r'=='
t_PONTO_VIRGULA = r';'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


def t_FLOAT(t):
    r'[+-]?[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t


def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t


t_ignore = ' \t'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass


def t_error(t):
    print(f"Ilegal character '{t.value[0]}' at line {t.lexer.lineno}, position {t.lexpos} ")
    t.lexer.skip(1)


def gera_tokens(codigo):

    lexer = lex.lex()
    lexer.input(codigo)
    token_list = []
    while True:
        token = lexer.token()
        if not token:
            return token_list
        token_list.append(token)
        print(token)


lexer = lex.lex()
