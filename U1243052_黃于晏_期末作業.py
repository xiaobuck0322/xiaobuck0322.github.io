from collections import Counter
import os

def save_winner(winner_name, filename="winners.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(winner_name + "\n")

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

def show_game_stats(scores):
    total = sum(scores.values())
    avg = total / len(scores)
    best_player, best_score = min(scores.items(), key=lambda x: x[1])

    print(f"\n📈 平均猜測次數：{avg:.2f} 次")
    print(f"🥇 最佳紀錄：{best_player}（{best_score} 次）")
