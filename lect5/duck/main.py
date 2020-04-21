class VideoPlayer:
    def __init__(self, VideoFile):
        self.video_file = VideoFile

    def start(self):
        self.video_file.play()

class Film:
    def __init__(self, TITLE):
        self.title = TITLE

    def play(self):
        print("Film", self.title, "started")

class Serial:
    def __init__(self, TITLE, NUM_SER):
        self.title = TITLE
        self.num_ser = NUM_SER 

    def play(self):
        print("Serial", self.title,"with episodes", self.num_ser,"started")

    def last_seria(self):
        pass 

f = Film("LOTR")
videoPlayer1 = VideoPlayer(f)
videoPlayer1.start()

s = Serial("BBT", 100)
videoPlayer2 = VideoPlayer(s)
videoPlayer2.start()