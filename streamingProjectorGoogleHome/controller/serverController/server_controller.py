from controller.streaming_controllers.streaming_service_controller  import streaming_service_controller

class server_controller:
    key_phrase = "video service"

    def __init__ (self):
        self.start()


    def start(self):
        # listen_to_server()

        # def listen_to_server(self):
        #     while True:
        #         self.input_parser()
        self.input_parser("Video Service youtube")

    def input_parser(self, user_input:str):
        user_input = user_input.lower()
        video_service = ""
        if self.key_phrase in user_input:
            video_service = self.crop_key_phrase_out(user_input)

        streaming_service_controller().select_streaming_service(video_service)

    # Sliding windows Problem
    def crop_key_phrase_out(self, user_input:str):
        start = -1
        end = -1
        count  = 0
        key_phrase_size = len(self.key_phrase)
        user_input_size = len(user_input)
        
        for i in range(user_input_size):
            if self.key_phrase[i] == user_input[i]:
                count += 1 
                # start is not assigned
                if start == -1:
                    start = i
                # found a whole match
                if count == key_phrase_size:
                    end = i
                    break    
            else:
                #couldnt find a whole match
                count =0
                start = -1
        return self.find_streaming_service_sub_string(user_input, start, end)

    def find_streaming_service_sub_string(self, user_input:str, start:int, end:int):
        user_input_size = len(user_input)
        sub_string = ""
        if start != -1:
            sub_string = user_input[0:start]
            sub_string = sub_string + user_input[end+1:user_input_size]
        
        return sub_string.strip()


# Create a Back function, to go to previous page
        



