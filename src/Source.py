from scraper import get_all_solutions
from handler import write_solutions_to_files
from pathlib import Path

if __name__ == "__main__":
    solutions = get_all_solutions(
        login=input("Enter a login from CodeWars account: "),
        password=input("Enter a password from CodeWars account: "),
    )

    write_solutions_to_files(solutions, Path.cwd())
