
tokens = [
    'NUMBER',
    'ID',
    # 'PLUS',
    # 'MINUS',
    # 'TIMES',
    # 'DIVIDE',
    # 'LPAREN',
    # 'RPAREN',
    # 'LCBR',
    # 'RCBR',
    'EQ_OP',
    'NE_OP',
    'POW',
    'LE_OP',
    'GE_OP',
    'LEFT_OP',
    'RIGHT_OP'
]

# Regular expression rules for simple tokens
t_EQ_OP = r'=='
t_NE_OP = r'!='
t_POW = r'\^\^'
t_LE_OP = r'<='
t_GE_OP = r'>='
t_LEFT_OP = r'<<'
t_RIGHT_OP = r'>>'


reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE'
}

# t_IF = r'if'
# t_ELSE = r'else'

tokens += list(reserved.values())

literals = ['+', '-', '*', '/', '%', '(', ')', '{', '}', '<', '>', '=', ';']


# def t_NUMBER(t):
#     r'\d+'
#     n_type = 'None'
#     t.value = (int(t.value), n_type)
#     return t


def t_NUMBER(t):
    r'(?P<n_value>\d+)(<(?P<n_type>\w+)>)?'
    n_value = t.lexer.lexmatch['n_value']
    n_type = t.lexer.lexmatch['n_type']
    if n_type is None:
        n_type = 'raw'
    t.value = (n_type, int(n_value))
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
