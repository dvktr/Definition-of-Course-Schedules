from z3 import *

def turn_common_inscriptions_pair_minicourses_to_propositional_logic(cx, cy, slots):
    if slots > 0:
        firstCourseInFirstSlot = Bool(f"x_{cx}_1")
        secondCourseInFirstSlot = Bool(f"x_{cy}_1")
        formula = Not(And(firstCourseInFirstSlot, secondCourseInFirstSlot))
        for slot in range(2, slots + 1):
            formula = And(formula, Not(And(Bool(f"x_{cx}_{slot}"), Bool(f"x_{cy}_{slot}"))))

        return formula

