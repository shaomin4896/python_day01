import game

road = game.create_sprite('road.jpg')
p1 = game.create_sprite('r_0.png', 'r_1.png')
p2 = game.create_sprite('g_0.png', 'g_1.png')
p3 = game.create_sprite('b_0.png', 'b_1.png')
p1_rank = game.create_sprite('1.png', '2.png', '3.png')
p2_rank = game.create_sprite('1.png', '2.png', '3.png')
p3_rank = game.create_sprite('1.png', '2.png', '3.png')

p1.move_to(600, 350)
p2.move_to(600, 450)
p3.move_to(600, 550)
p1_rank.move_to(1200, 430)
p2_rank.move_to(1200, 540)
p3_rank.move_to(1200, 650)

p1_rank.hidden = p2_rank.hidden = p3_rank.hidden = True

p1_steps = 0
p2_steps = 0
p3_steps = 0
rank = 0

game.create_sound('bgm.mp3', True)

def p1_right():
    global p1_steps
    if p1.costume_id == 0:
        p1.costume_id = 1
        p1_steps += 30

def p1_left():
    global p1_steps
    if p1.costume_id == 1:
        p1.costume_id = 0
        p1_steps += 30

def p2_right():
    global p2_steps
    if p2.costume_id == 0:
        p2.costume_id = 1
        p2_steps += 30

def p2_left():
    global p2_steps
    if p2.costume_id == 1:
        p2.costume_id = 0
        p2_steps += 30
        
def p3_right():
    global p3_steps
    if p3.costume_id == 0:
        p3.costume_id = 1
        p3_steps += 30

def p3_left():
    global p3_steps
    if p3.costume_id == 1:
        p3.costume_id = 0
        p3_steps += 30
        
def loop():
    global rank
    offset = max(p1_steps, p2_steps, p3_steps)
    road.x = 1600 - offset
    p1.x = 600 - offset + p1_steps
    p2.x = 600 - offset + p2_steps
    p3.x = 600 - offset + p3_steps
    
    if p1_steps > 2000 and p1_rank.hidden:
        p1_rank.hidden = False
        p1_rank.costume_id = rank
        rank += 1
        game.create_sound('applause.wav')
    
    if p2_steps > 2000 and p2_rank.hidden:
        p2_rank.hidden = False
        p2_rank.costume_id = rank
        rank += 1
        game.create_sound('applause.wav')
    
    if p3_steps > 2000 and p3_rank.hidden:
        p3_rank.hidden = False
        p3_rank.costume_id = rank
        rank += 1
        game.create_sound('applause.wav')

game.on('keydown', 'z', p1_right)
game.on('keydown', 'x', p1_left)
game.on('keydown', 'n', p2_right)
game.on('keydown', 'm', p2_left)
game.on('keydown', 'right', p3_right)
game.on('keydown', 'left', p3_left)
game.forever(loop)
