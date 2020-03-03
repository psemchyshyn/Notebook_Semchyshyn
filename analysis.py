from notebook import Notebook, Note


def clas_note():
    """
    A function for analysing instance of Note
    class
    """
    note = Note("hello world", tags="first note")
    print("Object note is a representitive of class: ", type(note), "\n")
    print("All attributes and their values of a Note object:", note.__dict__, "\n")
    all_attr, built_in_attr, created_attr = all_object_attr(note)
    print("All attributes of Note object:", all_attr, "\n")
    print("Built-in attributes:", built_in_attr, "\n")
    print("Creates attributes:", created_attr, "\n")


def clas_notebook():
    """
    A function for analysing instance of Notebook
    class
    """
    notebook = Notebook()
    print("Object note is a representitive of class: ", type(notebook), "\n")
    print("All attributes and their values of a Notebook object:", notebook.__dict__, "\n")
    all_attr, built_in_attr, created_attr = all_object_attr(notebook)
    print("All attributes of Notebook object:", all_attr, "\n")
    print("Built-in attributes:", built_in_attr, "\n")
    print("Created attributes:", created_attr, "\n")


def all_object_attr(object):
    """
    A function for getting all
    attributes of an object
    """
    all_attr = dir(object)
    built_ins = []
    created_attr = []
    for attr in all_attr:
        if "__" in attr:
            built_ins.append(attr)
        else:
            created_attr.append(attr)
    return all_attr, built_ins, created_attr


if __name__ == "__main__":
    clas_note()
    print("_"*100)
    clas_notebook()
    