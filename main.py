import os


def makeCommits(days: int):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('logs.txt', 'a') as file:
            file.write(f'{dates} <- testing github bot!!\n')

        os.system('git add logs.txt')

        os.system('git commit --date="' + dates + '" -m "Testing github bot!"')

        return days * makeCommits(days - 1)


makeCommits(1)
