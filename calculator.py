
"""
Calculator Application using DearPyGui
=====================================

TEACHING GUIDE FOR STUDENT DEVELOPMENT
======================================

This calculator application is designed to teach GUI programming concepts.
Follow the numbered steps below to guide the student through development.

CURRENT STATUS: Basic calculator with working buttons and operations
NEXT STEPS: Follow the instructional comments throughout the code

TEACHING PROGRESSION:
1. First, understand the basic structure (lines 1-50)
2. Then, improve the display and user experience (lines 51-100) 
3. Next, add input validation and error handling (lines 101-150)
4. Finally, add advanced features and polish (lines 151+)

Each section has specific instructions for what to tell the student.
"""

import dearpygui.dearpygui as dpg

# =============================================================================
# STEP 1: UNDERSTAND THE BASIC STRUCTURE
# =============================================================================
# Tell the student: "Let's start by understanding how the calculator works.
# We have three main functions that handle user input. Let's look at each one."

def update_number(sender, app_data, user_data):
    """
    STEP 1A: Explain to student: "This function handles when someone clicks a number button.
    The 'user_data' parameter contains the number that was clicked (like '7' or '3').
    We need to decide whether to add it to the left number or right number."
    
    TEACHING POINT: Show the student how we check if an operator is set to decide
    which operand to update.
    """
    # TEACHING NOTE: Point out these debug prints - we'll remove them later
    print(user_data)  # This shows what number was clicked
    print("left operand")  # This shows which operand we're updating
    
    # TEACHING POINT: "Look at this logic - if no operator is set, we're building the first number"
    if dpg.get_value("operator") == "":
        # No operator set yet, so we're building the left operand
        dpg.set_value("left_operand", dpg.get_value("left_operand") + user_data)
    else:
        # TEACHING POINT: "If an operator IS set, we're building the second number"
        dpg.set_value("right_operand", dpg.get_value("right_operand") + user_data)

def delete_number(sender, app_data, user_data):
    """
    STEP 1B: Explain to student: "This function handles the backspace button (⌫).
    It needs to delete characters in the right order - like a real calculator."
    
    TEACHING POINT: "Notice the order of the if/elif statements - this is important!
    We delete from right to left: right operand → operator → left operand"
    """
    # TEACHING POINT: "First, check if we have a right operand to delete from"
    if dpg.get_value("right_operand") != "":
        # Delete from right operand if it exists
        dpg.set_value("right_operand", dpg.get_value("right_operand")[:-1])
    elif dpg.get_value("operator") != "":
        # TEACHING POINT: "If no right operand, but we have an operator, clear the operator"
        dpg.set_value("operator", "")
    elif dpg.get_value("left_operand") != "":
        # TEACHING POINT: "Finally, if we only have a left operand, delete from that"
        dpg.set_value("left_operand", dpg.get_value("left_operand")[:-1])

def update_operator(sender, app_data, user_data):
    """
    STEP 1C: Explain to student: "This function handles when someone clicks +, -, ×, or ÷.
    We only set the operator if we already have a left number."
    
    TEACHING POINT: "This prevents errors - you can't do an operation without a first number!"
    """
    # TEACHING POINT: "We check if we have a left operand before setting the operator"
    if dpg.get_value("left_operand") != "":
        dpg.set_value("operator", user_data)

def perform_operation(sender, app_data):
    """
    STEP 1D: Explain to student: "This is the most important function - it does the math!
    When someone clicks =, we need to get all three pieces and calculate the result."
    
    TEACHING POINT: "Notice we use try/except to handle errors gracefully"
    """
    # TEACHING POINT: "First, we get all the values from our calculator state"
    left = dpg.get_value("left_operand")
    right = dpg.get_value("right_operand")
    operator = dpg.get_value("operator")
    
    # TEACHING POINT: "We check if we have all three pieces before doing math"
    if left and right and operator:
        try:
            # TEACHING POINT: "Convert strings to numbers for calculation"
            left_num = float(left)
            right_num = float(right)
            
            # TEACHING POINT: "Use if/elif to handle different operations"
            if operator == "+":
                result = left_num + right_num
            elif operator == "-":
                result = left_num - right_num
            elif operator == "×":
                result = left_num * right_num
            elif operator == "÷":
                # TEACHING POINT: "Special case for division by zero"
                result = left_num / right_num if right_num != 0 else "Error"
            
            # TEACHING POINT: "Show the result and clear the other values"
            dpg.set_value("left_operand", str(result))
            dpg.set_value("right_operand", "")
            dpg.set_value("operator", "")
        except:
            # TEACHING POINT: "If something goes wrong, show an error"
            dpg.set_value("left_operand", "Error")
            dpg.set_value("right_operand", "")
            dpg.set_value("operator", "")

def clear_all(sender, app_data, user_data):
    """
    STEP 1E: Explain to student: "This is the simplest function - it clears everything.
    When someone clicks 'C', we reset all three values to empty strings."
    """
    dpg.set_value("left_operand", "")
    dpg.set_value("right_operand", "")
    dpg.set_value("operator", "")

# =============================================================================
# STEP 2: IMPROVE THE DISPLAY AND USER EXPERIENCE
# =============================================================================
# Tell the student: "Now that we understand the basic functions, let's improve how
# the calculator looks and works. We'll start with the GUI setup."

# Initialize DearPyGui
dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

# TEACHING POINT: "This creates our 'memory' - three variables to store calculator state"
with dpg.value_registry():
    dpg.add_string_value(default_value="", tag="left_operand")
    dpg.add_string_value(default_value="", tag="right_operand")
    dpg.add_string_value(default_value="", tag="operator")

# =============================================================================
# STEP 2A: CREATE THE CALCULATOR WINDOW
# =============================================================================
# Tell the student: "Now we create the main window. This is like creating a new window
# on your computer that will hold our calculator."

# Create the main calculator window
with dpg.window(label="Calculator", width=420, height=600) as main_window:
    # =============================================================================
    # STEP 2B: CREATE THE DISPLAY AREA
    # =============================================================================
    # Tell the student: "This is where the numbers and operations will show up.
    # Right now it's very basic - we'll improve it later!"
    
    # TEACHING POINT: "This creates a horizontal group - all items will be side by side"
    with dpg.group(horizontal=True):
        dpg.add_text(source="left_operand")   # Shows the first number
        dpg.add_text(source="operator")      # Shows +, -, ×, or ÷
        dpg.add_text(source="right_operand") # Shows the second number
    
    dpg.add_separator()  # A line to separate display from buttons
    
    # =============================================================================
    # STEP 2C: CREATE THE BUTTON LAYOUT
    # =============================================================================
    # Tell the student: "Now we create all the buttons. Each button needs:
    # 1. A label (what text shows on the button)
    # 2. A callback (which function to call when clicked)
    # 3. user_data (what to pass to the function)
    # 4. Size (width and height)"
    
    # TEACHING POINT: "Each row of buttons is in its own horizontal group"
    # First row: 7, 8, 9, Delete, ÷
    with dpg.group(horizontal=True):
        dpg.add_button(label="7", callback=update_number, user_data="7", width=80, height=80)
        dpg.add_button(label="8", callback=update_number, user_data="8", width=80, height=80)
        dpg.add_button(label="9", callback=update_number, user_data="9", width=80, height=80)
        dpg.add_button(label="⌫", callback=delete_number, width=80, height=80)
        dpg.add_button(label="÷", callback=update_operator, user_data="÷", width=80, height=80)
    
    # TEACHING POINT: "Notice how we organize buttons in rows - this makes it look like a real calculator"
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
    
    # TEACHING POINT: "The equals button is wider - it spans multiple columns"
    # Fifth row: Equals button
    with dpg.group(horizontal=True):
        dpg.add_button(label="=", callback=perform_operation, width=340, height=80)

# =============================================================================
# STEP 3: ADD INPUT VALIDATION AND ERROR HANDLING
# =============================================================================
# Tell the student: "Now let's make our calculator more robust by adding validation.
# We'll prevent common errors and make the user experience better."

# TEACHING POINT: "This creates a theme to make our buttons look nicer"
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(main_window, global_theme)

# =============================================================================
# STEP 4: START THE APPLICATION
# =============================================================================
# Tell the student: "Finally, we start our calculator application. This is like
# turning on the calculator - it opens the window and starts listening for clicks."

dpg.set_primary_window(main_window, True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# =============================================================================
# TEACHING GUIDE: NEXT STEPS FOR STUDENT DEVELOPMENT
# =============================================================================
"""
INSTRUCTOR NOTES: Use these steps to guide your student through improvements

PHASE 1: BASIC IMPROVEMENTS (Start here!)
==========================================
Tell the student: "Great! Your calculator works. Now let's make it better."

Step 1: Remove Debug Prints
- Find the print() statements in update_number()
- Delete them: "We don't need these anymore - they were just for testing"

Step 2: Add Input Validation
- "Let's prevent users from entering multiple decimal points"
- Add this to update_number(): 
  if user_data == "." and "." in current_value:
      return  # Don't add another decimal point

Step 3: Improve Error Messages
- "Instead of just showing 'Error', let's be more specific"
- Replace generic "Error" with "Division by zero" or "Invalid input"

PHASE 2: INTERMEDIATE FEATURES
==============================
Tell the student: "Now let's add some cool features!"

Step 4: Add Memory Functions
- "Let's add M+, M-, MR, MC buttons like a real calculator"
- Create new functions: memory_add(), memory_subtract(), memory_recall(), memory_clear()
- Add memory buttons to the GUI

Step 5: Improve the Display
- "Let's make the display look more like a real calculator"
- Add a proper display box with borders
- Show the full calculation (e.g., "2 + 3 = 5")

PHASE 3: ADVANCED FEATURES
===========================
Tell the student: "Ready for some advanced programming?"

Step 6: Add Keyboard Support
- "Let's make it work with keyboard keys too"
- Research DearPyGui keyboard handling
- Add key callbacks for numbers and operations

Step 7: Add More Operations
- "Let's add square root, percentage, and power functions"
- Create new operation functions
- Add new buttons to the GUI

PHASE 4: POLISH AND ORGANIZATION
=================================
Tell the student: "Now let's make it professional!"

Step 8: Better Styling
- "Let's make it look really nice"
- Add different colors for different button types
- Add hover effects and animations

Step 9: Code Organization
- "Let's split this into multiple files"
- Create separate files for: calculator logic, GUI setup, operations
- "This makes the code easier to understand and maintain"

BONUS CHALLENGES FOR ADVANCED STUDENTS
======================================
- Add a history window showing previous calculations
- Implement undo/redo functionality
- Add calculator themes/skins
- Create a scientific calculator mode
- Add unit conversion features
- Make it work on mobile devices

TEACHING TIPS:
- Let the student run the calculator after each change
- Ask them to explain what each part does
- Encourage them to experiment with different values
- Have them test edge cases (like division by zero)
- Ask them to think of improvements they'd like to see
"""
