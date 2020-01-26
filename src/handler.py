from solution import Solution
from extensions import *
from typing import List
from pathlib import Path
from collections import Counter


def get_dir(solution: Solution, path: Path) -> Path:
    """
    Function creates and returns path to solution

    :param solution: Solution 
    :param path: path to the directory with all solutions
    :return: path to the specific solution
    """
    return (
        path
        / solution.language
        / solution.kyu
        / solution.title.replace(r'/\<>:"|?*', "")
    )


def create_file(path: Path, content: str) -> None:
    """
    Function creates file and write some content to it

    :param path: path to the directory
    :param content: some content
    :return: None
    """
    path.touch()
    with path.open("w") as f:
        f.write(content)


def write_solutions_to_files(
    solutions: List[Solution], path: Path, folder_name: str = "CodeWars"
) -> None:
    """
    Function writes solutions to files and create directories for them 

    :param solutions: list of Solutions 
    :param path: path to the directory for creating folder with all solutions
    :param folder_name: name of folder with all solutions
    :return: None
    """
    stat = {}
    path = path / folder_name
    for solution in solutions:
        if solution.kyu in stat:
            stat[solution.kyu] += 1
        else:
            stat[solution.kyu] = 1

        path_to_solution = get_dir(solution, path)
        path_to_solution.mkdir(parents=True, exist_ok=True)

        create_file(
            path_to_solution / f"main{EXTENSIONS[solution.language]}", solution.solution
        )

        create_file(path_to_solution / "README.md", f"Link: {solution.link}")

    kuy_stat = "\n".join([f":star: {x}: {stat[x]} :star:" for x in sorted(stat)])
    create_file(
        path / "README.md",
        f"Total: {sum([stat[x] for x in stat])}\n" f"Detail statistic:\n{kuy_stat}",
    )
