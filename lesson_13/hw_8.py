
lst = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


res = list(
    map(
        lambda line:
        (
            line[0],
            round(line[2] * line[3] + 10 if line[2] * line[3] < 100 else line[2] * line[3], 2)
        ),
        lst
    )
)
print(res)

# [163.8, 284.0, 98.85000000000001, 74.97]
# [163.8, 284.0, 108.85000000000001, 84.97]
