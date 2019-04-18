#Implements the symbol table required to store details of the tokens/lexemes encountered by the parser, used in semantic analysis


class SymbolTable:
	


class Symbol:
	def __init__(self,type_,value,position,line):
		self.type = type_
		self.value = value
		self.position = position
		self.line = line


class Keyword(Symbol):
	pass

class Identifier(Symbol): 
	def __init__(self,type_,value,position,line,scope):
		self.scope = scope
		super().__init__(type_,value,position,line)

class Constant(Symbol):
	pass