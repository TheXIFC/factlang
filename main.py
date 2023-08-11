import pyperclip as pyperclip

import grammar as gr
import blueprint_creation as bc
from node_parse import parse_node
from scope import Scope

f = open("script.fact", "r", encoding='utf-8')
data = f.read()

result = gr.get_AST(data)

command_list = []
scope = Scope()
parse_node(result, command_list, scope, 'gs', {})

# TODO command optimization goes here

bc.global_scope_start = 1
blueprint = bc.create_blueprint(command_list)
print(blueprint)
pyperclip.copy(blueprint)

print(f"Global scope size {len(scope.gs.stack)}")
print(f"Local scope size {len(scope.ls.stack)}")
