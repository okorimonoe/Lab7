import pygame
import os

pygame.init()
screen_width = 600
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
music_directory = "music"
songs = os.listdir(music_directory)
current_song_index = 0
pygame.mixer.music.load(os.path.join(music_directory, songs[current_song_index]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_directory, songs[current_song_index]))
    pygame.mixer.music.play()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_directory, songs[current_song_index]))
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_b:
                previous_song()

    screen.fill(WHITE)
    instructions_text = font.render("Press 'p' to Play, 's' to Stop, 'n' for Next, 'b' for Previous", True, BLACK)
    screen.blit(instructions_text, (10, 10))
    current_song_text = font.render(songs[current_song_index], True, BLACK)
    text_width, text_height = font.size(songs[current_song_index])
    screen.blit(current_song_text, ((screen_width - text_width) / 2, (screen_height - text_height) / 2))
    pygame.display.flip()


pygame.quit()

