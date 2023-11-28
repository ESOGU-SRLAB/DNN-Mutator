""" AST Mutator """
import ast
import random
import astunparse

# AST Value Mutator
class ConstantMutator(ast.NodeTransformer):
    """Node Traveller"""

    def __init__(self, mutation_name):
        self.mutation_name = mutation_name

    def visit_Constant(self, node):
        """The visitor function."""
        # value type control is for string or not
        # if type is string return node
        if not isinstance(node.value, str):
            # Need to pay attention for this section
            # if the type is not a string, it will mutate below
            if isinstance(node.value, bool):
                # Value mutator is for boolean type
                # if type is True return False
                # if type is False return True
                if node.value is True:
                    node.value = False
                    self.generic_visit(node)
                    return node
                node.value = True
                self.generic_visit(node)
                return node
            if self.mutation_name == "power":
                # Value mutator is for integer or double type
                node.value = exponent_of_two()
                return node
            elif self.mutation_name == "zero":
                # Value return 0
                node.value = 0
                return node
            elif self.mutation_name == "empty":
                # Value return 0
                node.value = ""
                return node
            elif self.mutation_name == "opposite":
                # Value return opposite number
                old_value = node.value
                node.value = old_value*-1
                return node
            elif self.mutation_name == "true_mutator":
                # Value return True
                node.value = True
                return node
            # Value return None
            node.value = None
            return node
        # if value is string, return empty value
        node.value = ""
        return node


def value_mutator(target_line, mutation_name):
    """Node Value Mutator"""
    node = ast.parse(target_line)
    renamer = ConstantMutator(mutation_name)
    new_node = renamer.visit(node)
    unparsed_code = astunparse.unparse(new_node)
    new_unparsed_code = unparsed_code.strip()
    if target_line != new_unparsed_code:
        print(new_unparsed_code)


def exponent_of_two():
    """retrun exponent of 2"""
    power = random.randint(1, 10)
    return pow(2, power)


# Mutant Types
# zero = return 0
# empty = return ''
# power = return exponent of two
# none = return None
# opposite = return 1 to -1
# true_mutator = return true_mutator

TARGET_LINE = "nn.Linear(28*28, 512)"
# TARGET_LINE = "yirmi_sekiz = 28"
# TARGET_LINE = "nn.Linear(yirmi_sekiz*yirmi_sekiz, sekiz)"

MUTATION_NAME = "opposite"
value_mutator(TARGET_LINE, MUTATION_NAME)