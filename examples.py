from . import LSystem, back_to_saved_state, leo, save_current_state

SIERPINSKI_TRIANGLE_STEP = 8
SIERPINSKI_TRIANGLE_ANGLE = 120
SIERPINSKI_TRIANGLE_AXIOM = "F"
SIERPINSKI_TRIANGLE_RULES = {"F": "F-G+F+G-F",
                             "G": "GG"}
SIERPINSKI_TRIANGLE_ACTIONS = {"F": lambda: leo.forward(SIERPINSKI_TRIANGLE_STEP), 
                               "G": lambda: leo.forward(SIERPINSKI_TRIANGLE_STEP),
                               "+": lambda: leo.right(SIERPINSKI_TRIANGLE_ANGLE),
                               "-": lambda: leo.left(SIERPINSKI_TRIANGLE_ANGLE)}

SIERPINSKI_TRIANGLE_LSYSTEM = LSystem(SIERPINSKI_TRIANGLE_AXIOM, SIERPINSKI_TRIANGLE_RULES, SIERPINSKI_TRIANGLE_ACTIONS)

SIMPLE_TREE_STEP = 7
SIMPLE_TREE_ANGLE = 22.5
SIMPLE_TREE_AXIOM = "X"
SIMPLE_TREE_RULES = {"X": "F[+X]F[-X]+X", "F": "FF"}
SIMPLE_TREE_ACTIONS = {"F": lambda: leo.forward(SIERPINSKI_TRIANGLE_STEP), 
                       "+": lambda: leo.right(SIMPLE_TREE_ANGLE),
                       "-": lambda: leo.left(SIMPLE_TREE_ANGLE),
                       "[": lambda: save_current_state(leo),
                       "]": lambda: back_to_saved_state(leo)}

SIMPLE_TREE_LSYSTEM = LSystem(SIMPLE_TREE_AXIOM, SIMPLE_TREE_RULES, SIMPLE_TREE_ACTIONS)
