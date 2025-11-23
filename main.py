import ply.lex as lex
from cripto import ENC_MAP, DEC_MAP
tokens = (
    'MAYUSCULA',
    'MINUSCULA',
    'NUMEROS',
    'ESPACIOS',
    'SIMBOLOS',
    'NUEVALINEA',    
)

################### REGLAS ############################
t_MAYUSCULA = r'[A-ZÑ]'
t_MINUSCULA = r'[a-zñ]'
t_NUMEROS = r'\d'
t_ESPACIOS = r'[ \t]'
t_SIMBOLOS = r'[¿\?¡!"#$%&/\(\)=\'\+\-_\*\\@><\{\}ç\[\]\^,;:\.\|~]'

def t_NUEVALINEA(t):
    r'\n'
    t.value = '\n'   # el caracter real
    return t

def t_error(t):
    print(f"Caracter no Valido: {t.value[0]!r} en posición {t.lexpos}")
    t.lexer.skip(1)


def mostrar_tokens(lexer):
    for tok in lexer:
        print(f"Token({tok.type}: {tok.value!r})")

def encriptar(texto:str) -> str:
    lexer.input(texto)
    salida = []
    
    for tok in lexer:
        if tok.type in ('MAYUSCULA', 'MINUSCULA', 'NUMEROS'):
            for c in tok.value:
                salida.append(ENC_MAP[c])
        elif tok.type == 'ESPACIOS':
            salida.append(ENC_MAP[tok.value])
        elif tok.type == 'SIMBOLOS':
            salida.append(ENC_MAP[tok.value])
        elif tok.type == 'NUEVALINEA':
            salida.append(ENC_MAP['\n'])
    return ''.join(salida)

def desencriptar(texto:str) -> str:
    salida = []
    for i in range(0, len(texto), 4):
        bloque = texto[i:i+4]
        salida.append(DEC_MAP[bloque])
    return ''.join(salida)

def leerArchivo(nombre_archivo:str) ->str:
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
    return contenido

def guardar_archivo(nombre_archivo:str, contenido:str) ->str:
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)

lexer = lex.lex()

# Leemos el archivo Original sin encriptar y lo mostramos
print("---------Texto Original---------")
archivo_original = "texto.txt"
data = leerArchivo(archivo_original)
print(data)

#Encriptamos y lo Guardamos en un archivo cualquiera
archivo_encriptado = "encriptado.txt"
guardar_archivo(archivo_encriptado, encriptar(data))

# leemos el archivo encriptado y lo mostramos
print("---------Texto Encriptado---------")
texto_encriptado = leerArchivo(archivo_encriptado)
print(f"{texto_encriptado}")

#Desencriptamos y lo guardamos en un archivo cualquiera
archivo_desencriptado = "desencriptado.txt"
guardar_archivo(archivo_desencriptado, desencriptar(texto_encriptado))

# Leemos el archivo desencriptado y lo mostramos
print("---------Texto Desencriptado---------")
texto_desencriptado = leerArchivo(archivo_desencriptado)
print(f"{texto_desencriptado}")
