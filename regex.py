import re


# pattern2 = "(\*\*{2}*)"
# (#)([a-zA-Z0-9_.!?\\-]*)?
# new_2 = r"<h1> </h1>"

user_input = input()

# Bold
pattern = "(\*\*)([a-zA-Z0-9_.!?\\- ]*)?(\*\*)"
new_pattern = r"<strong> \2 </strong>"


new_user_input = re.sub(pattern, new_pattern, user_input)
print(new_user_input)
user_input = new_user_input

#  H1
pattern_header = "(#)([a-zA-Z0-9_.!?\\- ]*$\n?)"
new_h1 = r"<h1> \2 </h1>"

new_user_input = re.sub(pattern_header, new_h1, user_input)
print(new_user_input)
user_input = new_user_input

#  H2
pattern_header_2 = "(##)([a-zA-Z0-9_.!?\\- ]*$\n?)"
new_h2 = r"<h2> \2 </h2>"

new_user_input = re.sub(pattern_header_2, new_h2, user_input)
print(new_user_input)
user_input = new_user_input

#  H3
pattern_header_3 = "(###)([a-zA-Z0-9_.!?\\- ]*$\n?)"
new_h3 = r"<h3> \2 </h3>"

new_user_input = re.sub(pattern_header_3, new_h2, user_input)
print(new_user_input)
user_input = new_user_input

#  List
pattern_list = "(-)([a-zA-Z0-9_.!?\\- ]*$\n?)"
new_list = r"<li> \2 </li>"

new_user_input = re.sub(pattern_list, new_list, user_input)
print(new_user_input)
user_input = new_user_input

# URL
pattern_link = "(\[)([a-zA-Z0-9_.!?\\- ]*)?(\])(\()([a-zA-Z0-9_.!?/\\-]*)(\))"
new_link = r"<a href='\5'> \2 </a>"

new_user_input = re.sub(pattern_link, new_link, user_input)
print(new_user_input)
user_input = new_user_input

# P
pattern_para = "(^[a-zA-Z0-9_.!?\*\\- ]*$\n?)"
new_para = r"<p> \1 </p>"

new_user_input = re.sub(pattern_para, new_para, user_input)
print(new_user_input)
user_input = new_user_input