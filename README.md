cw-parser
===================

cw-parser - web scraper for [CodeWars](https://www.codewars.com/). Script downloads all solutions from your account and saves them on your PC.

Features
--------
cw-parser creates README.md for each solution. And furthermore, script generates README.md for root folder with all solutions. Main README contains statistics on solved katas and them kyus. cw-parser separates all solutions by languages and kyus (see folders tree below)

<img align="center" src="https://user-images.githubusercontent.com/52821952/73137417-4e205000-4060-11ea-8529-2bde371f120c.png">

Installation and usage
---------------------
1. Clone this repository
```
git clone https://github.com/opastushkov/cw-parser.git
```
2. Create virtual environment, activate it and install all necessary packages
```
python3.7 -m venv venv
source src/bin/activate
pip install requirements.txt
```
3. Run Source.py
```
python Source.py
```
4. Enter your credentials for CodeWars

5. Profit!

Example
-------
Result of work you can see in [this reposiroty](https://github.com/opastushkov/codewars-solutions)