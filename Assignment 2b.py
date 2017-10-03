# Created by: Khoa Le
# Created on October 3 2017
# Created for ICS3U
# This program calculates how high the object is 100m from the ground.

import ui

def calculate_touch_up_inside(sender):
	# Variable
	GRAVITY = 9.81
	
	# Input
	seconds = int(view['enter_seconds_textfield'].text)
	
	# Process
	height = 100.0 - 0.5 * GRAVITY * seconds ** 2
	
	# Output
	view['answer_label'].text = str(height) + "m"

view = ui.load_view()
view.present('sheet')
