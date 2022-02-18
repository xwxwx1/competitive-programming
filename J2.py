gold = True                                             # if the team is a gold team
no_player = 0                                           # no. of gold players
for _ in range(int(input())):
    if 5 * int(input()) - 3 * int(input()) > 40:        # determine if is gold player
        no_player += 1
    else:
        gold = False                                    # if any player is not gold, the team is not gold
print(no_player, end='')
if gold:
    print('+')
