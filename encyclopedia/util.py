import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def query(title):
    """
    Searches database with regex
    """
    entry_list = []
    entries = list_entries()
    for entry in entries:
        match = re.search("%s" % title, entry, re.IGNORECASE)
        if match:
            entry_list.append(entry)
    return entry_list

def Markdown(entry):
    """
    Converts Markdown text to html
    """
    # BR
    # pattern_br = "(^_.)"
    # new_br = r"<br>"

    # entry = re.sub(re.compile(pattern_br, re.MULTILINE), new_br, entry)

    # P
    # pattern_para = "([^#|##|###].$)([\w\d_.!?\/\\:\>\<,'\"].*)"
    pattern_para = "^((\w|\d).*)"
    new_para = r"<p>\1</p>"

    entry = re.sub(re.compile(pattern_para, re.MULTILINE), new_para, entry)

    # Bold
    pattern = "(\*\*)([a-zA-Z0-9_.!?\\- ]*)?(\*\*)"
    new_pattern = r"<strong>\2</strong>"

    entry = re.sub(pattern, new_pattern, entry)

    #  H3
    pattern_header_3 = "^(#{3})([a-zA-Z0-9_.!?\\ ]*.)"
    new_h3 = r"<h3>\2</h3>"

    entry = re.sub(re.compile(pattern_header_3, re.MULTILINE), new_h3, entry)

    #  H2
    pattern_header_2 = "^(#{2})([a-zA-Z0-9_.!?\\ ]*.)"
    new_h2 = r"<h2>\2</h2>"

    entry = re.sub(re.compile(pattern_header_2, re.MULTILINE), new_h2, entry)

    #  H1
    pattern_header = "^(#{1})([a-zA-Z0-9_.!?\\ ]*.)"
    new_h1 = r"<h1>\2</h1>"

    entry = re.sub(re.compile(pattern_header, re.MULTILINE), new_h1, entry)

    #  List
    pattern_list = "^(\*)([a-zA-Z0-9_.!?\\ ]*.)"
    new_list = r"<li>\2</li>"

    entry = re.sub(re.compile(pattern_list, re.MULTILINE), new_list, entry)

    # URL
    pattern_link = "(\[)([a-zA-Z0-9_.!?\\-]*)?(\])(\()([a-zA-Z0-9_.!?/\\-]*)(\))"
    new_link = r"<a href='\5'> \2 </a>"

    entry = re.sub(pattern_link, new_link, entry)

    return entry