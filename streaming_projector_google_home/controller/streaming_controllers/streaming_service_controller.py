from streaming_service_type import streaming_service_type


class streaming_service_controller:

    def __init__(self):
        self.streaming_types = streaming_service_type()
        self.setMap()

    def setMap(self):
        self.services = {
            self.streaming_types.youtube: self.start_youtube_controller,
            self.streaming_types.amazon: self.start_amazon_controller,
            self.streaming_types.netflix: self.start_netflix_controller,
            self.streaming_types.other: self.start_other_controller,
        }

    def select_streaming_service(self, streaming_service):
        return self.services[streaming_service]()

    def switch_streaming_service(self, streaming_service):
        return self.select_streaming_service(streaming_service)

    def start_youtube_controller(self):
        return None

    def start_netflix_controller(self):
        return None

    def start_amazon_controller(self):
        return None

    def start_other_controller(self):
        return None
