import scraper
import handler

if __name__ == '__main__':
    handler.write_solutions_to_files(scraper.get_all_solutions(), r'C:\Users\Oleksandr\codewars-solutions')