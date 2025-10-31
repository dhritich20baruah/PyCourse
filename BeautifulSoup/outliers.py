game_initiating_window()
game_over_time = None  

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and current_winner is None and not is_draw:
            if check_win() is False: 
                user_click()
                if check_win():
                    game_over_time = time.time()


    if (current_winner or is_draw) and game_over_time and time.time() - game_over_time >= 10:
        reset_game()
        game_over_time = None

    pg.display.update()
    clock.tick(FPS)
