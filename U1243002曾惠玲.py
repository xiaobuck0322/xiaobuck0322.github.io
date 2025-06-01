# 檔案作者：曾惠玲（U1243002）
# 功能負責：玩家名稱輸入、排行榜儲存
def get_player_names():
    players = []
    while True:
        num_players = input("請輸入玩家人數：")
        if num_players.isdigit() and int(num_players) > 0:
            num_players = int(num_players)
            break
        else:
            print("❗ 請輸入有效的正整數！")

    for i in range(num_players):
        while True:
            name = input(f"請輸入第 {i+1} 位玩家名稱：").strip()
            if name and name not in players:
                players.append(name)
                break
            else:
                print("❗ 名稱不可重複或為空，請重新輸入。")

    return players

def save_leaderboard(scores, filename="leaderboard.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write("📅 本輪排行榜紀錄：\n")
        sorted_scores = sorted(scores.items(), key=lambda x: x[1])
        for i, (name, count) in enumerate(sorted_scores, start=1):
            file.write(f"{i}. {name} - {count} 次\n")
        file.write("\n")
