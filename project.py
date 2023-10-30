
from mutagen.mp3 import MP3
import pygame

class MusicPlayer:
    def __init__(self, file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        self.file = file
        self.playing = False
        self.paused = False
        self.volume = 1.0

    def play(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False

    def pause(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.paused = False

    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        return self.volume

    def get_duration(self):
        audio = MP3(self.file)
        duration = audio.info.length
        return duration

    def get_current_time(self):
        return pygame.mixer.music.get_pos() / 1000

    def is_playing(self):
        return self.playing

    def is_paused(self):
        return self.paused

if __name__ == "__main__":
    player = MusicPlayer("my_song.mp3")
    player.play()
    print("The song is playing u can increase the volume to listen...")
    pygame.time.delay(6893099)
    player.pause()
    print("Paused...")
    pygame.time.delay(378)
    player.play()
    print("Resuming...")
    pygame.time.delay(489)
    player.stop()
    print("Stopped.")
