import ply.lex as lex

tokens = (
    'MAYUSCULA',
    'MINUSCULA',
    'NUMEROS',
    'ESPACIOS',
    'SIMBOLOS',    
)

################### REGLAS ############################
t_MAYUSCULA = r'[A-ZÑ]'
t_MINUSCULA = r'[a-zñ]'
t_NUMEROS = r'\d'
t_ESPACIOS = r'[ \t]'
t_SIMBOLOS = r'[¿\?¡!"#$%&/\(\)=\'\+\-_\*\\@><\{\}ç\[\]\^,;:\.\|~]'


def t_error(t):
    print(f"Caracter no Valido: {t.value[0]!r} en posición {t.lexpos}")
    t.lexer.skip(1)


def mostrar(lexer):
    for tok in lexer:
        print(f"Token({tok.type}: {tok.value!r})")


lexer = lex.lex()
data = "Hola mundo  que taál"
lexer.input(data)
mostrar(lexer)


