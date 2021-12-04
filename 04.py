# 540/582
# 14:31/19:40
from sys import stdin
from re import split

lines = list(stdin.read().strip().split('\n'))
nums = list(map(int, lines[0].split(',')))
boards = [list(map(lambda line: list(map(int, split('\s+', line.strip()))), lines[i:i+5]))
    for i in range(2, len(lines), 6)]

called, scores = set(), []
won = lambda board: any(all(board[y][x] in called for x in range(5)) for y in range(5)) or any(
    all(board[y][x] in called for y in range(5)) for x in range(5))
score = lambda board, x: x * sum(n for row in board for n in row if n not in called)

for n in nums:
    called.add(n)
    for winner in [board for board in boards if won(board)]:
        scores.append(score(winner, n))
        boards.remove(winner)

print('a', scores[0])
print('b', scores[-1])
