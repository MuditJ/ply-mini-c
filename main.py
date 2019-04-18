import token_rules
import lexerparser as p

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
	p.parser.parse(content,lexer = token_rules.lexer)
print(f'Contents of the symbol table are: {token_rules.symbol_table}')
print(f'Tokens generated are: {token_rules.tokens_generated}')


