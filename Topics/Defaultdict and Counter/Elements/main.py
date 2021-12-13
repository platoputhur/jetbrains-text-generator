from collections import Counter

problem_string = input()
problem_string = Counter(problem_string.lower().split())
print(sorted(problem_string.elements()))
# ['a', 'alternating', 'and', 'board', 'chess', 'chessboard', 'dark', 'divided', 'draughts.', 'for', 'into', 'is', 'light', 'or', 'playing', 'sixty-four', 'square', 'squares,', 'used']