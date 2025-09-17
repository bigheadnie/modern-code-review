def is_win(game):
    # 简化判断条件，检查是否为非空格且三个相同
    def check_line(a, b, c):
        return game[a[0]][a[1]] == game[b[0]][b[1]] == game[c[0]][c[1]] != ' '

    # 检查所有获胜组合
    return (check_line((0, 0), (0, 1), (0, 2)) or  # 第一行
            check_line((1, 0), (1, 1), (1, 2)) or  # 第二行
            check_line((2, 0), (2, 1), (2, 2)) or  # 第三行
            check_line((0, 0), (1, 0), (2, 0)) or  # 第一列
            check_line((0, 1), (1, 1), (2, 1)) or  # 第二列
            check_line((0, 2), (1, 2), (2, 2)) or  # 第三列
            check_line((0, 0), (1, 1), (2, 2)) or  # 主对角线
            check_line((0, 2), (1, 1), (2, 0)))  # 副对角线


def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    players = {'X': "Player 1", 'O': "Player 2"}  # 用字典简化玩家判断
    current_player = 'X'  # 直接用棋子标记当前玩家，更直观
    print("X = Player 1")
    print("O = Player 2")

    for n in range(9):
        # 获取并验证输入
        while True:
            print(f"{players[current_player]}: Which cell to mark? i:[1..3], j:[1..3]: ")
            try:
                i, j = map(int, input().split())
                i -= 1
                j -= 1
                # 检查坐标是否有效且单元格为空
                if 0 <= i < 3 and 0 <= j < 3 and game[i][j] == ' ':
                    break
                print("Invalid move! Please try again.")
            except ValueError:
                print("Please enter two numbers separated by space!")

        # 放置棋子
        game[i][j] = current_player

        # 检查胜负
        if is_win(game):
            print(f"{players[current_player]} wins!")
            break

        # 检查平局
        if n == 8:
            print("Tie!")

        # 显示棋盘
        for row in game:
            print(" | ".join(row))  # 增加分隔符，更清晰
        if n < 8:  # 最后一步不需要显示分隔线
            print("-" * 9)

        # 切换玩家
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()
