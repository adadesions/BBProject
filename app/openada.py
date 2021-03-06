"""These are functions have written by AdaFactor"""
import os


def readimgfromlist(listfile):
    """Read each line of listfile"""
    profile_class = ["place", "food", "treatment", "facility", "room"]
    classifyer = ""
    for class_name in profile_class:
        if class_name in listfile:
            classifyer = class_name
            break

    project_dir = os.getcwd()
    path = "".join([project_dir, "/app/static/img/", listfile])
    f = open(path, "r")
    files = {}
    for line in f:
        cline = ("".join([project_dir, "/app/", line])).rstrip()
        if os.path.isfile(cline):
            files[line] = classifyer
        else:
            continue
    f.close()

    return files
