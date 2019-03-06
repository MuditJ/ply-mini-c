
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGNMENT_OP BINARY_OP BREAK CASE CHAR COLON DEFAULT DOUBLE FLOAT FLOW_CLOSE FLOW_OPEN FOR HASH HEADER_FILE IDENTIFIER INCLUDE INT MAIN NUM_LITERAL PRINT QUOTE RELATIONAL_OP SEMI_COLON SMALL_CLOSE SMALL_OPEN SWITCH TYPE UNARY_OP VOID\n\texpression : header rest\n\t\n\theader : HASH INCLUDE HEADER_FILE\n\t\n\trest : VOID MAIN SMALL_OPEN SMALL_CLOSE FLOW_OPEN stmt FLOW_CLOSE\n\t\t  \n\t\n\tstmt : for_stmt stmt\n\t      | switch_stmt stmt\n\t      | other_stmt stmt \n\t      | empty\n\t\n\tother_stmt : print_stmt other_stmt \n\t\t\t\t| empty\n\t\n\tswitch_stmt : SWITCH SMALL_OPEN IDENTIFIER SMALL_CLOSE FLOW_OPEN switch_body FLOW_CLOSE \n\t\n\tswitch_body : case_block switch_body\n\t\t\t\t| default_block\n\t\n\tcase_block : CASE NUM_LITERAL COLON FLOW_OPEN stmt BREAK SEMI_COLON FLOW_CLOSE\n\t\n\tdefault_block : DEFAULT COLON FLOW_OPEN stmt BREAK SEMI_COLON FLOW_CLOSE\n\t\n\tprint_stmt : PRINT SMALL_OPEN QUOTE IDENTIFIER QUOTE SMALL_CLOSE SEMI_COLON\n\t\n\tfor_stmt : FOR SMALL_OPEN init_exp SEMI_COLON conditional_exp SEMI_COLON update_exp SMALL_CLOSE FLOW_OPEN stmt FLOW_CLOSE\n\t\n\tinit_exp :  type IDENTIFIER \n\t\t\t\t| type IDENTIFIER ASSIGNMENT_OP NUM_LITERAL\n\t\t\t\t| empty\n\t\n\tconditional_exp :   IDENTIFIER RELATIONAL_OP NUM_LITERAL\n\t\t\t\t\t\t| IDENTIFIER RELATIONAL_OP IDENTIFIER\n\t\t\t\t\t\t| empty\n\t\n\tupdate_exp : IDENTIFIER UNARY_OP\n\t\t\t\t| empty\n\t\n\ttype : INT\n\t\t | FLOAT\n\t\t | CHAR\n\t\t | DOUBLE\n\tempty :'
    
_lr_action_items = {'HASH':([0,],[3,]),'$end':([1,4,21,],[0,-1,-3,]),'VOID':([2,8,],[5,-2,]),'INCLUDE':([3,],[6,]),'MAIN':([5,],[7,]),'HEADER_FILE':([6,],[8,]),'SMALL_OPEN':([7,17,18,20,],[9,25,26,29,]),'SMALL_CLOSE':([9,37,48,49,58,60,69,],[10,41,57,-29,68,-24,-23,]),'FLOW_OPEN':([10,41,66,68,70,],[11,47,71,72,73,]),'FOR':([11,13,14,15,16,19,27,28,63,67,71,72,73,78,],[17,17,17,17,-9,-29,-8,-9,-10,-15,17,17,17,-16,]),'SWITCH':([11,13,14,15,16,19,27,28,63,67,71,72,73,78,],[18,18,18,18,-9,-29,-8,-9,-10,-15,18,18,18,-16,]),'FLOW_CLOSE':([11,12,13,14,15,16,19,22,23,24,27,28,52,54,63,64,67,72,75,78,80,81,82,],[-29,21,-29,-29,-29,-7,-29,-4,-5,-6,-8,-9,63,-12,-10,-11,-15,-29,78,-16,82,83,-14,]),'PRINT':([11,13,14,15,16,19,27,28,63,67,71,72,73,78,],[20,20,20,20,-9,20,-8,-9,-10,-15,20,20,20,-16,]),'BREAK':([13,14,15,16,19,22,23,24,27,28,63,67,71,73,74,76,78,],[-29,-29,-29,-7,-29,-4,-5,-6,-8,-9,-10,-15,-29,-29,77,79,-16,]),'INT':([25,],[33,]),'FLOAT':([25,],[34,]),'CHAR':([25,],[35,]),'DOUBLE':([25,],[36,]),'SEMI_COLON':([25,30,32,39,40,43,45,51,57,61,62,77,79,],[-29,39,-19,-29,-17,49,-22,-18,67,-21,-20,80,81,]),'IDENTIFIER':([26,31,33,34,35,36,38,39,49,50,],[37,40,-25,-26,-27,-28,42,44,59,61,]),'QUOTE':([29,42,],[38,48,]),'ASSIGNMENT_OP':([40,],[46,]),'RELATIONAL_OP':([44,],[50,]),'NUM_LITERAL':([46,50,55,],[51,62,65,]),'CASE':([47,53,83,],[55,55,-13,]),'DEFAULT':([47,53,83,],[56,56,-13,]),'COLON':([56,65,],[66,70,]),'UNARY_OP':([59,],[69,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'header':([0,],[2,]),'rest':([2,],[4,]),'stmt':([11,13,14,15,71,72,73,],[12,22,23,24,74,75,76,]),'for_stmt':([11,13,14,15,71,72,73,],[13,13,13,13,13,13,13,]),'switch_stmt':([11,13,14,15,71,72,73,],[14,14,14,14,14,14,14,]),'other_stmt':([11,13,14,15,19,71,72,73,],[15,15,15,15,27,15,15,15,]),'empty':([11,13,14,15,19,25,39,49,71,72,73,],[16,16,16,16,28,32,45,60,16,16,16,]),'print_stmt':([11,13,14,15,19,71,72,73,],[19,19,19,19,19,19,19,19,]),'init_exp':([25,],[30,]),'type':([25,],[31,]),'conditional_exp':([39,],[43,]),'switch_body':([47,53,],[52,64,]),'case_block':([47,53,],[53,53,]),'default_block':([47,53,],[54,54,]),'update_exp':([49,],[58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> header rest','expression',2,'p_expression','fs.py',61),
  ('header -> HASH INCLUDE HEADER_FILE','header',3,'p_header','fs.py',67),
  ('rest -> VOID MAIN SMALL_OPEN SMALL_CLOSE FLOW_OPEN stmt FLOW_CLOSE','rest',7,'p_rest','fs.py',73),
  ('stmt -> for_stmt stmt','stmt',2,'p_stmt','fs.py',81),
  ('stmt -> switch_stmt stmt','stmt',2,'p_stmt','fs.py',82),
  ('stmt -> other_stmt stmt','stmt',2,'p_stmt','fs.py',83),
  ('stmt -> empty','stmt',1,'p_stmt','fs.py',84),
  ('other_stmt -> print_stmt other_stmt','other_stmt',2,'p_other','fs.py',90),
  ('other_stmt -> empty','other_stmt',1,'p_other','fs.py',91),
  ('switch_stmt -> SWITCH SMALL_OPEN IDENTIFIER SMALL_CLOSE FLOW_OPEN switch_body FLOW_CLOSE','switch_stmt',7,'p_switch','fs.py',97),
  ('switch_body -> case_block switch_body','switch_body',2,'p_switch_body','fs.py',103),
  ('switch_body -> default_block','switch_body',1,'p_switch_body','fs.py',104),
  ('case_block -> CASE NUM_LITERAL COLON FLOW_OPEN stmt BREAK SEMI_COLON FLOW_CLOSE','case_block',8,'p_case','fs.py',110),
  ('default_block -> DEFAULT COLON FLOW_OPEN stmt BREAK SEMI_COLON FLOW_CLOSE','default_block',7,'p_default','fs.py',115),
  ('print_stmt -> PRINT SMALL_OPEN QUOTE IDENTIFIER QUOTE SMALL_CLOSE SEMI_COLON','print_stmt',7,'p_print','fs.py',120),
  ('for_stmt -> FOR SMALL_OPEN init_exp SEMI_COLON conditional_exp SEMI_COLON update_exp SMALL_CLOSE FLOW_OPEN stmt FLOW_CLOSE','for_stmt',11,'p_for','fs.py',125),
  ('init_exp -> type IDENTIFIER','init_exp',2,'p_init_expression','fs.py',131),
  ('init_exp -> type IDENTIFIER ASSIGNMENT_OP NUM_LITERAL','init_exp',4,'p_init_expression','fs.py',132),
  ('init_exp -> empty','init_exp',1,'p_init_expression','fs.py',133),
  ('conditional_exp -> IDENTIFIER RELATIONAL_OP NUM_LITERAL','conditional_exp',3,'p_conditional_expression','fs.py',138),
  ('conditional_exp -> IDENTIFIER RELATIONAL_OP IDENTIFIER','conditional_exp',3,'p_conditional_expression','fs.py',139),
  ('conditional_exp -> empty','conditional_exp',1,'p_conditional_expression','fs.py',140),
  ('update_exp -> IDENTIFIER UNARY_OP','update_exp',2,'p_update_expression','fs.py',144),
  ('update_exp -> empty','update_exp',1,'p_update_expression','fs.py',145),
  ('type -> INT','type',1,'p_maintype','fs.py',150),
  ('type -> FLOAT','type',1,'p_maintype','fs.py',151),
  ('type -> CHAR','type',1,'p_maintype','fs.py',152),
  ('type -> DOUBLE','type',1,'p_maintype','fs.py',153),
  ('empty -> <empty>','empty',0,'p_empty','fs.py',157),
]