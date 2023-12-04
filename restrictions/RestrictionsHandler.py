from z3 import *

def convertCommonEnrollmentsToPropositionalLogic(courseX, courseY, slots):
    if slots > 0:
        firstCourseInFirstSlot = Bool(f"x_{courseX}_1")
        secondCourseInFirstSlot = Bool(f"x_{courseY}_1")
        formula = Not(And(firstCourseInFirstSlot, secondCourseInFirstSlot))
        for slot in range(2, slots + 1):
            formula = And(formula, Not(And(Bool(f"x_{courseX}_{slot}"), Bool(f"x_{courseY}_{slot}"))))

        return formula

def atLeastInOneSlot(courseX, slots):
    if slots > 0:
        firstCourseInFirstSlot = Bool(f"x_{courseX}_1")
        formula = firstCourseInFirstSlot

        for slot in range(2, slots + 1):
            formula = Or(formula, Bool(f"x_{courseX}_{slot}"))

        return formula

def maxInOneSlot(courseX, slots):
    if slots > 0:
        for x in range(1, slots + 1):
            for y in range(x + 1, slots + 1):
                not_in_two_slots = Not(And(Bool(f"x_{courseX}_{x}"), Bool(f"x_{courseX}_{y}")))

                if x == 1 and y == 2:
                    formula = not_in_two_slots
                else:
                    formula = And(formula, Not(And(Bool(f"x_{courseX}_{x}"), Bool(f"x_{courseX}_{y}"))))

        return formula