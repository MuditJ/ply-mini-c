#An approach to AST creation: create a set of data structures for different AST nodes corresponding to different unqiue parts of the 
#constructs being analyzed


class BinaryOperationNode: 
	'''For arithmetic and relational operations. Occur in for loops and can also occur in switch statements''' 
	def __init__(self,left,right,operator):
		self.left = left
		self.right = right
		self.operator = operator


class InitNode:
	def __init__(self,type_,identifier,operator,literal):
		self.type = type_
		self.identifier = identifier
		self.operator = operator
		self.literal = literal
		
class ForNode:
	def __init__(self,init,conditional,update,body):
		self.init = init
		self.conditional = conditional
		self.update = update
		self.body = body 