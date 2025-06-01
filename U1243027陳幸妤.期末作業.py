import random

def play_game(player_name, time_limit=20):
    answer = random.randint(1, 100)
    guess_count = 0
    print(f"\n🎯 {player_name} 的猜數字遊戲開始！（1～100，每次限時 {time_limit} 秒）")

    while True:
        guess = timed_input("請輸入你的猜測：", timeout=time_limit)

        if guess is None:
            print("⚠️ 超時，請快一點～")
            continue

        if not is_valid_number(guess):
            print("❗ 請輸入 1 到 100 的整數！")
            continue

        guess = int(guess)
        guess_count += 1

        if guess < answer:
            print("📉 太小了！")
        elif guess > answer:
            print("📈 太大了！")
        else:
            print(f"🎉 恭喜 {player_name} 猜對了！總共猜了 {guess_count} 次。")
            return guess_count
