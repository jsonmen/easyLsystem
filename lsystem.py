from typing import Callable, Dict

class LSystem:
    def __init__(self, axiom: str, rules: Dict[str, str], action_on_char: Dict[str, Callable]):
        self.axiom = axiom
        self.rules = rules
        self.action_on_char = action_on_char
        
    def apply_rules(self):
        result = ""
        for char in self.axiom:
            if char in self.rules:
                result += self.rules[char]
            else:
                result += char 
        self.axiom = result
    
    def apply_rules_to_axiom(self, axiom: str) -> str:
        result = ""
        for char in axiom:
            if char in self.rules:
                result += self.rules[char]
            else:
                result += char
        return result
    
    def make_generation(self, generation_num: int):
        for _ in range(generation_num):
            self.apply_rules()
            
    def get_result_at_axiom_on_generation(self, axiom: str, generation_num: int) -> str:
        result = axiom
        for _ in range(generation_num):
            result = self.apply_rules_to_axiom(result)

        return result
    def draw(self):
        for char in self.axiom:
            if char in self.action_on_char:
                self.action_on_char[char]() 

