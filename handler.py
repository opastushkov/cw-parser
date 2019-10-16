from solution import Solution
from scraping_info import *
from extensions import *
from typing import List
from os import mkdir
from os import path


def create_directory(directory_path: str, folder: str) -> None:
    root = path.join(directory_path, folder)
    if not path.exists(root):
        mkdir(root)


def create_main_readme(stat: dict, directory: str) -> None:
    with open(path.join(directory, 'README.md'), 'w') as f:
        f.write('Statistic' + '\n')
        f.write('=' + '\n')
        for i in stat.keys():
            f.write(':star:' + i + ': ' + str(stat[i]) + ':star:')
            f.write('\n')


def create_readme_for_solution(solution: Solution, directory: str) -> None:
    with open(path.join(directory, 'README.md'), 'w') as f:
        f.write(solution.title + '\n')
        f.write('=' + '\n')
        f.write('[Get more information about kata...](' + BASE_URL + solution.link + ')')


def create_file(solution: Solution, directory: str) -> None:
    with open(path.join(directory, 'Source' + EXTENSIONS[solution.language[:-1]]), 'w') as f:
        f.write(solution.solution)


def write_solutions_to_files(solutions: List[Solution], directory: str, folder_name: str = 'CodeWars') -> None:
    stat = {}
    create_directory(directory, folder_name)
    for s in solutions:
        if s.kyu in stat.keys():
            stat[s.kyu] += 1
        else:
            stat[s.kyu] = 1

        title = s.title
        title = title.rstrip()
        for i in '/\\?*:<>|".':
            title = title.replace(i, '')

        create_directory(path.join(directory, folder_name), s.language[:-1])
        create_directory(path.join(directory, folder_name, s.language[:-1]), s.kyu)
        create_directory(path.join(directory, folder_name, s.language[:-1], s.kyu), title)
        create_file(s, path.join(directory, folder_name, s.language[:-1], s.kyu, title))
        create_readme_for_solution(s, path.join(directory, folder_name, s.language[:-1], s.kyu, title))

    create_main_readme(stat, directory)
