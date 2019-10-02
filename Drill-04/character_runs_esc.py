from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 0
frame = 0
Height = 1
Direction = 0


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * Height, 100, 100, x, 80)
    update_canvas()
    frame = (frame + 1) % 8
    if (x > 800):
        Direction = 0
        Height = 0
    elif (x < 0):
        Direction = 1
        Height = 1

    if (Direction == 0):
        x -= 10
    elif (Direction == 1):
        x += 10

    delay(0.05)
    handle_events()

close_canvas()

