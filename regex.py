import re

user_input = input()

# Bold
pattern = "(\*\*)([a-zA-Z0-9_.!?\\- ]*)?(\*\*)"
new_pattern = r"<strong> \2 </strong>"

entry = re.sub(pattern, new_pattern, entry)

#  H1
pattern_header = "(#)([a-zA-Z0-9_.!?\\- ]*$\n?)"
new_h1 = r"<h1> \2 </h1>"

entry = re.sub(pattern_header, new_h1, entry)

#  H2
pattern_header_2 = "(##)([a-zA-Z0-9_.!?\\- ]*$\n?)"
new_h2 = r"<h2> \2 </h2>"

entry = re.sub(pattern_header_2, new_h2, entry)

#  H3
pattern_header_3 = "(###)([a-zA-Z0-9_.!?\\- ]*$\n?)"
new_h3 = r"<h3> \2 </h3>"

entry = re.sub(pattern_header_3, new_h2, entry)

#  List
pattern_list = "(-)([a-zA-Z0-9_.!?\\- ]*$\n?)"
new_list = r"<li> \2 </li>"

entry = re.sub(pattern_list, new_list, entry)

# URL
pattern_link = "(\[)([a-zA-Z0-9_.!?\\- ]*)?(\])(\()([a-zA-Z0-9_.!?/\\-]*)(\))"
new_link = r"<a href='\5'> \2 </a>"

entry = re.sub(pattern_link, new_link, entry)

# P
pattern_para = "(^[a-zA-Z0-9_.!?\*\\- ]*$\n?)"
new_para = r"<p> \1 </p>"

entry = re.sub(pattern_para, new_para, entry)
