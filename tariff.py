#выводим информацию для пользователя
#получаем ввод
#проверяем корректность ввода тарифа и денег: если нет, - выводим ошибку
#проверяем, хватает ли пользователю денег: если нет, выводим пользователю о недостатке денег
#ищем сдачу: разность между балансом и ценой выбранного тарифа
#считаем количество монет
#выводим пользователю информацию об оплаченном тарифе и количестве сдачи монетами по 10, по 5, по 2, по 1

#функция обработки введенного тарифа
#если тариф "1 час" - возвращает 60, "2 часа" - 110, "5 часов" - 250, иначе - возвращает ошибку

#функция обработки внесенных денег
#если ввод является числом - возвращает число, иначе - возвращает ошибку

#функция обработки сдачи
#определяем количество монет по 10: делим сдачу на 10
#определяем остаток сдачи: ищем остаток сдачи от деления на 10
#определяем количество монет по 5: делим сдачу на 5
#определяем остаток сдачи: ищем остаток сдачи от деления на 5
#определяем количество монет по 10: делим сдачу на 2
#определяем остаток сдачи: ищем остаток сдачи от деления на 2
#определяем количество монет по 10: делим сдачу на 1
#возвращает количество монет по 10, по 5, по 2, по 1




def get_tariff_price(tariff_name):

    check_input_flag = True

    if tariff_name == "1 час":
        return 60
    
    elif tariff_name == "2 часа":
        return 110
    
    elif tariff_name == "5 часов":
        return 250
    
    else:
        check_input_flag = False
        
        return check_input_flag

def check_money_input(money):

    check_money_input_flag = True

    if money.isdigit():
        return int(money)
    
    else:
        check_money_input_flag = False

        return check_money_input_flag

def calculate_sdacha(sdacha):

    monet_10 = sdacha // 10
    sdacha = sdacha % 10

    monet_5 = sdacha // 5
    sdacha = sdacha % 5

    monet_2 = sdacha // 2
    sdacha = sdacha % 2

    monet_1 = sdacha // 1

    return monet_10, monet_5, monet_2, monet_1


def main():
    tariff_input = input("Введите название тарифа (1 час, 2 часа, 5 часов): ")
    tariff_price = get_tariff_price(tariff_input)

    if not tariff_price:
        print("Неверный тариф")
        return

    money = input("Внесите сумму денег: ")
    balance = check_money_input(money)

    if not balance:
        print("Ошибка: введено некорректное значение для суммы денег.")
        return

    if balance < tariff_price:
        print("Недостаточно средств для оплаты выбранного тарифа")
        return

    sdacha = balance - tariff_price
    
    monet_10, monet_5, monet_2, monet_1 = calculate_sdacha(sdacha)

    print(f"Оплачен тариф '{tariff_input}'. Ваша сдача: {monet_10} по 10 руб., {monet_5} по 5 руб., {monet_2} по 2 руб., {monet_1} по 1 руб.")

if __name__ == "__main__":
    main()

