# from controller import try2
# from controller.streaming_controllers.youtube_controller import youtube_controller 

from controller.serverController.server_controller import server_controller

class main_class:
    def __init__(self):
        self.sc = server_controller()


main_class()