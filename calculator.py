
left - int(dpg-get_value("left_operand" ))

right - int(dpg-get_value("right_operand" ))
1f dps-get_value("operator") -=
"+":

dpg-set_ value( str (left + right)

if dpg-get_value("operator") -
dpg-set_value str (left - right) )

if dpg-get_value("operator") -= */":
dpg-set_value( str (left / right) )

if dpg-get_value("operator")
-- *x*:
dpg-set_value( str (left * right) )

if dpg-get_value("operator")
*%*:
dpg-set_value( str (left % right) )
mainpy
alc apppy 1 x
A › Cosches > Coach Eric >
* calc. app-py > 6 update operator
Import dearpygul,dearpyaul, as dpe
def update number (sender, app_data, user_data) :
print(user data)
print("left operand" )
1f dpg-get value("operator*) - **:
pg-set_value("left _operand",pg-get _value ("left operand") + user _data)
dag-set_value ("right_operand",dpg-get_value ("right_operand*") + user data)
119
11101
1140
defi
delete number (sender, app.
data,
user data):
If (dpg-get_value("right_operand*) - **) :
dpg-set_ value("right_operand",
•11f (dps-get_value("left_operand") - **):
dpg-set_value("left_operand",
18
19
def update operator (sender,
app_data, user data):
dpg-set _value""operator", user_datal
def perforn_operation(sender, app_data):
25
調型
36
37
dpg-create_context()
dpg-create_vicuport()
dpg-setup dearpygui ()
39
41
4고
43
44
45
with dpg-texture_registry():
width, height, channel, data, - dpg. load _image("delete_button-png")
dpg-add _static_texture(width-width, height-height, default_valus-data, tag-"delete_button_texture*)
47
4룸
49
58
51
52
53
54
with dpg-value_registry():
dpg-add _string_value(default_valuc="", tag-"left_operand" )
dpg-add_string_value(default_value-"*,
tag-"right_operand")
dpg-add_string_value(default_valuc-**, tag-"operator")
with dpg-window(label-"Example Window")as main_window:
with dps-group(horizontal-Truc) :
dpg-add_ text(source-"left_operand" )
dpg-add _text (source-"operator") dpg-add_text(source-"right_operand")
56
57
58
59
68）
61
62
with dpg-group(horizontal-Truc):
dpg-add_button(label-"7", callback-update_number, user_data-"7",
width-108, height-100)
dpg-add_button(label-"g", callback-update_number, user_data-"8", width-188, height-100) dpg-add_button(label-"9", callback-update_number, user_data-"9",
width-100, height-100)
dpg-add image_button(texture_tag-"delete_button_texture", callback-delete_number, tag-"delete", user_data-"delete_number", width-58, height-50) dpg-add_button(label-"/", callback-update_operator, user_data-"/*, width-180, height-100)
64
65
66
67
68
69
with dpg-group(horizonta)-True): dpg-add_button(label-"*"
callback-update_number,user_data-"4",
dpg-add_ button(label-"5,
callback-update_number,user_data-"5",
width-100, height-100) width-100, height-100)
dpg-add_button(label-"6",
callback-update_number, user _data-*6", width-100, height-100)
dpg-add_ button(label-"x", callback-update_operator,user _data-"x", width-100, height-100)
71
72
73
74
75
76
77
78
79
8e
81
82
Nth
dps-group(horizontal-True):
dE-add_button(label-"3", callback-update_number, user_data dpg-add_button(label-"2",
callback-update_number, user_data»
dpg-add_buttan(label-"3",
callback-update number, user _data
dpg-add_ button(label-"*"
callback-update_operator, user_
dpg-add_button(label-"-"
callback-update_operator,user.
wddth-180, height-100)
Midth-100, height-100) wddth-100, height-100)
width-100, height-100) width-100, height-100)
with dps-group(horizontal-True):
dpg-add_button(label-"e", callback-update_number, user_data-dpg-add_button(label-"-",
callback-update_operator, user_data
dpg-add_button(label-"**, callback-update_ operator, user.
,width-100, height-100)
width-180, height-188) wddth-100, height-200)
85
86
ВОДІ
with dipe thene() as global theme:
with dp-thems component (4pg-mvButton):
epp-add there_style(dpg-myStyleVar Franckounding,50, category-dpg-avTheneCat_Care)
ars-bind iten thene(nain vindon, Blobal thene) spe-shoe viesport()
dpe-start dearpygul
Ape-destroy _context)