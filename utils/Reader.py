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