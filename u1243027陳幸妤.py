import random

answer = random.randint(1, 10)
guess = int(input("我心裡有一個 1 到 10 的數字，你猜是幾？"))

if guess == answer:
    print("猜對了！你好厲害！")
else:
    print("猜錯了，其實是", answer)
