from cradle.config import Config
from cradle.log import Logger
from cradle.gameio import IOEnvironment
from cradle.environment.chrome.skill_registry import register_skill
from cradle.environment.chrome.atomic_skills.interact import *
config = Config()
logger = Logger()
io_env = IOEnvironment()

"""
TODO:

Add a start_sketch_mode(top, front, right) function that starts sketch mode on the plane you want
Add a draw_rectangle(center, width, length) which specifies the coordinates to draw the rectangle, 
the wdith and the length of the rectangle. For now let's just fix coords to the center
"""

@register_skill("click_on_label")
def click_on_label(label_id, mouse_button):
    """
    Moves the mouse to the position of the specified box id inside the application window and clicks.

    Parameters:
    - label_id: The numerical label id of the bounding box to click at.
    - mouse_button: The mouse button to be clicked. It should be one of the following values: "left", "right", "middle".
    """
    label_id = str(label_id)
    x, y = 0.5, 0.5
    click_at_position(x, y, mouse_button)


@register_skill("start_extrude_menu")
def start_extrude_menu():
    """
    Opens the extrusion menu. 
    """
    # click_at_position(0.15, 0.16, "left")
    press_keys_combined(["shift", "E"])
    


@register_skill("exit_menu")
def exit_menu():
    """
    If an operation menu is opened (such as sketching, chamfers and extruding), exits out of the menu
    """
    click_at_position(0.294, 0.203, "left")

@register_skill("set_extrude_depth")
def set_extrude_depth(depth=25):
    """
    Sets the extrude depth. Ensure that the extrude menu is open before calling this operation

    Parameters:
     - depth: The depth (measured in mm) to extrude the surface by. If no depth is specified. The default depth will be 25
    """
    click_at_position(0.263, 0.398, "left")
    type_text(f"{depth}")

@register_skill("confirm_operation")
def confirm_operation():
    """
    If an operation menu is open (like extrudes, sketches and chamfers), confirms the operation
    """
    click_at_position(0.275, 0.204, "left")


@register_skill("extrude")
def extrude(depth=25):
    """
    Performs an extrusion on the selected face. Ensure that you have selected a face before calling this action
    
    Preconditions:
    - A surface is selected if and only if it is highlighted in yellow and has yellow borders. You must select exactly one surface before calling this action. 

    Parameters:
    - depth: The depth (measured in mm) to extrude the surface by. If no depth is specified. The default depth will be 25
    """
    click_at_position(0.15, 0.16, "left")
    if depth:
        click_at_position(0.263, 0.398, "left")
        type_text(f"{depth}")
    click_at_position(0.275, 0.204, "left")
    press_key('esc') #ensure that we close the menu

@register_skill("fillet")
def fillet(radius=5):
    """
    Performs a fillet on the selected edge. Ensure that you have selected an edge before calling this action

    Parameters:
    - radius: The radius to perform the fillet. If no fillet is specified, the fillet will be 5
    """
    click_at_position(0.27, 0.16, "left")
    if radius:
        click_at_position(0.27, 0.434, "left")
        type_text(f"{radius}")
    click_at_position(0.275, 0.209, "left")
    press_key('esc')

@register_skill("start_sketch")
def start_sketch(plane):
    """
    Starts a sketch on a specified plane

    Parameters:
    - plane: the plane you want to start the sketch on. They are the Top, Front and Right planes. 
    """
    click_at_position(0.11, 0.17, "left")
    if plane == "Top":
        click_at_position(0.092, 0.337, "left")
    elif plane == "Front":
        click_at_position(0.092, 0.374, "left")
    elif plane == "Right":
        click_at_position(0.092, 0.407, "left")

@register_skill("draw_rectangle")
def draw_rectangle(width, height):
    """
    Draws a rectangle centered in the origin with the specified width and height. Ensure that you have started a sketch via click_sketch_button before calling this function. Otherwise the function will fail

    Parameters:
    - width: width of the rectangle measured in mm
    - height: height of the rectangle measured in mm
    """
    click_at_position(0.942, 0.288, "left") # centers origin
    
    press_key('r')
    click_at_position(0.579, 0.571, "left")
    click_at_position(0.61, 0.673, "left") # arbitrary position to create the rectangle
    type_text(str(width))
    press_key('enter')
    type_text(str(height))
    press_key('enter')

@register_skill("cancel_sketch")
def cancel_sketch():
    """
    Cancels a sketch if currently in sketch mode. Ensure that you are currently drawing a sketch before calling this command
    """
    click_at_position(0.294, 0.203, "left")

@register_skill("confirm_sketch")
def confirm_sketch():
    """
    Confirms the creation of a sketch. Ensure that you are currently drawing a sketch before calling this command
    """
    click_at_position(0.275, 0.203, "left")


# def mirror(mirror_entity, plane):
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.48, 0.16, "left")
#     click_on_label(mirror_entity)
#     click_at_position(0.217, 0.369)
#     click_on_label(plane)
#     click_at_position(0.278, 0.213)


# def hole():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.4, 0.16, "left")

# def external_thread():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.42, 0.16, "left")


# def sweep():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.19, 0.16, "left")


# def loft():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.21, 0.16, "left")



def revolve(sketch_plane, sketch_axis):
    """
    Clicks on the extrude button
    """
    click_at_position(0.17, 0.16, "left")
    click_on_label(sketch_plane)
    click_at_position(0.237, 0.369, "left")
    click_on_label(sketch_axis)
    click_at_position(0.272, 0.206, "left")









# def chamfer():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.31, 0.16, "left")





# def thicken():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.24, 0.16, "left")


# def thicken_dropdown():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.25, 0.16, "left")




# def fillet_dropdown():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.285, 0.16, "left")





# def draft():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.33, 0.16, "left")

# def draft_dropdown():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.34, 0.16, "left")


# def rib():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.36, 0.16, "left")

# def shell():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.38, 0.16, "left")






# def linear_pattern():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.45, 0.16, "left")


# def linear_pattern_dropdown():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.465, 0.16, "left")




# def boolean():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.51, 0.16, "left")

# def split():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.53, 0.16, "left")

# def transform():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.555, 0.16, "left")


# def transform_dropdown():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.57, 0.16, "left")


# def delete_part():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.59, 0.16, "left")


# def modify_fillet():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.61, 0.16, "left")

# def delete_face():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.635, 0.16, "left")

# def move_face():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.655, 0.16, "left")


# def replace_face():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.685, 0.16, "left")

# def plane():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.7, 0.16, "left")

# def plane_dropdown():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.72, 0.16, "left")

# def frame():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.74, 0.16, "left")


# def frame_dropdown():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.76, 0.16, "left")

# def sheet_metal_model():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.78, 0.16, "left")

# def sheet_metal_model_dropdown():
#     """
#     Clicks on the extrude button
#     """
#     click_at_position(0.795, 0.16, "left")

# __all__ = [
#     "click_on_label",
# ]
