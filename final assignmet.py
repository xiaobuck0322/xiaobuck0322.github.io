import random
import threading
import time
import sys
import os
from collections import Counter

# 🧠 限時輸入 + 倒數顯示
def timed_input(prompt, timeout):
    result = [None]

    def ask():
        result[0] = input(prompt)

    def countdown():
        for i in range(timeout, 0, -1):
            sys.stdout.write(f"\r⏳ 剩餘時間：{i:2d} 秒  ")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r⌛ 時間到！請稍等...        \n")

    input_thread = threading.Thread(target=ask)
    timer_thread = threading.Thread(target=countdown)

    input_thread.start()
    timer_thread.start()

    input_thread.join(timeout)

    if input_thread.is_alive():
        return None
    return result[0]

# 🎮 猜數字主邏輯（含限時）
def play_game(player_name, time_limit=20):
    answer = random.randint(1, 100)
    guess_count = 0
    print(f"\n🎯 {player_name} 的猜數字遊戲開始！（1～100，每次限時 {time_limit} 秒）")

    while True:
        guess = timed_input("請輸入你的猜測：", timeout=time_limit)

        if guess is None:
            print("⚠️ 超時，請快一點～")
            continue

        if not guess.isdigit():
            print("請輸入數字！")
            continue

        guess = int(guess)
        guess_count += 1

        if guess < answer:
            print("太小了！")
        elif guess > answer:
            print("太大了！")
        else:
            print(f"🎉 恭喜 {player_name} 猜對了！總共猜了 {guess_count} 次。")
            return guess_count

# 👥 玩家名稱輸入
def get_player_names():
    players = []
    while True:
        num_players = input("請輸入玩家人數：")
        if num_players.isdigit():
            num_players = int(num_players)
            break
        else:
            print("請輸入有效的數字！")
    
    for i in range(num_players):
        name = input(f"請輸入第 {i+1} 位玩家名稱：")
        players.append(name)
    
    return players

# 📝 排行榜儲存
def save_leaderboard(scores, filename="leaderboard.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write("📅 本輪排行榜紀錄：\n")
        sorted_scores = sorted(scores.items(), key=lambda x: x[1])
        for i, (name, count) in enumerate(sorted_scores, start=1):
            file.write(f"{i}. {name} - {count} 次\n")
        file.write("\n")

# 🏆 儲存贏家
def save_winner(winner_name, filename="winners.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(winner_name + "\n")

# 📊 勝場統計
def show_winner_stats(filename="winners.txt"):
    if not os.path.exists(filename):
        print("📂 尚無歷史勝場紀錄。")
        return
    
    with open(filename, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]
    
    if not names:
        print("📂 尚無勝場資料。")
        return
    
    counter = Counter(names)
    print("\n🏅 歷史勝場排行榜：")
    for name, count in counter.most_common():
        print(f"{name} - 勝場 {count} 次")

# 🧩 遊戲主迴圈
print("👥 歡迎進入多人猜數字遊戲！")

while True:
    players = get_player_names()
    scores = {}

    for player in players:
        tries = play_game(player, time_limit=20)
        scores[player] = tries

    # 顯示當輪排行榜
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    print("\n🏆 本輪排行榜（依猜測次數）:")
    for i, (name, count) in enumerate(sorted_scores, start=1):
        print(f"{i}. {name} - {count} 次")

    # 儲存本輪資訊
    save_leaderboard(scores)
    winner_name = sorted_scores[0][0]
    save_winner(winner_name)
    show_winner_stats()

    # 是否再玩
    again = input("\n想再玩一次嗎？（y/n）：").strip().lower()
    if again != "y":
        print("👋 感謝遊玩！排行榜與勝場紀錄已儲存。")
        break
