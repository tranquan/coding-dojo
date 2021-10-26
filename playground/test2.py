def add_rank_score(score, ranked):
    if len(ranked) == 0 or ranked[len(ranked)-1] != score:
        ranked.append(score)


def add_player_score(score, ranked):
    if len(ranked) == 0:
        ranked.append(score)
        return 1
    else:
        index = len(ranked) / 2
        for i in range(0, len(ranked)):
            index = i
            if score > ranked[i]:
                ranked.insert(i, score)
                break
            elif score == ranked[i]:
                break
            else:
                continue
    if index == len(ranked) - 1 and ranked[index] != score:
        ranked.append(score)
        index += 1
    return index + 1


def add_player_score_2(score, ranked, left, right):
    if left == right:
        if score > ranked[left]:
            ranked.insert(left, score)
            return left + 1
        elif score < ranked[left]:
            ranked.insert(left+1, score)
            return left + 2
        else:
            return left
    else:
        mid = (int)((left + right) / 2)
        if score < ranked[mid]:
            return add_player_score_2(score, ranked, mid+1, right)
        elif score > ranked[mid]:
            return add_player_score_2(score, ranked, left, mid-1)
        else:
            return mid + 1


def add_player_score_3(score, ranked):
    left = 0
    right = len(ranked) - 1

    while left != right:
        mid = (int)((left + right) / 2)
        if score < ranked[mid]:
            left = mid + 1
        elif score > ranked[mid]:
            right = mid - 1
        else:
            return mid + 1

    if score > ranked[left]:
        ranked.insert(left, score)
        return left + 1
    elif score < ranked[left]:
        ranked.insert(left+1, score)
        return left + 2
    else:
        return left


r = [100, 90, 90, 80]
p = [70, 80, 105]
rr = []
order = []

for i in range(0, len(r)):
    add_rank_score(r[i], rr)

print(rr)

dd = {}
for i in range(0, len(p)):
    key = f'{p[i]}'
    if key not in dd.keys():
        o = add_player_score_3(p[i], rr)
        order.append(o)
        dd.update(key=o)
    else:
        order.append(dd.get(key))


print(rr)
print(order)
