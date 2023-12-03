from z3 import *

def turn_common_inscriptions_pair_minicourses_to_propositional_logic(cx, cy, slots):
    if slots > 0:
        firstCourseInFirstSlot = Bool(f"x_{cx}_1")
        secondCourseInFirstSlot = Bool(f"x_{cy}_1")
        formula = Not(And(firstCourseInFirstSlot, secondCourseInFirstSlot))
        for slot in range(2, slots + 1):
            formula = And(formula, Not(And(Bool(f"x_{cx}_{slot}"), Bool(f"x_{cy}_{slot}"))))

        return formula

def at_least_in_one_slot(cx, slots):
    if slots > 0:
        firstCourseInFirstSlot = Bool(f"x_{cx}_1")
        formula = firstCourseInFirstSlot

        for slot in range(2, slots + 1):
            formula = Or(formula, Bool(f"x_{cx}_{slot}"))

        return formula

def max_in_one_slot(cx, slots):
    if slots > 0:
        for x in range(1, slots + 1):
            for y in range(x + 1, slots + 1):
                not_in_two_slots = Not(And(Bool(f"x_{cx}_{x}"), Bool(f"x_{cx}_{y}")))

                if x == 1 and y == 2:
                    formula = not_in_two_slots
                else:
                    formula = And(formula, Not(And(Bool(f"x_{cx}_{x}"), Bool(f"x_{cx}_{y}"))))

        return formula