from pyscript import document, display

# CLASS DEF
class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject


# LIST
classmates = []


def addClassmate(e):
    name = document.getElementById("urname").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value


    classmate = Classmate(name, section, subject)
    classmates.append(classmate)

    document.getElementById("urname").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""


def showList(e):
    output = "My name is Mauri from Ruby. My favorite subject is SS.<br><br>" \
             "My name is Samantha from Ruby. My favorite subject is Math.<br><br>" \
             "My name is Queeny from Ruby. My favorite subject is English.<br><br>" \
             "My name is Sam from Ruby. My favorite subject is Science.<br><br>" \
             "My name is Ebti from Ruby. My favorite subject is TLE."

    for c in classmates:
        output += f"My name is {c.name} from {c.section}. My favorite subject is {c.subject}."

    document.getElementById("list").innerHTML = output