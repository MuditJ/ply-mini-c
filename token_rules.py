import ply.lex as lex

tokens = ['HASH','HEADER_FILE','FLOW_OPEN','FLOW_CLOSE','SEMI_COLON',
'TYPE','SMALL_OPEN','SMALL_CLOSE','IDENTIFIER','COLON',
'ASSIGNMENT_OP','UNARY_OP','BINARY_OP','NUM_LITERAL','RELATIONAL_OP','QUOTE','STRING_LITERAL']


reserved = {'include' : 'INCLUDE', 'main': 'MAIN','int':'INT','void':'VOID',
'float':'FLOAT','char':'CHAR','double':'DOUBLE','for':'FOR','switch':'SWITCH',
'case':'CASE','default':'DEFAULT','break':'BREAK','printf':'PRINT'}


tokens += reserved.values()

symbol_table = [] #For the time being, implemented as a list of dictionaries
tokens_generated = [] #To store the tokens found in the input program
#regex for the different tokens. Store as a list of dictionaries where the token is the key and its (type,value) the value

t_HASH = r'\#'
t_HEADER_FILE = r'<stdio.h>' 
t_SMALL_OPEN = r'\('
t_SMALL_CLOSE = r'\)'
t_SEMI_COLON = r';'
t_ASSIGNMENT_OP = r'\='
t_UNARY_OP = r'\++|\--'
#t_BINARY_OP = r'[\+\-\*\/]'

t_RELATIONAL_OP = r'\<|\>=|\>'
t_COLON =  r'\:'
t_QUOTE = r'\"'


def t_FLOW_OPEN(t):
	r'{'
	symbol_table.append([])
	return t


def t_FLOW_CLOSE(t):
	r'}'
	symbol_table.pop()
	return t

def t_NUM_LITERAL(t):
	r'[0-9][0-9]*'
	t.value = int(t.value)
	return t


def t_STRING_LITERAL(t):
	r'\"[a-zA-Z]+\"'
	return t


def t_check_reserved(t):
	r'[a-zA-Z][a-zA-Z]*'
	if t.value in reserved: #If the matched lexeme is one of the reserved words
		t.type = reserved[t.value]
	else:
		t.type = 'IDENTIFIER'
		if len(t.value) > 31:
			print(f'''Line {t.lexer.lineno}. The identifier name {t.value} is greater than 31 characters and hence too long.
	 It will be truncated to return the first 31 characters''')
			t.value = t.value[:30]
		if (t.value,t.type) not in symbol_table:
			symbol_table[-1].append((t.value,t.type))
		tokens_generated.append((t.type,t.value))
	return t


def t_error(token):
	print(f'Illegal character: {token.value} on line number {t.lineno}')
	token.lexer.skip(1)

def t_whitespace(t):
	r'\s+'
	pass

def t_COMMENT(t):
	r'(\/\/\/.*)|(\/\/\!.*)|(\/\/.*)|(\/\*[.\n]*.*\*\/)'
	pass


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)



lexer = lex.lex()
