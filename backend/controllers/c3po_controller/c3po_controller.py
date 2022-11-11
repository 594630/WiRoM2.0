import sys
import os

controller_path = os.path.join(os.getcwd(), os.pardir)
sys.path.insert(0, controller_path)

from bb8_controller_class import Bb8ControllerClass
bb8_controller = Bb8ControllerClass("c3po")
bb8_controller.initiate_threads()