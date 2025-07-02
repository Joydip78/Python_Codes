#!/bin/python3

import math
import os
import random
import re
import sys



def climbingLeaderboard(ranked, player):
    # Remove duplicates and sort descending
    ranked = sorted(set(ranked), reverse=True)
    result = []
    n = len(ranked)
    index = n - 1  # Start from the end of leaderboard

    for score in player:
        while index >= 0 and score >= ranked[index]:
            index -= 1
        result.append(index + 2)  # Rank is index+2 due to 0-based indexing
    return result


if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
