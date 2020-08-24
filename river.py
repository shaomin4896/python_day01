import game
# 角色設定及初始化
bg = game.create_sprite("bg2.jpg","bg3.jpg","bg4.jpg") 
player = game.create_sprite("1.png","2.png","3.png") 
def pullLeft():
    player.x -= 10
    if player.x < 280:
        bg.costume_id = 1
        player.costume_id = 1
        stop()
        
def pullRight():
    player.x += 10
    if player.x > 360:
        bg.costume_id = 2
        player.costume_id = 2
        stop()
# space按下判斷
on("keydown", "space", pullLeft)

# enter按下判斷
on("keydown", "enter", pullRight)