import ply.yacc as yacc


#Building the lexer
from token_rules import tokens,symbol_table,tokens_generated


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
	print(f'Symbol table currently is: {symbol_table}')

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
	if len(p) == 2:
		print(f'Symbol table currently is:{symbol_table}')

def p_other(p):
	'''
	other_stmt : print_stmt other_stmt 
				| arithmetic_stmt other_stmt
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
	print_stmt : PRINT SMALL_OPEN STRING_LITERAL SMALL_CLOSE SEMI_COLON
	'''
def p_arithmetic(p):
	'''
	arithmetic_stmt : NUM_LITERAL BINARY_OP rest_arithmetic
	'''

def p_rest_arithemtic(p):
	'''
	rest_arithmetic : arithmetic_stmt 
					 | NUM_LITERAL

	'''
def p_for(p):
	'''
	for_stmt : FOR SMALL_OPEN init_exp SEMI_COLON conditional_exp SEMI_COLON update_exp SMALL_CLOSE FLOW_OPEN stmt FLOW_CLOSE
	'''
	print('Derived for')

def p_init_expression(p):
	'''
	init_exp :  type IDENTIFIER empty
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


