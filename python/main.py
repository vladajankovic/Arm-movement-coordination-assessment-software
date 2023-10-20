import os
import pygame as pg
import numpy as np
from datetime import datetime


def menu_buttons():
    text_font = pg.font.Font("fonts/liera-sans/LieraSans-Medium.ttf", 50)
    button_labels = [
        text_font.render("Training", 1, 'black'),
        text_font.render("Draw Test", 1, 'black'),
        text_font.render("Exit", 1, 'black')
    ]

    pg.draw.rect(screen, 'black', (
        WIDTH / 2 - WIDTH / 5 / 2 - 10,
        HEIGHT * (menu_select_no + 3) / 10 + 30 * menu_select_no - HEIGHT / 11 / 2 - 10,
        WIDTH / 5 + 20,
        HEIGHT / 11 + 20
    ), border_radius=10)

    for b in range(len(button_labels)):
        pg.draw.rect(screen, (240, 0, 0), (
            WIDTH / 2 - WIDTH / 5 / 2,
            HEIGHT * (b + 3) / 10 + 30 * b - HEIGHT / 11 / 2,
            WIDTH / 5,
            HEIGHT / 11
        ), border_radius=10)
        screen.blit(button_labels[b], button_labels[b].get_rect(center=(
            WIDTH / 2,
            HEIGHT * (b + 3) / 10 + 30 * b
        )))

    select = pg.image.load("./images/arrow.png").convert_alpha()
    select_rect = select.get_rect(center=(
        WIDTH * 3 / 8 - 15,
        HEIGHT * (menu_select_no + 3) / 10 + 30 * menu_select_no
    ))
    screen.blit(select, select_rect)


def menu_info():
    font = pg.font.Font("fonts/corbel/CORBELB.TTF", 35)
    surface_keys_info = font.render("Keys:", 1, 'black')
    surface_keys_info_up = font.render("UP KEY -> Previous button", 1, 'black')
    surface_keys_info_down = font.render("DOWN KEY -> Next button", 1, 'black')
    surface_keys_info_select = font.render("ENTER KEY -> Select button", 1, 'black')
    surface_keys_info_quit = font.render("ESC KEY -> Quit program", 1, 'black')

    screen.blit(surface_keys_info, surface_keys_info.get_rect(topleft=(50, HEIGHT * 1 / 2 + 150)))
    screen.blit(surface_keys_info_up, surface_keys_info_up.get_rect(topleft=(50, HEIGHT * 1 / 2 + 200)))
    screen.blit(surface_keys_info_down, surface_keys_info_down.get_rect(topleft=(50, HEIGHT * 1 / 2 + 250)))
    screen.blit(surface_keys_info_select, surface_keys_info_select.get_rect(topleft=(50, HEIGHT * 1 / 2 + 300)))
    screen.blit(surface_keys_info_quit, surface_keys_info_quit.get_rect(topleft=(50, HEIGHT * 1 / 2 + 350)))


def training_lines():
    line_color = (240, 200, 0)
    # Straight lines
    pg.draw.line(screen, line_color, (0, HEIGHT / 2), (WIDTH, HEIGHT / 2), 3)
    pg.draw.line(screen, line_color, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 3)
    pg.draw.line(screen, line_color, (0, 0), (WIDTH, HEIGHT), 3)
    pg.draw.line(screen, line_color, (WIDTH, 0), (0, HEIGHT), 3)
    pg.draw.line(screen, line_color, (WIDTH / 3, 0), (WIDTH * 2 / 3, HEIGHT), 3)
    pg.draw.line(screen, line_color, (WIDTH / 3, HEIGHT), (WIDTH * 2 / 3, 0), 3)

    # Horizontal lines
    for k in range(1, 18, 1):
        pg.draw.line(screen, line_color, (0, HEIGHT * k / 18), (WIDTH, HEIGHT * k / 18), 3)

    # Vertical lines
    v_step = 32
    for k in range(1, 8, 1):
        pg.draw.line(screen, line_color, (WIDTH * k / v_step, 0), (WIDTH * k / v_step, HEIGHT), 3)
        pg.draw.line(screen, line_color, (WIDTH * (v_step - k) / v_step, 0), (WIDTH * (v_step - k) / v_step, HEIGHT), 3)

    # Concentric circles
    for k in range(1, 10, 1):
        pg.draw.circle(screen, line_color, (WIDTH / 2, HEIGHT / 2), (HEIGHT / 2) * k / 9, 3)


def transparent_banner():
    transparent = pg.Surface((WIDTH, HEIGHT))
    transparent.set_alpha(150)
    screen.blit(transparent, (0, 0))

    text_back = pg.Surface((WIDTH / 2, HEIGHT / 2))
    text_back.fill('cyan')
    text_back_rect = text_back.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text_back, text_back_rect)

    str_font = pg.font.Font("fonts/liera-sans/LieraSans-Black.ttf", 40)
    str_text = ["Press SPACE or MOUSE CLICK", "to start/restart",
                "--------------------------------",
                "Sensitivity x{:.2f}".format(1 / drawtest.sensitivity[drawtest.level])]
    for idx, lvl in enumerate([-1, 0, 1, 2]):
        draw_info = str_font.render(str_text[idx], 1, 'black')
        draw_info_rect = draw_info.get_rect(center=(
            WIDTH / 2,
            HEIGHT / 2 + draw_info.get_height() * lvl
        ))
        screen.blit(draw_info, draw_info_rect)


def check_mouse_position():
    mouse_pos = pg.mouse.get_pos()
    if mouse_pos[0] == 0:
        pg.mouse.set_pos(WIDTH - 2, mouse_pos[1])
    if mouse_pos[1] == 0:
        pg.mouse.set_pos(mouse_pos[0], HEIGHT - 2)
    if mouse_pos[0] == WIDTH - 1:
        pg.mouse.set_pos(1, mouse_pos[1])
    if mouse_pos[1] == HEIGHT - 1:
        pg.mouse.set_pos(mouse_pos[0], 1)


class BaseModule:
    def __init__(self):
        self.cursor = pg.image.load("images/cursor_ball.png").convert_alpha()
        self.cursor = pg.transform.scale(self.cursor, (20, 20))
        self.cursor_rect = self.cursor.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        self.sensitivity = [1, 2, 4, 6, 8, 10, 15, 20, 30]
        self.max_level = len(self.sensitivity) - 1
        self.level = 0
        self.distance = [0, 0]

        self.text = pg.font.Font(None, 30)
        val = 1 / self.sensitivity[self.level]
        self.surface_room_info = self.text.render("Sensitivity x{:.2f}".format(val), 1, 'white')
        self.surface_room_info_up = self.text.render("Faster -> UP KEY", 1, 'white')
        self.surface_room_info_down = self.text.render("Slower -> DOWN KEY", 1, 'white')
        self.surface_room_info_quit = self.text.render("Exit -> ESC KEY", 1, 'white')
        self.surface_room_info_reset = self.text.render("", 1, 'white')
        self.surface_room_info_reset2 = self.text.render("", 1, 'white')
        self.surface_info_back1 = pg.Surface((250, 150))
        self.surface_info_back2 = pg.Surface((260, 160))
        self.surface_info_back2.fill('white')

    def refresh_info(self):
        self.surface_room_info = self.text.render(
            "Sensitivity x{:.2f}".format(1 / self.sensitivity[self.level]), 1, 'white')

    def room_info(self):
        self.refresh_info()
        x = WIDTH / 32 + 10
        y = HEIGHT * 6 / 18 - 70

        screen.blit(self.surface_info_back2, self.surface_info_back2.get_rect(topleft=(x - 5, y - 5)))
        screen.blit(self.surface_info_back1, self.surface_info_back1.get_rect(topleft=(x, y)))
        screen.blit(self.surface_room_info, self.surface_room_info.get_rect(topleft=(x + 15, y + 5)))
        screen.blit(self.surface_room_info_up, self.surface_room_info_up.get_rect(topleft=(x + 15, y + 30)))
        screen.blit(self.surface_room_info_down, self.surface_room_info_down.get_rect(topleft=(x + 15, y + 55)))
        screen.blit(self.surface_room_info_quit, self.surface_room_info_quit.get_rect(topleft=(x + 15, y + 80)))
        screen.blit(self.surface_room_info_reset, self.surface_room_info_reset.get_rect(topleft=(x + 15, y + 105)))
        screen.blit(self.surface_room_info_reset2, self.surface_room_info_reset2.get_rect(topleft=(x + 15, y + 130)))

    def reset(self):
        self.cursor_rect.center = (WIDTH / 2, HEIGHT / 2)
        self.level = 0
        self.distance = [0, 0]

    def move_cursor(self):
        rel_move = pg.mouse.get_rel()
        self.distance[0] += abs(rel_move[0])
        self.distance[1] += abs(rel_move[1])
        x_dist = self.distance[0] // self.sensitivity[self.level]
        self.cursor_rect.centerx += np.sign(rel_move[0]) * x_dist
        self.distance[0] = self.distance[0] % self.sensitivity[self.level]
        y_dist = self.distance[1] // self.sensitivity[self.level]
        self.cursor_rect.centery += np.sign(rel_move[1]) * y_dist
        self.distance[1] = self.distance[1] % self.sensitivity[self.level]

    def bound_cursor(self):
        if self.cursor_rect.left < 0:
            self.cursor_rect.left = 0
        if self.cursor_rect.right > WIDTH:
            self.cursor_rect.right = WIDTH
        if self.cursor_rect.top < 0:
            self.cursor_rect.top = 0
        if self.cursor_rect.bottom > HEIGHT:
            self.cursor_rect.bottom = HEIGHT


class TrainingModule(BaseModule):
    def __init__(self):
        super().__init__()

        self.surface_room_info_reset = self.text.render("Center dot -> SPACE or", 1, 'white')
        self.surface_room_info_reset2 = self.text.render("MOUSE CLICK", 1, 'white')


class DrawTestModule(BaseModule):
    def __init__(self):
        super().__init__()

        self.state = 0
        self.start_drawing = False

        self.elapsed_time = 0
        self.start_time = 0
        self.quadrant = 0
        self.visited_quadrants = {1: False, 2: False, 3: False, 4: False}

        self.score = 0
        self.sum_score = 0
        self.count = 0
        self.total_score = 0
        self.penalty = 0

        self.last_surface_and_score = []
        self.color_inner_list = []

        d = (HEIGHT / 10) / 6  # actually d = (HEIGHT / 2 / 10) / 6 but then dim -= 2 * d
        dim = HEIGHT * 8 / 10  # actually dim = (2 * HEIGHT / 2) * 8 / 10
        for k in range(6):
            surf = pg.Surface((dim, dim))
            surf.fill(((255 / 5) * k, 255, 0))
            self.color_inner_list.append([surf, surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))])
            dim -= d

        d = (HEIGHT / 10) / 15
        dim = HEIGHT * 7 / 10
        for k in range(15):
            surf = pg.Surface((dim, dim))
            surf.fill((255, 255 - (255 / 15) * (k + 1), 0))
            self.color_inner_list.append([surf, surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))])
            dim -= d

        d = (HEIGHT * 6 / 10) / 79
        dim = HEIGHT * 6 / 10
        for k in range(79):
            surf = pg.Surface((dim, dim))
            surf.fill((255 - (255 / 79) * (k + 1), 0, 0))
            self.color_inner_list.append([surf, surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))])
            dim -= d

        self.color_outer_list = []

        d = (HEIGHT / 10) / 6
        dim = HEIGHT * 8 / 10
        for k in range(6):
            dim += d
            surf = pg.Surface((dim, dim))
            surf.fill(((255 / 5) * k, 255, 0))
            self.color_outer_list.append([surf, surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))])

        d = (HEIGHT / 10) / 15
        dim = HEIGHT * 9 / 10
        for k in range(15):
            dim += d
            surf = pg.Surface((dim, dim))
            surf.fill((255, 255 - (255 / 15) * (k + 1), 0))
            self.color_outer_list.append([surf, surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))])

        d = (WIDTH / 2 - HEIGHT / 2) / 79
        dim = HEIGHT
        for k in range(79):
            dim += d
            surf = pg.Surface((dim, dim))
            surf.fill((255 - (255 / 79) * (k + 1), 0, 0))
            self.color_outer_list.append([surf, surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))])

        surf = pg.Surface((WIDTH, HEIGHT))
        self.color_outer_list.append([surf, surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))])

        xstep = 185
        m = WIDTH / 2 - HEIGHT / 2

        self.min_brightness = 100
        self.max_brightness = 200

        self.collision_left_top_surface_and_rect_list = []
        self.collision_left_bot_surface_and_rect_list = []
        self.collision_right_top_surface_and_rect_list = []
        self.collision_right_bot_surface_and_rect_list = []
        self.collision_top_left_surface_and_rect_list = []
        self.collision_top_right_surface_and_rect_list = []
        self.collision_bot_left_surface_and_rect_list = []
        self.collision_bot_right_surface_and_rect_list = []

        inc = 1
        for k in range(50):
            if k % 25 == 0 and k != 0:
                inc += 1
            surf = pg.Surface((m + WIDTH * (k + inc) / xstep, HEIGHT / 100))
            surf.set_alpha(self.min_brightness)
            self.collision_left_top_surface_and_rect_list.append([
                surf,
                surf.get_rect(topleft=(0, HEIGHT * k / 100))
            ])

        inc = 1
        for k in range(50):
            if k % 25 == 0 and k != 0:
                inc += 1
            surf = pg.Surface((m + WIDTH * (k + inc) / xstep, HEIGHT / 100))
            surf.fill('red')
            surf.set_alpha(self.min_brightness)
            self.collision_left_bot_surface_and_rect_list.append([
                surf,
                surf.get_rect(bottomleft=(0, HEIGHT * (100 - k) / 100))
            ])

        inc = 1
        for k in range(50):
            if k % 25 == 0 and k != 0:
                inc += 1
            surf = pg.Surface((m + WIDTH * (k + inc) / xstep, HEIGHT / 100))
            surf.fill('blue')
            surf.set_alpha(self.min_brightness)
            self.collision_right_top_surface_and_rect_list.append([
                surf,
                surf.get_rect(topright=(WIDTH, HEIGHT * k / 100))
            ])

        inc = 1
        for k in range(50):
            if k % 25 == 0 and k != 0:
                inc += 1
            surf = pg.Surface((m + WIDTH * (k + inc) / xstep, HEIGHT / 100))
            surf.fill('green')
            surf.set_alpha(self.min_brightness)
            self.collision_right_bot_surface_and_rect_list.append([
                surf,
                surf.get_rect(bottomright=(WIDTH, HEIGHT * (100 - k) / 100))
            ])

        inc = 1
        for k in range(50):
            surf = pg.Surface((WIDTH / xstep, HEIGHT * (1 + k) / 100))
            surf.fill('yellow')
            surf.set_alpha(self.min_brightness)
            self.collision_top_left_surface_and_rect_list.append([
                surf,
                surf.get_rect(topleft=(m + WIDTH * (k + inc) / xstep, 0))
            ])
            if k == 24:
                inc += 1
                self.collision_top_left_surface_and_rect_list.append([
                    surf,
                    surf.get_rect(topleft=(m + WIDTH * (k + inc) / xstep, 0))
                ])

        inc = 0
        for k in range(50):
            surf = pg.Surface((WIDTH / xstep, HEIGHT * (50 - k) / 100))
            surf.fill('magenta')
            surf.set_alpha(self.min_brightness)
            self.collision_top_right_surface_and_rect_list.append([
                surf,
                surf.get_rect(topleft=(WIDTH / 2 + WIDTH * (k + inc) / xstep, 0))
            ])
            if k == 25:
                inc += 1
                self.collision_top_right_surface_and_rect_list.append([
                    surf,
                    surf.get_rect(topleft=(WIDTH / 2 + WIDTH * (k + inc) / xstep, 0))
                ])

        inc = 1
        for k in range(50):
            surf = pg.Surface((WIDTH / xstep, HEIGHT * (1 + k) / 100))
            surf.fill('cyan')
            surf.set_alpha(self.min_brightness)
            self.collision_bot_left_surface_and_rect_list.append([
                surf,
                surf.get_rect(bottomleft=(m + WIDTH * (k + inc) / xstep, HEIGHT))
            ])
            if k == 24:
                inc += 1
                self.collision_bot_left_surface_and_rect_list.append([
                    surf,
                    surf.get_rect(bottomleft=(m + WIDTH * (k + inc) / xstep, HEIGHT))
                ])

        inc = 0
        for k in range(50):
            surf = pg.Surface((WIDTH / xstep, HEIGHT * (50 - k) / 100))
            surf.fill('pink')
            surf.set_alpha(self.min_brightness)
            self.collision_bot_right_surface_and_rect_list.append([
                surf,
                surf.get_rect(bottomleft=(WIDTH / 2 + WIDTH * (k + inc) / xstep, HEIGHT))
            ])
            if k == 25:
                inc += 1
                self.collision_bot_right_surface_and_rect_list.append([
                    surf,
                    surf.get_rect(bottomleft=(WIDTH / 2 + WIDTH * (k + inc) / xstep, HEIGHT))
                ])

        self.result_image = pg.Surface((0, 0))

        self.test_complete = pg.image.load("images/checkmark.png").convert_alpha()
        self.test_complete_rect = self.test_complete.get_rect(center=(
            WIDTH / 2 + HEIGHT * 5 / 10 + 145,
            HEIGHT / 2
        ))

        self.test_complete_text = pg.font.Font(None, 35).render("Test Completed", 1, 'white')
        self.test_complete_text_rect = self.test_complete_text.get_rect(center=(
            WIDTH / 2 + HEIGHT * 5 / 10 + 145,
            HEIGHT / 2 + self.test_complete.get_height() / 2 + 30
        ))

        self.surface_room_info_reset = self.text.render("Restart -> SPACE or", 1, 'white')
        self.surface_room_info_reset2 = self.text.render("MOUSE CLICK", 1, 'white')

        self.square_inner = pg.Surface((HEIGHT * 8 / 10, HEIGHT * 8 / 10))
        self.square_inner_rect = self.square_inner.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        self.square_goal = pg.Surface((HEIGHT / 10, HEIGHT / 10))
        self.square_goal.fill('red')
        self.square_goal_rect = self.square_goal.get_rect(center=(WIDTH / 2 - HEIGHT * 2 / 5, HEIGHT * 9 / 10))

        self.square_botleft_rect = pg.Surface((WIDTH / 2, HEIGHT / 2)).get_rect(topleft=(0, HEIGHT / 2))
        self.square_topleft_rect = pg.Surface((WIDTH / 2, HEIGHT / 2)).get_rect(topleft=(0, 0))
        self.square_topright_rect = pg.Surface((WIDTH / 2, HEIGHT / 2)).get_rect(topleft=(WIDTH / 2, 0))
        self.square_botright_rect = pg.Surface((WIDTH / 2, HEIGHT / 2)).get_rect(topleft=(WIDTH / 2, HEIGHT / 2))

    def reset(self):
        super().reset()
        self.state = 0

    def drawtest_surface(self):
        screen.fill((50, 168, 58))

        top_bar = pg.Surface((HEIGHT * 9 / 10, HEIGHT * 1 / 10))
        top_bar.fill('black')
        top_bar_rect = top_bar.get_rect(center=(WIDTH / 2, HEIGHT * 1 / 10))

        bot_bar = pg.Surface((HEIGHT * 9 / 10, HEIGHT * 1 / 10))
        bot_bar.fill('black')
        bot_bar_rect = bot_bar.get_rect(center=(WIDTH / 2, HEIGHT * 9 / 10))

        left_bar = pg.Surface((HEIGHT * 1 / 10, HEIGHT * 9 / 10))
        left_bar.fill('black')
        left_bar_rect = left_bar.get_rect(center=(WIDTH / 2 - (HEIGHT / 2) * 8 / 10, HEIGHT / 2))

        right_bar = pg.Surface((HEIGHT * 1 / 10, HEIGHT * 9 / 10))
        right_bar.fill('black')
        right_bar_rect = right_bar.get_rect(center=(WIDTH / 2 + (HEIGHT / 2) * 8 / 10, HEIGHT / 2))

        screen.blit(top_bar, top_bar_rect)
        screen.blit(bot_bar, bot_bar_rect)
        screen.blit(left_bar, left_bar_rect)
        screen.blit(right_bar, right_bar_rect)

        screen.blit(self.square_goal, self.square_goal_rect)

        half_length = (HEIGHT / 2) * 8 / 10
        pg.draw.line(screen, 'green', (WIDTH / 2 - half_length, HEIGHT / 2 - half_length),
                     (WIDTH / 2 + half_length, HEIGHT / 2 - half_length))
        pg.draw.line(screen, 'green', (WIDTH / 2 - half_length, HEIGHT / 2 + half_length),
                     (WIDTH / 2 + half_length, HEIGHT / 2 + half_length))
        pg.draw.line(screen, 'green', (WIDTH / 2 - half_length, HEIGHT / 2 - half_length),
                     (WIDTH / 2 - half_length, HEIGHT / 2 + half_length))
        pg.draw.line(screen, 'green', (WIDTH / 2 + half_length, HEIGHT / 2 - half_length),
                     (WIDTH / 2 + half_length, HEIGHT / 2 + half_length))

    def show_time(self):
        milis = (self.elapsed_time // 100) % 10
        secs = (self.elapsed_time // 1000) % 60
        mins = self.elapsed_time // 60000

        back = pg.draw.rect(screen, 'black', (WIDTH / 2 + HEIGHT * 5 / 10 + 20,
                                              HEIGHT * 2 / 10 - 100 - 5 + 50, 250, 130), border_radius=20)
        time_font = pg.font.Font(None, 40)
        time_text = time_font.render("Elapsed time:", 1, 'white')
        time_text_rect = time_text.get_rect(center=((back.left + back.right) / 2, back.top + 40))
        screen.blit(time_text, time_text_rect)

        time_val_mins = time_font.render("{:02} : ".format(mins), 1, 'white')
        time_val_mins_rect = time_val_mins.get_rect(topleft=(
            time_text_rect.centerx - time_val_mins.get_width() - 10,
            time_text_rect.bottom + 15
        ))
        time_val_secs = time_font.render("{:02} : ".format(secs), 1, 'white')
        time_val_secs_rect = time_val_secs.get_rect(topleft=(
            time_text_rect.centerx - 10,
            time_text_rect.bottom + 15
        ))
        time_val_milis = time_font.render("{}".format(milis), 1, 'white')
        time_val_milis_rect = time_val_milis.get_rect(topleft=(
            time_text_rect.centerx + time_val_secs.get_width() - 10,
            time_text_rect.bottom + 15
        ))
        screen.blit(time_val_mins, time_val_mins_rect)
        screen.blit(time_val_secs, time_val_secs_rect)
        screen.blit(time_val_milis, time_val_milis_rect)

    def show_score(self):
        x = WIDTH / 32 + 10
        y = HEIGHT * 6 / 18 + 100

        score_font = pg.font.Font(None, 50)
        score_text_surface = score_font.render("Accuracy:", 1, 'white')

        score_back1_surf = pg.Surface((score_text_surface.get_width() + 60, 140))
        score_back1_surf.fill('white')
        score_back1_rect = score_back1_surf.get_rect(topleft=(x - 5, y - 5))

        score_back2_surf = pg.Surface((score_text_surface.get_width() + 50, 130))
        score_back2_rect = score_back2_surf.get_rect(topleft=(x, y))

        disp = (score_back2_rect.left + score_back2_rect.right) / 2
        score_text_rect = score_text_surface.get_rect(midtop=(disp, y + 20))

        score_val = "{:.1f}".format(self.total_score)
        score_val = score_val.split('.')

        score_val_surf = score_font.render("{}.".format(score_val[0]), 1, 'white')
        score_val_rect = score_val_surf.get_rect(topright=(score_text_rect.centerx, score_text_rect.bottom + 10))

        score_dec_surf = score_font.render("{} %".format(score_val[1]), 1, 'white')
        score_dec_rect = score_dec_surf.get_rect(topright=(score_val_rect.right + score_dec_surf.get_width(),
                                                           score_text_rect.bottom + 10))

        screen.blit(score_back1_surf, score_back1_rect)
        screen.blit(score_back2_surf, score_back2_rect)
        screen.blit(score_text_surface, score_text_rect)
        screen.blit(score_val_surf, score_val_rect)
        screen.blit(score_dec_surf, score_dec_rect)

    def check_score(self):
        if self.square_inner_rect.collidepoint(self.cursor_rect.center):
            for idx, inner_surface_and_rect in enumerate(self.color_inner_list):
                if not inner_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.score = 100 - idx + 1
                    return
        else:
            for idx, outer_surface_and_rect in enumerate(self.color_outer_list):
                if outer_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.score = 100 - idx
                    return

    def calculate_penalty(self):
        if 100 >= self.score > 90:
            return 0.06
        if 90 >= self.score > 60:
            return 0.1
        if 60 >= self.score > 30:
            return 0.2
        if 30 >= self.score:
            return 0.4

    def calculate_score(self, surface_and_rect):
        brightness = surface_and_rect[0].get_alpha()
        self.check_score()
        if brightness == self.min_brightness:
            surface_and_rect[0].set_alpha(self.max_brightness)
            self.sum_score += self.score
            self.count += 1
            self.last_surface_and_score = [surface_and_rect[0], self.score]
        else:
            if self.last_surface_and_score[0] != surface_and_rect[0] or self.last_surface_and_score[1] != self.score:
                if self.penalty < 30:
                    self.penalty += self.calculate_penalty()
        if self.count != 0:
            self.total_score = self.sum_score / self.count - self.penalty
        if self.total_score < 0:
            self.total_score = 0

    def check_collisions(self):
        if self.quadrant == 1:
            for left_bot_surface_and_rect in self.collision_left_bot_surface_and_rect_list:
                if left_bot_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.calculate_score(left_bot_surface_and_rect)
                    return
            for bot_left_surface_and_rect in self.collision_bot_left_surface_and_rect_list:
                if bot_left_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.calculate_score(bot_left_surface_and_rect)
                    return

        if self.quadrant == 2:
            for left_top_surface_and_rect in self.collision_left_top_surface_and_rect_list:
                if left_top_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.calculate_score(left_top_surface_and_rect)
                    return
            for top_left_surface_and_rect in self.collision_top_left_surface_and_rect_list:
                if top_left_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.calculate_score(top_left_surface_and_rect)
                    return

        if self.quadrant == 3:
            for right_top_surface_and_rect in self.collision_right_top_surface_and_rect_list:
                if right_top_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.calculate_score(right_top_surface_and_rect)
                    return
            for top_right_surface_and_rect in self.collision_top_right_surface_and_rect_list:
                if top_right_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.calculate_score(top_right_surface_and_rect)
                    return

        if self.quadrant == 4:
            for right_bot_surface_and_rect in self.collision_right_bot_surface_and_rect_list:
                if right_bot_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.calculate_score(right_bot_surface_and_rect)
                    return
            for bot_right_surface_and_rect in self.collision_bot_right_surface_and_rect_list:
                if bot_right_surface_and_rect[1].collidepoint(self.cursor_rect.center):
                    self.calculate_score(bot_right_surface_and_rect)
                    return

    def collision_field(self):
        screen.fill((255, 255, 255))
        for sr_elem in self.collision_left_top_surface_and_rect_list:
            screen.blit(sr_elem[0], sr_elem[1])
        for sr_elem in self.collision_left_bot_surface_and_rect_list:
            screen.blit(sr_elem[0], sr_elem[1])
        for sr_elem in self.collision_right_top_surface_and_rect_list:
            screen.blit(sr_elem[0], sr_elem[1])
        for sr_elem in self.collision_right_bot_surface_and_rect_list:
            screen.blit(sr_elem[0], sr_elem[1])
        for sr_elem in self.collision_top_left_surface_and_rect_list:
            screen.blit(sr_elem[0], sr_elem[1])
        for sr_elem in self.collision_top_right_surface_and_rect_list:
            screen.blit(sr_elem[0], sr_elem[1])
        for sr_elem in self.collision_bot_left_surface_and_rect_list:
            screen.blit(sr_elem[0], sr_elem[1])
        for sr_elem in self.collision_bot_right_surface_and_rect_list:
            screen.blit(sr_elem[0], sr_elem[1])

    def scoring_field(self):
        srlist = reversed(self.color_outer_list)
        for sr_elem in srlist:
            screen.blit(sr_elem[0], sr_elem[1])
        for sr_elem in self.color_inner_list:
            screen.blit(sr_elem[0], sr_elem[1])

    def check_test_end(self):
        if self.square_goal_rect.collidepoint(self.cursor_rect.center):
            if self.visited_quadrants[1] and \
                    self.visited_quadrants[2] and \
                    self.visited_quadrants[3] and \
                    self.visited_quadrants[4]:
                return True
        return False


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    running = True

    pg.mouse.set_visible(False)

    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()

    program_state = 0
    menu_select_no = 0

    trainig = TrainingModule()
    drawtest = DrawTestModule()

    while running:
        if program_state == 0:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                    if event.key == pg.K_DOWN:
                        menu_select_no = (menu_select_no + 1) % 3
                    if event.key == pg.K_UP:
                        menu_select_no = (menu_select_no - 1) % 3
                    if event.key == pg.K_RETURN:
                        program_state = menu_select_no + 1
                        pg.mouse.set_pos(WIDTH / 2, HEIGHT / 2)
                        if program_state == 1:
                            trainig.reset()
                        if program_state == 2:
                            drawtest.reset()

            main_menu = pg.Surface((screen.get_width(), screen.get_height()))
            main_menu.fill((245, 207, 100))
            screen.blit(main_menu, (0, 0))

            menu_buttons()
            menu_info()

        elif program_state == 1:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN or \
                        event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    trainig.cursor_rect.center = (WIDTH / 2, HEIGHT / 2)
                    pg.mouse.set_pos(WIDTH / 2, HEIGHT / 2)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        program_state = 0
                    if event.key == pg.K_DOWN and trainig.level < trainig.max_level:
                        trainig.level += 1
                    if event.key == pg.K_UP and trainig.level > 0:
                        trainig.level -= 1

                if event.type == pg.MOUSEMOTION:
                    trainig.move_cursor()
                    trainig.bound_cursor()
                    check_mouse_position()

            screen.fill('black')
            training_lines()
            trainig.room_info()
            screen.blit(trainig.cursor, trainig.cursor_rect)

        elif program_state == 2:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN or\
                        event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    drawtest.state = 1
                    drawtest.start_drawing = False

                    drawtest.cursor_rect.center = (
                        WIDTH / 2 - (HEIGHT / 2) * 8 / 10,
                        HEIGHT / 2 + (HEIGHT / 2) * 8 / 10
                    )
                    pg.mouse.set_pos(WIDTH / 2, HEIGHT / 2)

                    drawtest.elapsed_time = 0
                    drawtest.start_time = pg.time.get_ticks()

                    drawtest.quadrant = 1
                    drawtest.total_score = 0
                    drawtest.count = 0
                    drawtest.sum_score = 0
                    drawtest.penalty = 0

                    for sr in drawtest.collision_left_bot_surface_and_rect_list:
                        sr[0].set_alpha(drawtest.min_brightness)
                    for sr in drawtest.collision_left_top_surface_and_rect_list:
                        sr[0].set_alpha(drawtest.min_brightness)
                    for sr in drawtest.collision_right_bot_surface_and_rect_list:
                        sr[0].set_alpha(drawtest.min_brightness)
                    for sr in drawtest.collision_right_top_surface_and_rect_list:
                        sr[0].set_alpha(drawtest.min_brightness)
                    for sr in drawtest.collision_top_left_surface_and_rect_list:
                        sr[0].set_alpha(drawtest.min_brightness)
                    for sr in drawtest.collision_top_right_surface_and_rect_list:
                        sr[0].set_alpha(drawtest.min_brightness)
                    for sr in drawtest.collision_bot_left_surface_and_rect_list:
                        sr[0].set_alpha(drawtest.min_brightness)
                    for sr in drawtest.collision_bot_right_surface_and_rect_list:
                        sr[0].set_alpha(drawtest.min_brightness)

                    drawtest.visited_quadrants[1] = False
                    drawtest.visited_quadrants[2] = False
                    drawtest.visited_quadrants[3] = False
                    drawtest.visited_quadrants[4] = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        program_state = 0
                    if event.key == pg.K_DOWN and drawtest.level < drawtest.max_level:
                        drawtest.level += 1
                    if event.key == pg.K_UP and drawtest.level > 0:
                        drawtest.level -= 1

                if event.type == pg.MOUSEMOTION:
                    drawtest.move_cursor()
                    drawtest.bound_cursor()
                    drawtest.check_collisions()
                    check_mouse_position()

            if drawtest.state == 0:
                drawtest.drawtest_surface()
                drawtest.room_info()
                transparent_banner()

            elif drawtest.state == 1:
                if not drawtest.start_drawing:
                    drawtest.start_drawing = True
                    drawtest.drawtest_surface()
                drawtest.room_info()
                drawtest.show_time()
                drawtest.show_score()
                # drawtest.scoring_field()
                # drawtest.collision_field()

                drawtest.elapsed_time = pg.time.get_ticks() - drawtest.start_time

                if drawtest.square_botleft_rect.collidepoint(drawtest.cursor_rect.center):
                    drawtest.quadrant = 1
                    drawtest.visited_quadrants[1] = True
                if drawtest.square_topleft_rect.collidepoint(drawtest.cursor_rect.center):
                    drawtest.quadrant = 2
                    drawtest.visited_quadrants[2] = True
                if drawtest.square_topright_rect.collidepoint(drawtest.cursor_rect.center):
                    drawtest.quadrant = 3
                    drawtest.visited_quadrants[3] = True
                if drawtest.square_botright_rect.collidepoint(drawtest.cursor_rect.center):
                    drawtest.quadrant = 4
                    drawtest.visited_quadrants[4] = True

                if drawtest.check_test_end():
                    drawtest.state = 2
                    file_name = str(datetime.now()).split('.')[0].replace(":", ".")
                    file_path = "./results/" + file_name + ".png"
                    if not os.path.exists("./results"):
                        os.mkdir("./results")
                    pg.image.save(screen, file_path)
                    drawtest.result_image = pg.image.load(file_path).convert_alpha()

            elif drawtest.state == 2:
                screen.blit(drawtest.result_image, (0, 0))
                drawtest.room_info()
                pg.draw.rect(screen, 'black', (
                    WIDTH / 2 + HEIGHT * 5 / 10 + 20, HEIGHT / 2,
                    250, 200
                ), border_radius=20)
                screen.blit(drawtest.test_complete, drawtest.test_complete_rect)
                screen.blit(drawtest.test_complete_text, drawtest.test_complete_text_rect)

                for n, s in enumerate(["Result saved", "Restart to try again"]):
                    s = pg.font.Font(None, 30).render(s, 1, 'white')
                    screen.blit(s, s.get_rect(center=(
                        drawtest.test_complete_text_rect.centerx,
                        drawtest.test_complete_text_rect.centery + 20 + s.get_height() * (n + 1)
                    )))

            screen.blit(drawtest.cursor, drawtest.cursor_rect)

        else:
            running = False

        pg.display.update()
        clock.tick(300)

    pg.quit()
