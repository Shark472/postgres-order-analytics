print("Магазин стим- покупка игры")

cash = float(input("Сколько у тебя сейчас денег?-"))
game_cash = float(input("Сколько стоит игра которую ты хочешь купить?-"))
if cash - game_cash >= 0:
    print(f"Поздравляю вы купили игру у вас осталось {cash - game_cash} денег!")
else:
    print(f"вам не хватает {game_cash - cash} денег, пополните баланс!")
print("До вствечи")