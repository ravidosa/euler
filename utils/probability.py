import collections

def hand_rank(hand):
    values = "23456789TJQKA"
    suits = hand[1::3]
    ranks = hand[::3]
    sorted_ranks = "".join(sorted(ranks, key=lambda c: values.index(c)))

    suit_counter = collections.Counter(suits)
    rank_counter = collections.Counter(ranks)

    suit_freq = sorted(suit_counter.values())
    rank_freq = sorted(rank_counter.values())

    if suit_freq == [5]:
        if sorted_ranks == "TJQKA":
            return ("rf")
        elif sorted_ranks in values:
            return ("sf", values.index(sorted_ranks[-1]))
        else:
            return ("fl", *sorted(map(lambda c: values.index(c[0]), rank_counter.most_common(5)), reverse=True))
    elif rank_freq == [1, 4]:
        return ("fk", values.index(rank_counter.most_common(1)[0][0]), values.index(rank_counter.most_common(2)[1][0]))
    elif rank_freq == [2, 3]:
        return ("fh", values.index(rank_counter.most_common(1)[0][0]), values.index(rank_counter.most_common(2)[1][0]))
    elif sorted_ranks in values:
        return ("st", values.index(sorted_ranks[-1]))
    elif rank_freq == [1, 1, 3]:
        return ("tk", values.index(rank_counter.most_common(1)[0][0]), *sorted(map(lambda c: values.index(c[0]), rank_counter.most_common(3)[1:]), reverse=True))
    elif rank_freq == [1, 2, 2]:
        return ("tp", *sorted(map(lambda c: values.index(c[0]), rank_counter.most_common(2)), reverse=True), values.index(rank_counter.most_common(3)[2][0]))
    elif rank_freq == [1, 1, 1, 2]:
        return ("op", values.index(rank_counter.most_common(1)[0][0]), *sorted(map(lambda c: values.index(c[0]), rank_counter.most_common(4)[1:]), reverse=True))
    else:
        return ("hc", *sorted(map(lambda c: values.index(c[0]), rank_counter.most_common(5)), reverse=True))

def compare_hand(hand1, hand2):
    rank1, rank2 = hand_rank(hand1), hand_rank(hand2)
    ranking = ["hc", "op", "tp", "tk", "st", "fl", "fh", "fk", "sf", "rf"]

    if ranking.index(rank1[0]) < ranking.index(rank2[0]):
        return 2
    elif ranking.index(rank1[0]) > ranking.index(rank2[0]):
        return 1
    else:
        if rank1 < rank2:
            return 2
        elif rank1 > rank2:
            return 1
        else:
            return 0