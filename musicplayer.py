import os
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playing = False
        self.paused = False
        self.music_folder = None
        self.current_index = 0
        self.music_list = []

    def select_music_folder(self, folder_path):
        if os.path.exists(folder_path):
            self.music_folder = folder_path
            self.music_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.mp3')]
            if self.music_list:
                self.current_index = 0
                pygame.mixer.music.load(self.music_list[self.current_index])
                print("Music folder selected:", folder_path)
            else:
                print("No music files found in the selected folder.")
        else:
            print("Invalid folder path.")

    def play(self):
        if self.music_folder:
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False
            print("Playing:", os.path.basename(self.music_list[self.current_index]))

    def stop(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.paused = False
            print("Music stopped.")

    def pause(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            print("Music paused.")
        elif self.playing and self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            print("Music resumed.")

    def next_song(self):
        if self.music_folder:
            self.stop()
            self.current_index = (self.current_index + 1) % len(self.music_list)
            pygame.mixer.music.load(self.music_list[self.current_index])
            self.play()

    def prev_song(self):
        if self.music_folder:
            self.stop()
            self.current_index = (self.current_index - 1) % len(self.music_list)
            pygame.mixer.music.load(self.music_list[self.current_index])
            self.play()

if __name__ == "__main__":
    player = MusicPlayer()

    while True:
        print("\nMenu:")
        print("1. Select Music Folder")
        print("2. Play")
        print("3. Stop")
        print("4. Pause/Resume")
        print("5. Next Song")
        print("6. Previous Song")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            folder_path = input("Enter folder path: ")
            player.select_music_folder(folder_path)
        elif choice == "2":
            player.play()
        elif choice == "3":
            player.stop()
        elif choice == "4":
            player.pause()
        elif choice == "5":
            player.next_song()
        elif choice == "6":
            player.prev_song()
        elif choice == "7":
            pygame.quit()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
