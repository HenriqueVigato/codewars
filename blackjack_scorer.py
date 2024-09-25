def score_hand(cards):
    sum_without_aces = 0
    aces = 0

    for card in cards:
        if card == "A":
            aces += 1
        elif card in ["J", "Q", "K"]:
            sum_without_aces += 10
        else:
            sum_without_aces += int(card)

    possible_sums = [sum_without_aces + aces]
    for i in range(aces):
        new_sum = sum_without_aces + i + (aces - i) * 11
        possible_sums.append(new_sum)

    valid_sums = [s for s in possible_sums if s <= 21]
    if valid_sums:
        return max(valid_sums)
    else:
        return min(possible_sums)


print(score_hand(["A", "A", "K"]))  # Deve retornar 12
print(score_hand(["10", "K"]))  # Deve retornar 20
print(score_hand(["5", "4", "3", "2", "A"]))  # Deve retornar 15
print(score_hand(["K", "Q", "J"]))  # Deve retornar 30
