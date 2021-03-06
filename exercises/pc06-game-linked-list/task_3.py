from linkedlist import LinkedList


SCORE_LIST = LinkedList()
with open("GAME.dat", 'r') as infile:
    for line in infile:
        player_id, score = line[:-1].split()
        SCORE_LIST.add(player_id.lower(), score)


def val_rank_range(rank_range, linkedlist):
    try:
        lower, upper = rank_range.split('-')  # check correct format ("X-Y")
    except:
        return False

    if (lower.isdigit() and upper.isdigit()
            and int(lower) > 0 and int(upper) > 0
            and int(lower) < int(upper)
            and int(upper) <= linkedlist.get_max_rank()):
        return True
    else:
        return False


def display_rank(linkedlist):
    if linkedlist.isEmpty():
        print("- List is empty -")
        return  # EXIT

    while True:
        rank_range = input("Enter a rank range (e.g. 1-3): ")
        if not val_rank_range(rank_range, linkedlist):
            print("\n- Invalid input -\n")
        else:
            break

    ranked_list = []  # list of tuples [(rank1, player1), (rank2, player2),...]
    rank_count = {}   # {rank1:count1, rank2:count2,...}

    lower, upper = [int(i) for i in rank_range.split('-')]

    current = linkedlist.head
    while current is not None:
        current_rank = linkedlist.get_rank(current.id)

        if current_rank >= lower and current_rank <= upper:
            ranked_list.append((current_rank, current.id))
            rank_count[current_rank] = rank_count.get(current_rank, 0) + 1
        elif current_rank > upper:
            break

        current = current.next

    # display rank & player ID header
    print("\n{0:^10}{1}{2:^15}".format("Rank", '|', "Player ID"))
    print('-'*25)

    # display rank & player ID
    for data in ranked_list:
        print("{0:^10}{1}{2:^15}".format(data[0], '|', data[1]))

    print()

    # display rank count header
    print("{0:^25}".format("Count"))
    print('-'*25)

    # display rank count
    for rank in range(lower, upper+1):
        if rank in rank_count:
            print("Rank #{0}: {1}".format(rank, rank_count[rank]))


# display_rank(SCORE_LIST)
