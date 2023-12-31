from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self): #객체가 생성될 때 맨 처음 자동 호출되는 함수. 객체의 초기 상태를 결정
        self.image = load_image('grass.png')

    def draw(self): #self-생성된 객체를 가리키는 더미 변수. 멤버 함수는 항상 첫 번째 인자가 self 여야 함
        self.image.draw(400,30)

    def update(self):   #기능이 있는 함수는 아니지만 더미 함수를 넣어서 코드를 통일 할 수 있기 때문에 관리 차원에서 유용하다
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
