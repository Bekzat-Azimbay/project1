
import rx
from rx import operators as ops
import time

class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.volume = 50
    def add_track(self, track):
        self.playlist.append(track)
    def play(self):
        def play_track(track):
            print(f"Playing track: {track}")
        rx.from_(self.playlist) \
            .pipe(
                ops.map(lambda track: play_track(track))
            ) \
            .subscribe()
    def set_volume(self, volume):
        self.volume = volume
    def get_volume(self):
        return self.volume
player = MusicPlayer()
player.add_track("Track 1")
player.add_track("Track 2")
player.add_track("Track 3")
player.play()
time.sleep(5)
player.set_volume(70)
print(f"Volume: {player.get_volume()}")
