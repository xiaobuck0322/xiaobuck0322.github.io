def main():
    print("👥 歡迎進入多人猜數字遊戲！")

    try:
        while True:
            players = get_player_names()
            scores = {}

            for player in players:
                tries = play_game(player, time_limit=20)
                scores[player] = tries

            sorted_scores = sorted(scores.items(), key=lambda x: x[1])
            print("\n🏆 本輪排行榜（依猜測次數）:")
            for i, (name, count) in enumerate(sorted_scores, start=1):
                print(f"{i}. {name} - {count} 次")

            show_game_stats(scores)

            save_leaderboard(scores)
            winner_name = sorted_scores[0][0]
            save_winner(winner_name)
            show_winner_stats()

            again = input("\n想再玩一次嗎？（y/n）：").strip().lower()
            if again != "y":
                print("👋 感謝遊玩！排行榜與勝場紀錄已儲存。")
                break

    except KeyboardInterrupt:
        print("\n🛑 中斷遊戲，感謝您的參與！")
        sys.exit(0)

