import random
# 設定上下界
up_bound = 100
low_bound = 0

# 產生0~100隨機數
answer = random.randint(low_bound,up_bound)
print(answer)
setBackdrop("start.png")

def onclick():
    global up_bound, low_bound
    
    guess = int(input(f"輸入數值 {low_bound} ~ {up_bound}"))
    
    if guess > low_bound and guess < up_bound:
        if guess == answer:
            up_bound = guess
            low_bound = guess
            setBackdrop("bingo.png")
        elif guess > answer:
            up_bound = guess
            setBackdrop("big.png")
        elif guess < answer:
            low_bound = guess
            setBackdrop("small.png")
    pass

def loop():
    # 顯示上下界範圍
    drawText(low_bound, 500, 770, 'black', 70)
    drawText('-', 640, 770, 'black', 70)
    drawText(up_bound, 720, 770, 'black', 70)
    pass

forever(loop)
on("click", onclick)
