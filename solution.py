from dataclasses import dataclass


@dataclass
class Solution:
    """
    Class for storing solution of kata
    """
    title: str
    language: str
    link: str
    solution: str
    kyu: str
