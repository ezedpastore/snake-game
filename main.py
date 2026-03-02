import sys
import pygame
from snake import Snake
from food import generate_food
from game_music import MusicManager
from game_sound import SoundManager
from game_over import handle_gameover, check_gameover
from constants import STATE_MENU, STATE_SETTINGS, STATE_PLAYING, STATE_COUNTDOWN, STATE_EXIT, FPS, MOVE_EVENT_INTERVAL, STATE_GAMEOVER
from draw_game import DrawGame
from handle_game_events import handle_keys_events, handle_snake_events
from handle_game_states import handle_menu_states, handle_settings_states


def main() -> None:
    """
    Punto de entrada principal del juego.
    Inicializa pygame, recursos y ejecuta el bucle principal manejando estados,
    eventos y renderizado. No devuelve valor.
    """
    pygame.init()

    state = STATE_MENU

    # setting up the music and sounds
    music = MusicManager('assets/music/snake_music.ogg')
    sound = SoundManager('assets/music/game_over.wav')

    # display screen
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Snake Game")

    # get a pygame clock object
    clock = pygame.time.Clock()  

    # initialize indexes and flags for menu and settings
    menu_index = 0
    settings_index = 0
    is_setting_selected = False
    
    countdown_start_time = 0

    snake = None
    food_position = None
    
    post_gameover_until = 0  # timestamp (ms) hasta el que mostramos "game over"
    
    draw = DrawGame(screen=screen)

    draw.draw_menu(selected_index=menu_index)

    move_event = pygame.USEREVENT + 1
    pygame.time.set_timer(move_event, MOVE_EVENT_INTERVAL)  # ms

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                music.quit()
                sound.quit()
                pygame.quit()
                sys.exit()
            
            if state == STATE_MENU:
                (currently_menu_index, is_option_selected) = handle_keys_events(event=event, selected_index=menu_index)
            
                menu_index = currently_menu_index
                
                (state, countdown_start_time) = handle_menu_states(is_option_selected=is_option_selected, currently_menu_index=currently_menu_index, state=state, countdown_start_time=countdown_start_time)
        
            elif state == STATE_SETTINGS:    
                (currently_settings_index, is_setting_selected) = handle_keys_events(event=event, selected_index=settings_index)
                
                settings_index = currently_settings_index
            
                state = handle_settings_states(is_setting_selected=is_setting_selected, currently_settings_index=currently_settings_index, state=state, music=music, sound=sound)
            
            elif state == STATE_PLAYING:
                if snake is not None:
                    handle_snake_events(event=event, snake=snake, move_event=move_event)
                        
            elif state == STATE_EXIT:
                music.quit()
                sound.quit()
                pygame.quit()
                sys.exit()
            
        if state == STATE_MENU:
            draw.draw_menu(selected_index=menu_index)
        
        elif state == STATE_SETTINGS:
            draw.draw_settings(selected_index=settings_index, music=music, sound=sound)
        
        elif state == STATE_COUNTDOWN:        
            has_finished = draw.draw_countdown(countdown_start_time=countdown_start_time)
            
            if has_finished:
                # create the snake
                snake = Snake()  
                            
                # genrate the first food position
                food_position = generate_food(snake)
                
                state = STATE_PLAYING
        
        elif state == STATE_PLAYING:
            # safety: ensure snake exists
            if snake is None:
                snake = Snake()
                food_position = generate_food(snake)

            #eat food
            if snake.get_body()[0] == food_position:
                snake.grow_snake()
                food_position = generate_food(snake)
            
            draw.draw_playing()
                        
            draw.draw_score(score=snake.get_score())
            
            draw.draw_food(position=food_position)
            
            draw.draw_snake(snake=snake)
            
            # check if game is over and handle it
            if snake is not None:
                is_gameover = check_gameover(snake=snake)
                
                if is_gameover:
                    state = STATE_GAMEOVER

        elif state == STATE_GAMEOVER:
            if is_gameover and post_gameover_until == 0:
                was_music_paused = handle_gameover(music=music, sound=sound, draw=draw, snake=snake)
                
                # establish the timestamp until which we show the game over screen (2 seconds from now)
                post_gameover_until = pygame.time.get_ticks() + 2000  
                
            elif post_gameover_until != 0:
                draw.draw_gameover(snake=snake)
                
                if pygame.time.get_ticks() >= post_gameover_until:
                    if was_music_paused:
                        music.music_on()
                    
                    snake = None
                    food_position = None
                    state = STATE_MENU
                    post_gameover_until = 0
                    was_music_paused = False
                
            
        pygame.display.update()
        
        clock.tick(FPS) # limit the frame rate to 60 FPS

if __name__ == "__main__":
    main()
