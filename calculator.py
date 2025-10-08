
import dearpygui.dearpygui as dpg

def update_number(sender, app_data, user_data):
    print(user_data)
    print("left operand")
    if dpg.get_value("operator") == "":
        dpg.set_value("left_operand", dpg.get_value("left_operand") + user_data)
    else:
        dpg.set_value("right_operand", dpg.get_value("right_operand") + user_data)

def delete_number(sender, app_data, user_data):
    if dpg.get_value("right_operand") != "":
        dpg.set_value("right_operand", dpg.get_value("right_operand")[:-1])
    elif dpg.get_value("operator") != "":
        dpg.set_value("operator", "")
    elif dpg.get_value("left_operand") != "":
        dpg.set_value("left_operand", dpg.get_value("left_operand")[:-1])

def update_operator(sender, app_data, user_data):
    if dpg.get_value("left_operand") != "":
        dpg.set_value("operator", user_data)

def perform_operation(sender, app_data):
    left = dpg.get_value("left_operand")
    right = dpg.get_value("right_operand")
    operator = dpg.get_value("operator")
    
    if left and right and operator:
        try:
            left_num = float(left)
            right_num = float(right)
            
            if operator == "+":
                result = left_num + right_num
            elif operator == "-":
                result = left_num - right_num
            elif operator == "×":
                result = left_num * right_num
            elif operator == "÷":
                result = left_num / right_num if right_num != 0 else "Error"
            
            # Clear all values and show result
            dpg.set_value("left_operand", str(result))
            dpg.set_value("right_operand", "")
            dpg.set_value("operator", "")
        except:
            dpg.set_value("left_operand", "Error")
            dpg.set_value("right_operand", "")
            dpg.set_value("operator", "")

def clear_all(sender, app_data, user_data):
    dpg.set_value("left_operand", "")
    dpg.set_value("right_operand", "")
    dpg.set_value("operator", "")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.value_registry():
    dpg.add_string_value(default_value="", tag="left_operand")
    dpg.add_string_value(default_value="", tag="right_operand")
    dpg.add_string_value(default_value="", tag="operator")

with dpg.window(label="Calculator", width=420, height=600) as main_window:
    # Display area
    with dpg.group(horizontal=True):
        dpg.add_text(source="left_operand")
        dpg.add_text(source="operator")
        dpg.add_text(source="right_operand")
    
    dpg.add_separator()
    
    # First row: 7, 8, 9, Delete, ÷
    with dpg.group(horizontal=True):
        dpg.add_button(label="7", callback=update_number, user_data="7", width=80, height=80)
        dpg.add_button(label="8", callback=update_number, user_data="8", width=80, height=80)
        dpg.add_button(label="9", callback=update_number, user_data="9", width=80, height=80)
        dpg.add_button(label="⌫", callback=delete_number, width=80, height=80)
        dpg.add_button(label="÷", callback=update_operator, user_data="÷", width=80, height=80)
    
    # Second row: 4, 5, 6, ×
    with dpg.group(horizontal=True):
        dpg.add_button(label="4", callback=update_number, user_data="4", width=80, height=80)
        dpg.add_button(label="5", callback=update_number, user_data="5", width=80, height=80)
        dpg.add_button(label="6", callback=update_number, user_data="6", width=80, height=80)
        dpg.add_button(label="×", callback=update_operator, user_data="×", width=80, height=80)
    
    # Third row: 1, 2, 3, +
    with dpg.group(horizontal=True):
        dpg.add_button(label="1", callback=update_number, user_data="1", width=80, height=80)
        dpg.add_button(label="2", callback=update_number, user_data="2", width=80, height=80)
        dpg.add_button(label="3", callback=update_number, user_data="3", width=80, height=80)
        dpg.add_button(label="+", callback=update_operator, user_data="+", width=80, height=80)
    
    # Fourth row: 0, ., C, -
    with dpg.group(horizontal=True):
        dpg.add_button(label="0", callback=update_number, user_data="0", width=80, height=80)
        dpg.add_button(label=".", callback=update_number, user_data=".", width=80, height=80)
        dpg.add_button(label="C", callback=clear_all, width=80, height=80)
        dpg.add_button(label="-", callback=update_operator, user_data="-", width=80, height=80)
    
    # Fifth row: Equals button
    with dpg.group(horizontal=True):
        dpg.add_button(label="=", callback=perform_operation, width=340, height=80)

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(main_window, global_theme)
dpg.set_primary_window(main_window, True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
