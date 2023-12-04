def openArchive(archive_name):
    with open(f"inputs/{archive_name}", "r") as archive:
        lines = archive.readlines()
    return lines