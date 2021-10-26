import math


def add_rank_score(score, ranked):
    if len(ranked) == 0 or ranked[len(ranked)-1] != score:
        ranked.append(score)


def add_player_score(score, ranked):
    """
    We using binary search here for faster
    """
    left = 0
    right = len(ranked) - 1
    mid = math.floor((left + right) / 2)

    if ranked[left] < score:
        ranked.insert(left, score)
        return left + 1
    if ranked[right] > score:
        ranked.append(score)
        return right + 2

    while left < right:
        mid = math.floor((left + right) / 2)
        if ranked[mid] > score:
            left = mid + 1
        elif ranked[mid] < score:
            right = mid - 1
        else:
            break

    if ranked[mid] == score:
        return mid + 1

    if ranked[left] < score:
        ranked.insert(left, score)
        return left + 1
    elif ranked[left] > score:
        ranked.insert(left+1, score)
        return left + 2
    else:
        return left + 1


def climbingLeaderboard(ranked, player):
    ranked_norm = []
    for i in range(0, len(ranked)):
        add_rank_score(ranked[i], ranked_norm)

    player_rank = []
    rank_dict = {}
    for i in range(0, len(player)):
        key = player[i]
        if key not in rank_dict:
            o = add_player_score(player[i], ranked_norm)
            player_rank.append(o)
            rank_dict.update(key=o)
        else:
            player_rank.append(rank_dict.get(key))
    return player_rank
