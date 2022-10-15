# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Сумма цифр числа
def sumDigits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

# 1я функция, возращает словарь из суммы цифр и количества человек
def n_groups(n_customers):
    d = {}
    for i in range(n_customers):
        sum_dig = sumDigits(i)
        if d.get(str(sum_dig)) is None:
            d[str(sum_dig)] = 1
        else:
            d[str(sum_dig)] += 1
    return d

# 2я функция, возращает словарь из суммы цифр и количества человек
def n_groups_random(n_customers, n_first_id):
    d = {}
    for i in range(n_first_id, n_customers + n_first_id):
        sum_dig = sumDigits(i)
        if d.get(str(sum_dig)) is None:
            d[str(sum_dig)] = 1
        else:
            d[str(sum_dig)] += 1
    return d


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(n_groups(154392))
    print(n_groups_random(358000, 0))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
