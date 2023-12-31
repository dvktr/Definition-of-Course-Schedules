def openArchive(archive_name):
    with open(f"inputs/{archive_name}", "r") as archive:
        lines = archive.readlines()
    return lines

def getCourses(archive_name):
    lines = openArchive(archive_name)

    courses = []
    for line in lines:
        if line.startswith('# Minicursos'):
            continue
        if line.startswith('#'):
            break
        courses.append(line.split(' ')[1].rstrip('\n'))

    qtd_courses = len(courses)

    minicourses = {}
    for x in range(0, qtd_courses):
        minicourses[x + 1] = courses[x]

    return minicourses

def getPairs(archive_name):
    lines = openArchive(archive_name)

    courses = []
    
    found_pairs = False

    for line in lines:
        if found_pairs:
            minicourse1, minicourse2 = line.split(' ')[:2]
            courses.append((int(minicourse1), int(minicourse2)))
        elif line.startswith('# Pares de minicursos com inscriÃ§Ãµes em comum:'):
            found_pairs = True
   
    return courses 

def getSlots(archive_name):
    lines = openArchive(archive_name)
        
    for line in lines:
        if line.startswith('# Minicursos'):
            continue
        
        if 'Slots' in line:
            num = line.split()
            slot = int(num[2])

    return slot