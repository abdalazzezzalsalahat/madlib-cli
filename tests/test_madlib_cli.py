from madlib_cli.madlib import *


def test_parse():
    madlib('assets/Game.txt', 'y')
    assert "Make Me A Video Game!\n\nI the  and   have 's  sister and plan to steal her  !\n\nWhat are a  and backpacking  to do? Before you can help , you'll have to collect the   and   that open up the  worlds connected to A  Lair. There are   and   in the game, along with hundreds of other goodies for you to find."



def test_read_file():
    actual = read_template("assets/stormy_test_file.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected