import ply.lex as lex
import ply.yacc as yacc

tokens = ['HASH','HEADER_FILE','FLOW_OPEN','FLOW_CLOSE','SEMI_COLON',
'TYPE','SMALL_OPEN','SMALL_CLOSE','IDENTIFIER','COLON',
'ASSIGNMENT_OP','UNARY_OP','BINARY_OP','NUM_LITERAL','RELATIONAL_OP','QUOTE']


reserved = {'include' : 'INCLUDE', 'main': 'MAIN','int':'INT','void':'VOID',
'float':'FLOAT','char':'CHAR','double':'DOUBLE','for':'FOR','switch':'SWITCH',
'case':'CASE','default':'DEFAULT','break':'BREAK','printf':'PRINT'}

tokens += reserved.values()

symbol_table = [] #For the time being, implemented as a list of dictionaries

#regex for the different tokens

t_HASH = r'\#'
t_HEADER_FILE = r'<stdio.h>' 
t_FLOW_OPEN = r'{'
t_FLOW_CLOSE = r'}'
t_SMALL_OPEN = r'\('
t_SMALL_CLOSE = r'\)'
t_SEMI_COLON = r';'
t_ASSIGNMENT_OP = r'\='
t_UNARY_OP = r'\++|\--'
#t_BINARY_OP = r'[\+\-\*\/]'
t_NUM_LITERAL = r'[0-9][0-9]*'
t_RELATIONAL_OP = r'\<|\>=|\>'
t_COLON =  r'\:'
t_QUOTE = r'\"'


def t_check_reserved(t):
	r'[a-zA-Z][a-zA-Z]*'
	if t.value in reserved: #If the matched lexeme is one of the reserved words
		t.type = reserved[t.value]
	else:
		t.type = 'IDENTIFIER'
	return t

def t_error(token):
	print(f'Illegal character: {token.value}')

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
#Building the parser

def p_expression(p):
	'''
	expression : header rest
	'''
	print('Derivation complete!')

def p_header(p):
	'''
	header : HASH INCLUDE HEADER_FILE
	'''
	print('Derived header')

def p_rest(p):
	'''
	rest : VOID MAIN SMALL_OPEN SMALL_CLOSE FLOW_OPEN stmt FLOW_CLOSE
		  
	'''
	print('Derived rest')


def p_stmt(p):
	'''
	stmt : for_stmt stmt
	      | switch_stmt stmt
	      | other_stmt stmt 
	      | empty
	'''
	print('Derived statement')

def p_other(p):
	'''
	other_stmt : print_stmt other_stmt 
				| empty
	'''
	print('Derived other statement')

def p_switch(p):
	'''
	switch_stmt : SWITCH SMALL_OPEN IDENTIFIER SMALL_CLOSE FLOW_OPEN switch_body FLOW_CLOSE 
	'''
	print('Derived switch')

def p_switch_body(p):
	'''
	switch_body : case_block switch_body
				| default_block
	'''
	print('Derived switch body')

def p_case(p):
	'''
	case_block : CASE NUM_LITERAL COLON FLOW_OPEN stmt BREAK SEMI_COLON FLOW_CLOSE
	'''

def p_default(p):
	'''
	default_block : DEFAULT COLON FLOW_OPEN stmt BREAK SEMI_COLON FLOW_CLOSE
	'''

def p_print(p):
	'''
	print_stmt : PRINT SMALL_OPEN QUOTE IDENTIFIER QUOTE SMALL_CLOSE SEMI_COLON
	'''

def p_for(p):
	'''
	for_stmt : FOR SMALL_OPEN init_exp SEMI_COLON conditional_exp SEMI_COLON update_exp SMALL_CLOSE FLOW_OPEN stmt FLOW_CLOSE
	'''
	print('Derived for')

def p_init_expression(p):
	'''
	init_exp :  type IDENTIFIER 
				| type IDENTIFIER ASSIGNMENT_OP NUM_LITERAL
				| empty
	''' 

def p_conditional_expression(p):
	'''
	conditional_exp :   IDENTIFIER RELATIONAL_OP NUM_LITERAL
						| IDENTIFIER RELATIONAL_OP IDENTIFIER
						| empty
	'''
def p_update_expression(p):
	'''
	update_exp : IDENTIFIER UNARY_OP
				| empty
	'''

def p_maintype(p):
	'''
	type : INT
		 | FLOAT
		 | CHAR
		 | DOUBLE
	'''

def p_empty(p):
	'empty :'


def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")


parser = yacc.yacc(method='LALR',debug=True)

with open(r'parsethis.txt','r') as file:
	'''while True:
		try:
			line = next(file)
			print('Parsing')
			parser.parse(line)
		except:
			print('Finished')
			break
	'''
	content = file.read()
	parser.parse(content)
print(f'Contents of the symbol table are: {symbol_table}')