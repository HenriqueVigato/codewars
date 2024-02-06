def count_change(money, coins):
    result = []

    def find_conbinations(money, coins, way, result):
        if sum(way) == money:
            result.append(way.copy())
            return

        if sum(way) > money:
            return

        for n in coins:
            new_way = way + [n]
            if sorted(new_way) not in [sorted(c) for c in result]:
                find_conbinations(money, coins, new_way, result)

    find_conbinations(money, coins, [0], result)
    return len(result)


print(count_change(10, [5, 2]))
