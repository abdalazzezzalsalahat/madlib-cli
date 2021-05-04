from madlib_cli.madlib import (__version__, read_Game, merge, parse)


def test_version():
    assert __version__ == '0.1.0'


def test_read_Game():
    expected = "banana"
    actual = read_Game("         banana      ")
    assert expected == actual

def test_merge():
    x = """
    Madlib Game
    %s on the %s and he %s from LTUC students
    so he will %s on his face.
    """
    y = ["ali","tree","afraid","hit"]
    expected = """
    Madlib Game
    ali on the tree and he afraid from LTUC students
    so he will hit on his face.
    """
    actual = merge(x,y)
    assert expected == actual


def test_parse():
    x = """
    Make Me A Video Game!

    I the %s and %s %s have %s's %s sister and plan to steal her %s %s!

    What are a %s and backpacking %s to do? Before you can help %s,
    you'll have to collect the %s %s and %s %s that open up the %s worlds connected to A %s Lair.
    There are %s %s and %s %s in the game, along with hundreds of other goodies for you to find.
    """
    
    expected = ["""
                Make Me A Video Game!

                I the \n and \n \n have \n's \n sister and plan to steal her \n \n!

                What are a \n and backpacking \n to do? Before you can help \n,
                you'll have to collect the \n \n and \n \n that open up the \n worlds connected to A \n Lair.
                There are \n \n and \n \n in the game, along with hundreds of other goodies for you to find.
                """, 
                ['%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',]]
    actual = parse(x)
    assert expected == actual


# import pytest
# from madlib_cli.madlib import read_template, parse_template, merge


# def test_read_template_returns_stripped_string():
#     actual = read_template("assets/dark_and_stormy_night.txt")
#     expected = "It was a {Adjective} and {Adjective} {Noun}."
#     assert actual == expected


# def test_parse_template():
#     actual_stripped, actual_parts = parse_template(
#         "It was a {Adjective} and {Adjective} {Noun}."
#     )
#     expected_stripped = "It was a {} and {} {}."
#     expected_parts = ("Adjective", "Adjective", "Noun")

#     assert actual_stripped == expected_stripped
#     assert actual_parts == expected_parts


# def test_merge():
#     actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
#     expected = "It was a dark and stormy night."
#     assert actual == expected


# def test_read_template_raises_exception_with_bad_path():

#     with pytest.raises(FileNotFoundError):
#         path = "missing.txt"
#         read_template(path)