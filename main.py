from z3 import *
from utils.CourseInformationReader import *
from restrictions.RestrictionsHandler import *

archive_name = "input.txt"
slots = getSlots(archive_name)
courses = getCourses(archive_name)
common_inscriptions_courses = getPairs(archive_name)

common_inscriptions_courses_restrictions = None

for course_pair in common_inscriptions_courses:
    if course_pair == common_inscriptions_courses[0]:
        common_inscriptions_courses_restrictions = convertCommonEnrollmentsToPropositionalLogic(course_pair[0], course_pair[1], slots)
    else:
        common_inscriptions_courses_restrictions = And(common_inscriptions_courses_restrictions, convertCommonEnrollmentsToPropositionalLogic(course_pair[0], course_pair[1], slots))

solver = Solver()

at_least_in_one_slot_restrictions = None
max_in_one_slot_restrictions = None

for course_number in range(1, len(courses) + 1):
    if course_number == 1:
        at_least_in_one_slot_restrictions = atLeastInOneSlot(course_number, slots)
        max_in_one_slot_restrictions = maxInOneSlot(course_number, slots)
    else:
        at_least_in_one_slot_restrictions = And(at_least_in_one_slot_restrictions, atLeastInOneSlot(course_number, slots))
        max_in_one_slot_restrictions = And(max_in_one_slot_restrictions, maxInOneSlot(course_number, slots))

all_restrictions = And(And(max_in_one_slot_restrictions, at_least_in_one_slot_restrictions), common_inscriptions_courses_restrictions)

solver.add(all_restrictions)

isSatisfatible = solver.check() == sat and slots > 0

if isSatisfatible:
    model = solver.model()

    truly_course_variables = []

    for variable in model:
        if model[variable]:
            truly_course_variables.append(str(variable))

    for course_variable in truly_course_variables:
        splitted_course_variable = course_variable.split("_")
        course_number = int(splitted_course_variable[1])
        slot_number = int(splitted_course_variable[2])
        course_name = courses[course_number]

        print(f"O curso {course_name}", end=' ')
        print(f'ficará no slot de horário {slot_number}\n')
else:
    print("É impossível organizar os cursos com a quantidade de slots e restrições fornecidas.")
