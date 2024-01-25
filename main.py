import timeit


def find_coins_greedy(amount):
    start_amount = amount
    coin_values = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin_value in coin_values:
        coins_needed = amount // coin_value

        if coins_needed > 0:
            result[coin_value] = coins_needed
        amount -= coin_value * coins_needed

    print("\nFor ", start_amount, " cents, using greedy algorithm: ", result)


def find_min_coins(amount):
    start_amount = amount
    coin_values = [1, 2, 5, 10, 25, 50]
    dp_table = [float('inf')] * (amount + 1)
    dp_table[0] = 0

    for i in range(1, amount + 1):
        for j in range(len(coin_values)):
            coin_value = coin_values[j]
            if i >= coin_value:
                dp_table[i] = min(dp_table[i], dp_table[i - coin_value] + 1)

    result = {}
    current_amount = amount

    for coin_value in reversed(coin_values):
        while current_amount >= coin_value and dp_table[current_amount] == dp_table[current_amount - coin_value] + 1:
            result[coin_value] = result.get(coin_value, 0) + 1
            current_amount -= coin_value

    print("\nFor ", start_amount, " cents, using find_min_coins algorithm: ", result)


def main():
    amount_to_return = 1234567
    greedy_time = timeit.timeit(
        lambda: find_coins_greedy(amount_to_return), number=1)
    print("Find Coins Greedy Time:", round(greedy_time, 4), " seconds")

    min_coins_time = timeit.timeit(
        lambda: find_min_coins(amount_to_return), number=1)
    print("Find Min Coins Time:", round(min_coins_time, 4), " seconds\n")

    amount_to_return = 12345670
    greedy_time = timeit.timeit(
        lambda: find_coins_greedy(amount_to_return), number=1)
    print("Find Coins Greedy Time:", round(greedy_time, 4), " seconds")

    # min_coins_time = timeit.timeit(
    #     lambda: find_min_coins(amount_to_return), number=1)
    # print("Find Min Coins Time:", round(min_coins_time, 4), " seconds\n")
if __name__ == "__main__":
    main()
