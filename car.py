# 設定場景背景及設定角色
game.set_backdrop("border.jpg")
end = game.create_sprite("e.png")
grass = game.create_sprite("grass.png")
end.direction = 0
end.y = 40
end.x = 450
# 建立car1及初始化
car1 = game.create_sprite("car_red.png") #創造角色
car1.direction = 270
car1.y = 20
car1.x = 340
# 建立car2及初始化
car2 = game.create_sprite("car_blue.png") #創造角色
car2.direction = 270
car2.y = 50
car2.x = 340
def loop ():
    # car1左右控制
    if key.left:
        car1.direction -= 4
    if key.right:
        car1.direction += 4
    # car1速度設定
    if car1.touched(grass):
        car1.step_forward(0.3)    
    else:
        car1.step_forward(2.5)
    # car2左右控制
    if key.a:
        car2.direction -= 4
    if key.d:
        car2.direction += 4
    # car2速度設定
    if car2.touched(grass):
        car2.step_forward(0.3)    
    else:
        car2.step_forward(2.5)
    # 遊戲結束
    if car1.touched(end) or car2.touched(end):
        stop()
    pass
forever(loop)