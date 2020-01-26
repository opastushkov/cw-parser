from typing import List
from scraping_info import *
from requests import Session
from solution import Solution
from bs4 import BeautifulSoup


def get_token(s: Session) -> str:
    """
    Function gets token from page

    :param s: Session
    :return: token
    """
    auth_page = BeautifulSoup(
        s.get(url=f"{BASE_URL}users/sign_in", headers=HEADERS,).text,
        features="html.parser",
    )

    token = auth_page.find("input", {"name": "authenticity_token"}).get("value")

    return token


def authorization(s: Session, token: str, login: str, password: str) -> None:
    """
    Function for authorization on Code Wars

    :param s: Session
    :param token: authenticity token
    :return: None
    """
    s.post(
        url=f"{BASE_URL}users/sign_in",
        headers=HEADERS,
        data={
            **DATA,
            "user[email]": login,
            "user[password]": password,
            "authenticity_token": token,
        },
    )


def get_page_with_solutions(s: Session, page_number: int) -> BeautifulSoup:
    """
    Function gets page with kata' solutions

    :param s: Session
    :param page_number: number of page with solutions
    :return: page with solution in BS format
    """
    page_with_solutions = BeautifulSoup(
        s.get(
            url=f"{BASE_URL}users/{USERNAME}/completed_solutions?"
            f"page={page_number}",
            headers=HEADERS,
        ).text,
        features="html.parser",
    )

    return page_with_solutions


def get_solutions(page: BeautifulSoup) -> List[BeautifulSoup]:
    """
    Function returns list with solutions from page in BS format

    :param page: page with solutions
    :return: list with solutions in BS format
    """

    return page.find_all("div", {"class": "list-item solutions"})


def parse_solutions(solutions_list) -> List[Solution]:
    """
    Function returns list with solutions from page

    :param solutions_list: list with solutions in BS format
    :return: list with solutions
    """

    return [
        Solution(
            s.find("a").next,
            s.find("h6").next[:-1],
            s.find("a").get("href"),
            s.find("code").next,
            s.find("span").next,
        )
        for s in solutions_list
    ]


def get_all_solutions(login: str, password: str) -> List[Solution]:
    """
    Function returns list with all solutions

    :return: all solutions
    """
    with Session() as session:
        authenticity_token = get_token(session)
        authorization(session, authenticity_token, login, password)

        HEADERS["Authorization"] = authenticity_token
        HEADERS["X-Requested-With"] = "XMLHttpRequest"

        it = 0
        solutions = []
        while True:
            page_with_solutions = get_page_with_solutions(session, it)
            solutions_from_page = get_solutions(page_with_solutions)
            solutions += parse_solutions(solutions_from_page)

            if not page_with_solutions.find("h5"):
                break

            it += 1

        return solutions
