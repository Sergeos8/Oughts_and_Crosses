game_space = list(range(1, 10))


def welcome():  # функция, которая привествует игроков перед началом игры
    print("= = = = = = = = = = = = = = = = = = = ")
    print("       Приветствуем Вас в игре        ")
    print("   крестики-нолики для двух игроков!  ")
    print("= = = = = = = = = = = = = = = = = = = ")


def refl_game_space(game_space):  # функция, которая отображает игровое поле в формате 3 х 3
    print("Это игровое поле")
    print("-------------")
    for x in range(3):
        print("|", game_space[0+x*3], "|", game_space[1+x*3], "|", game_space[2+x*3], "|")
        print("-------------")


def users_input(player_token):  # функция, которая принимает данные, введенные пользователем и проверяет корректность их ввода.
    valid = False
    while not valid:
        player_answer = input("В какую клетку ставим  " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Неверный ввод. Необходимо ввести число.")
            continue
        if 1 <= player_answer <= 9:
            if str(game_space[player_answer-1]) not in "XO":
                print(str(game_space[player_answer-1]))
                game_space[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята. Попробуйте указать другую клетку")
        else:
            print("Неверный ввод. Необходимо ввести число от 1 до 9.")


def review_win(game_space):  # функция, которая проверяет выиграл ли игрок.
    win_cord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for j in win_cord:
        if game_space[j[0]] == game_space[j[1]] == game_space[j[2]]:
            return game_space[j[0]]
    return False


def main(game_space):  # основная функция игры, которая запускает и управляет игровым процессом.
    welcome()
    counter = 0
    win = False
    while not win:
        refl_game_space(game_space)
        if counter % 2 == 0:
            users_input("X")
        else:
            users_input("O")
        counter += 1
        if counter > 4:
            gamer = review_win(game_space)
            if gamer:
                refl_game_space(game_space)
                print(gamer, "Выиграл!")
                win = True
                break
        if counter == 9:
            print("Никто не проиграл! Попробуйте еще раз!")
            break
        refl_game_space(game_space)


main(game_space)

