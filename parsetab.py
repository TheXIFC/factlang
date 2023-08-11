
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ELSE EQ_OP GE_OP ID IF LEFT_OP LE_OP NE_OP NUMBER POW RIGHT_OP WHILE\n    script : script_entity\n    | script script_entity\n    script_entity : statement\n    statement_list : statement\n    | statement_list statement\n    \n    compound_statement : '{' '}'\n    | '{' statement_list '}'\n    \n    primary_expression : value\n    unary_expression : primary_expression\n    exponential_expression : unary_expression\n    multiplicative_expression : exponential_expression\n    additive_expression : multiplicative_expression\n    shift_expression : additive_expression\n    relational_expression : shift_expression\n    equality_expression : relational_expression\n\n    assignment_expression : equality_expression\n    expression : assignment_expression\n    expression_statement : expression ';'\n    statement : expression_statement\n    statement : compound_statement\n    value : NUMBERvalue : IDprimary_expression : '(' expression ')'\n    unary_operator : '&'\n    | '*'\n    | '+'\n    | '-'\n    | '~'\n    | '!'\n    unary_expression : unary_operator primary_expressionexponential_expression : unary_expression POW exponential_expression\n    multiplicative_expression : multiplicative_expression '*' exponential_expression\n    | multiplicative_expression '/' exponential_expression\n    | multiplicative_expression '%' exponential_expression\n    \n    additive_expression : additive_expression '+' multiplicative_expression\n    | additive_expression '-' multiplicative_expression\n    \n    shift_expression : shift_expression LEFT_OP additive_expression\n    | shift_expression RIGHT_OP additive_expression\n    \n    relational_expression : relational_expression '<' shift_expression\n    | relational_expression '>' shift_expression\n    | relational_expression LE_OP shift_expression\n    | relational_expression GE_OP shift_expression\n    \n    equality_expression : equality_expression EQ_OP relational_expression\n    | equality_expression NE_OP relational_expression\n    assignment_operator : '='assignment_expression : ID assignment_operator assignment_expression\n    statement : IF '(' expression ')' statement\n    | IF '(' expression ')' statement ELSE statement\n    statement : WHILE '(' expression ')' statementempty :"
    
_lr_action_items = {'IF':([0,1,2,3,4,5,10,30,33,35,36,37,59,60,76,77,78,79,80,81,],[6,6,-1,-3,-19,-20,6,-2,-18,-6,6,-4,-7,-5,6,6,-47,-49,6,-48,]),'WHILE':([0,1,2,3,4,5,10,30,33,35,36,37,59,60,76,77,78,79,80,81,],[9,9,-1,-3,-19,-20,9,-2,-18,-6,9,-4,-7,-5,9,9,-47,-49,9,-48,]),'{':([0,1,2,3,4,5,10,30,33,35,36,37,59,60,76,77,78,79,80,81,],[10,10,-1,-3,-19,-20,10,-2,-18,-6,10,-4,-7,-5,10,10,-47,-49,10,-48,]),'ID':([0,1,2,3,4,5,7,10,18,19,21,24,26,27,28,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,59,60,76,77,78,79,80,81,],[13,13,-1,-3,-19,-20,13,13,-26,-27,-25,55,-24,-28,-29,-2,13,-18,13,-6,13,-4,55,55,13,-45,55,55,55,55,55,55,55,55,55,55,55,55,-7,-5,13,13,-47,-49,13,-48,]),'(':([0,1,2,3,4,5,6,7,9,10,18,19,21,24,26,27,28,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,59,60,76,77,78,79,80,81,],[7,7,-1,-3,-19,-20,31,7,34,7,-26,-27,-25,7,-24,-28,-29,-2,7,-18,7,-6,7,-4,7,7,7,-45,7,7,7,7,7,7,7,7,7,7,7,7,-7,-5,7,7,-47,-49,7,-48,]),'&':([0,1,2,3,4,5,7,10,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,59,60,76,77,78,79,80,81,],[26,26,-1,-3,-19,-20,26,26,-2,26,-18,26,-6,26,-4,26,26,26,-45,26,26,26,26,26,26,26,26,26,26,26,26,-7,-5,26,26,-47,-49,26,-48,]),'*':([0,1,2,3,4,5,7,10,13,17,20,22,23,25,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,60,70,71,72,73,74,75,76,77,78,79,80,81,],[21,21,-1,-3,-19,-20,21,21,-22,50,-11,-10,-9,-8,-21,-2,21,-18,21,-6,21,-4,21,21,21,-45,21,21,21,21,21,21,21,21,21,21,21,21,-30,-22,-23,-7,-5,50,50,-32,-33,-34,-31,21,21,-47,-49,21,-48,]),'+':([0,1,2,3,4,5,7,10,13,16,17,20,22,23,25,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,60,68,69,70,71,72,73,74,75,76,77,78,79,80,81,],[18,18,-1,-3,-19,-20,18,18,-22,48,-12,-11,-10,-9,-8,-21,-2,18,-18,18,-6,18,-4,18,18,18,-45,18,18,18,18,18,18,18,18,18,18,18,18,-30,-22,-23,-7,-5,48,48,-35,-36,-32,-33,-34,-31,18,18,-47,-49,18,-48,]),'-':([0,1,2,3,4,5,7,10,13,16,17,20,22,23,25,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,60,68,69,70,71,72,73,74,75,76,77,78,79,80,81,],[19,19,-1,-3,-19,-20,19,19,-22,49,-12,-11,-10,-9,-8,-21,-2,19,-18,19,-6,19,-4,19,19,19,-45,19,19,19,19,19,19,19,19,19,19,19,19,-30,-22,-23,-7,-5,49,49,-35,-36,-32,-33,-34,-31,19,19,-47,-49,19,-48,]),'~':([0,1,2,3,4,5,7,10,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,59,60,76,77,78,79,80,81,],[27,27,-1,-3,-19,-20,27,27,-2,27,-18,27,-6,27,-4,27,27,27,-45,27,27,27,27,27,27,27,27,27,27,27,27,-7,-5,27,27,-47,-49,27,-48,]),'!':([0,1,2,3,4,5,7,10,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,59,60,76,77,78,79,80,81,],[28,28,-1,-3,-19,-20,28,28,-2,28,-18,28,-6,28,-4,28,28,28,-45,28,28,28,28,28,28,28,28,28,28,28,28,-7,-5,28,28,-47,-49,28,-48,]),'NUMBER':([0,1,2,3,4,5,7,10,18,19,21,24,26,27,28,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,59,60,76,77,78,79,80,81,],[29,29,-1,-3,-19,-20,29,29,-26,-27,-25,29,-24,-28,-29,-2,29,-18,29,-6,29,-4,29,29,29,-45,29,29,29,29,29,29,29,29,29,29,29,29,-7,-5,29,29,-47,-49,29,-48,]),'$end':([1,2,3,4,5,30,33,35,59,78,79,81,],[0,-1,-3,-19,-20,-2,-18,-6,-7,-47,-49,-48,]),'}':([4,5,10,33,35,36,37,59,60,78,79,81,],[-19,-20,35,-18,-6,59,-4,-7,-5,-47,-49,-48,]),'ELSE':([4,5,33,35,59,78,79,81,],[-19,-20,-18,-6,-7,80,-49,-48,]),';':([8,11,12,13,14,15,16,17,20,22,23,25,29,54,55,57,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[33,-17,-16,-22,-15,-14,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,-43,-44,-46,-39,-40,-41,-42,-37,-38,-35,-36,-32,-33,-34,-31,]),')':([11,12,13,14,15,16,17,20,22,23,25,29,32,54,55,56,57,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-17,-16,-22,-15,-14,-13,-12,-11,-10,-9,-8,-21,57,-30,-22,76,-23,77,-43,-44,-46,-39,-40,-41,-42,-37,-38,-35,-36,-32,-33,-34,-31,]),'EQ_OP':([12,13,14,15,16,17,20,22,23,25,29,54,55,57,61,62,64,65,66,67,68,69,70,71,72,73,74,75,],[38,-22,-15,-14,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,-43,-44,-39,-40,-41,-42,-37,-38,-35,-36,-32,-33,-34,-31,]),'NE_OP':([12,13,14,15,16,17,20,22,23,25,29,54,55,57,61,62,64,65,66,67,68,69,70,71,72,73,74,75,],[39,-22,-15,-14,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,-43,-44,-39,-40,-41,-42,-37,-38,-35,-36,-32,-33,-34,-31,]),'POW':([13,22,23,25,29,54,55,57,],[-22,53,-9,-8,-21,-30,-22,-23,]),'/':([13,17,20,22,23,25,29,54,55,57,70,71,72,73,74,75,],[-22,51,-11,-10,-9,-8,-21,-30,-22,-23,51,51,-32,-33,-34,-31,]),'%':([13,17,20,22,23,25,29,54,55,57,70,71,72,73,74,75,],[-22,52,-11,-10,-9,-8,-21,-30,-22,-23,52,52,-32,-33,-34,-31,]),'LEFT_OP':([13,15,16,17,20,22,23,25,29,54,55,57,64,65,66,67,68,69,70,71,72,73,74,75,],[-22,46,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,46,46,46,46,-37,-38,-35,-36,-32,-33,-34,-31,]),'RIGHT_OP':([13,15,16,17,20,22,23,25,29,54,55,57,64,65,66,67,68,69,70,71,72,73,74,75,],[-22,47,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,47,47,47,47,-37,-38,-35,-36,-32,-33,-34,-31,]),'<':([13,14,15,16,17,20,22,23,25,29,54,55,57,61,62,64,65,66,67,68,69,70,71,72,73,74,75,],[-22,42,-14,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,42,42,-39,-40,-41,-42,-37,-38,-35,-36,-32,-33,-34,-31,]),'>':([13,14,15,16,17,20,22,23,25,29,54,55,57,61,62,64,65,66,67,68,69,70,71,72,73,74,75,],[-22,43,-14,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,43,43,-39,-40,-41,-42,-37,-38,-35,-36,-32,-33,-34,-31,]),'LE_OP':([13,14,15,16,17,20,22,23,25,29,54,55,57,61,62,64,65,66,67,68,69,70,71,72,73,74,75,],[-22,44,-14,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,44,44,-39,-40,-41,-42,-37,-38,-35,-36,-32,-33,-34,-31,]),'GE_OP':([13,14,15,16,17,20,22,23,25,29,54,55,57,61,62,64,65,66,67,68,69,70,71,72,73,74,75,],[-22,45,-14,-13,-12,-11,-10,-9,-8,-21,-30,-22,-23,45,45,-39,-40,-41,-42,-37,-38,-35,-36,-32,-33,-34,-31,]),'=':([13,],[41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'script':([0,],[1,]),'script_entity':([0,1,],[2,30,]),'statement':([0,1,10,36,76,77,80,],[3,3,37,60,78,79,81,]),'expression_statement':([0,1,10,36,76,77,80,],[4,4,4,4,4,4,4,]),'compound_statement':([0,1,10,36,76,77,80,],[5,5,5,5,5,5,5,]),'expression':([0,1,7,10,31,34,36,76,77,80,],[8,8,32,8,56,58,8,8,8,8,]),'assignment_expression':([0,1,7,10,31,34,36,40,76,77,80,],[11,11,11,11,11,11,11,63,11,11,11,]),'equality_expression':([0,1,7,10,31,34,36,40,76,77,80,],[12,12,12,12,12,12,12,12,12,12,12,]),'relational_expression':([0,1,7,10,31,34,36,38,39,40,76,77,80,],[14,14,14,14,14,14,14,61,62,14,14,14,14,]),'shift_expression':([0,1,7,10,31,34,36,38,39,40,42,43,44,45,76,77,80,],[15,15,15,15,15,15,15,15,15,15,64,65,66,67,15,15,15,]),'additive_expression':([0,1,7,10,31,34,36,38,39,40,42,43,44,45,46,47,76,77,80,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,68,69,16,16,16,]),'multiplicative_expression':([0,1,7,10,31,34,36,38,39,40,42,43,44,45,46,47,48,49,76,77,80,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,70,71,17,17,17,]),'exponential_expression':([0,1,7,10,31,34,36,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,76,77,80,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,72,73,74,75,20,20,20,]),'unary_expression':([0,1,7,10,31,34,36,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,76,77,80,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'primary_expression':([0,1,7,10,24,31,34,36,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,76,77,80,],[23,23,23,23,54,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'unary_operator':([0,1,7,10,31,34,36,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,76,77,80,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'value':([0,1,7,10,24,31,34,36,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,76,77,80,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'statement_list':([10,],[36,]),'assignment_operator':([13,],[40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> script","S'",1,None,None,None),
  ('script -> script_entity','script',1,'p_script','grammar.py',33),
  ('script -> script script_entity','script',2,'p_script','grammar.py',34),
  ('script_entity -> statement','script_entity',1,'p_script_entity','grammar.py',44),
  ('statement_list -> statement','statement_list',1,'p_statement_list','grammar.py',50),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','grammar.py',51),
  ('compound_statement -> { }','compound_statement',2,'p_compound_statement','grammar.py',63),
  ('compound_statement -> { statement_list }','compound_statement',3,'p_compound_statement','grammar.py',64),
  ('primary_expression -> value','primary_expression',1,'p_unit_exp','grammar.py',74),
  ('unary_expression -> primary_expression','unary_expression',1,'p_unit_exp','grammar.py',75),
  ('exponential_expression -> unary_expression','exponential_expression',1,'p_unit_exp','grammar.py',76),
  ('multiplicative_expression -> exponential_expression','multiplicative_expression',1,'p_unit_exp','grammar.py',77),
  ('additive_expression -> multiplicative_expression','additive_expression',1,'p_unit_exp','grammar.py',78),
  ('shift_expression -> additive_expression','shift_expression',1,'p_unit_exp','grammar.py',79),
  ('relational_expression -> shift_expression','relational_expression',1,'p_unit_exp','grammar.py',80),
  ('equality_expression -> relational_expression','equality_expression',1,'p_unit_exp','grammar.py',81),
  ('assignment_expression -> equality_expression','assignment_expression',1,'p_unit_exp','grammar.py',83),
  ('expression -> assignment_expression','expression',1,'p_unit_exp','grammar.py',84),
  ('expression_statement -> expression ;','expression_statement',2,'p_unit_exp','grammar.py',85),
  ('statement -> expression_statement','statement',1,'p_unit_exp','grammar.py',86),
  ('statement -> compound_statement','statement',1,'p_unit_exp','grammar.py',87),
  ('value -> NUMBER','value',1,'p_expression_num','grammar.py',93),
  ('value -> ID','value',1,'p_expression_id','grammar.py',98),
  ('primary_expression -> ( expression )','primary_expression',3,'p_primary_exp','grammar.py',103),
  ('unary_operator -> &','unary_operator',1,'p_unary_op','grammar.py',109),
  ('unary_operator -> *','unary_operator',1,'p_unary_op','grammar.py',110),
  ('unary_operator -> +','unary_operator',1,'p_unary_op','grammar.py',111),
  ('unary_operator -> -','unary_operator',1,'p_unary_op','grammar.py',112),
  ('unary_operator -> ~','unary_operator',1,'p_unary_op','grammar.py',113),
  ('unary_operator -> !','unary_operator',1,'p_unary_op','grammar.py',114),
  ('unary_expression -> unary_operator primary_expression','unary_expression',2,'p_unary_exp','grammar.py',120),
  ('exponential_expression -> unary_expression POW exponential_expression','exponential_expression',3,'p_exponential_exp','grammar.py',125),
  ('multiplicative_expression -> multiplicative_expression * exponential_expression','multiplicative_expression',3,'p_multiplicative_exp','grammar.py',131),
  ('multiplicative_expression -> multiplicative_expression / exponential_expression','multiplicative_expression',3,'p_multiplicative_exp','grammar.py',132),
  ('multiplicative_expression -> multiplicative_expression % exponential_expression','multiplicative_expression',3,'p_multiplicative_exp','grammar.py',133),
  ('additive_expression -> additive_expression + multiplicative_expression','additive_expression',3,'p_additive_exp','grammar.py',140),
  ('additive_expression -> additive_expression - multiplicative_expression','additive_expression',3,'p_additive_exp','grammar.py',141),
  ('shift_expression -> shift_expression LEFT_OP additive_expression','shift_expression',3,'p_shift_exp','grammar.py',148),
  ('shift_expression -> shift_expression RIGHT_OP additive_expression','shift_expression',3,'p_shift_exp','grammar.py',149),
  ('relational_expression -> relational_expression < shift_expression','relational_expression',3,'p_relational_exp','grammar.py',156),
  ('relational_expression -> relational_expression > shift_expression','relational_expression',3,'p_relational_exp','grammar.py',157),
  ('relational_expression -> relational_expression LE_OP shift_expression','relational_expression',3,'p_relational_exp','grammar.py',158),
  ('relational_expression -> relational_expression GE_OP shift_expression','relational_expression',3,'p_relational_exp','grammar.py',159),
  ('equality_expression -> equality_expression EQ_OP relational_expression','equality_expression',3,'p_equality_exp','grammar.py',166),
  ('equality_expression -> equality_expression NE_OP relational_expression','equality_expression',3,'p_equality_exp','grammar.py',167),
  ('assignment_operator -> =','assignment_operator',1,'p_assignment_op','grammar.py',173),
  ('assignment_expression -> ID assignment_operator assignment_expression','assignment_expression',3,'p_assignment_exp','grammar.py',188),
  ('statement -> IF ( expression ) statement','statement',5,'p_if_statement','grammar.py',194),
  ('statement -> IF ( expression ) statement ELSE statement','statement',7,'p_if_statement','grammar.py',195),
  ('statement -> WHILE ( expression ) statement','statement',5,'p_while_statement','grammar.py',203),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',208),
]
