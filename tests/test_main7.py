import pytest

from src.day7.main import *


@pytest.fixture
def load_test_file():
    Bag.load_all_definitions(testfile)


def test_load(load_test_file):
    a = Bag()
    a.load('light red bags contain 1 bright white bag, 2 muted yellow bags.')
    assert a.colour == 'light red'
    assert 'bright white' in a.content_definition_colour_to_count
    assert 'muted yellow' in a.content_definition_colour_to_count


def sum_bag_colours_containing(input_colour):
    result = 0
    for colour, bag in Bag.flat_list_of_bags.items():
        if bag.contains_bag_of_this_colour(input_colour):
            result += 1
    return result


def test_sum_bags_containing(load_test_file):
    assert not Bag.get_new_bag('faded blue').has_bag_definitions
    assert sum_bag_colours_containing('shiny gold') == 4


def test_contains():
    assert Bag.get_new_bag('bright white').contains_bag_of_this_colour('shiny gold')
    assert Bag.get_new_bag('muted yellow').contains_bag_of_this_colour('shiny gold')
    assert Bag.get_new_bag('dark orange').contains_bag_of_this_colour('shiny gold')
    assert Bag.get_new_bag('light red').contains_bag_of_this_colour('shiny gold')


def test_count_contained_bags(load_test_file):
    assert Bag.get_new_bag('faded blue').count_all_bags == 0
    assert Bag.get_new_bag('dotted black').count_all_bags == 0
    assert Bag.get_new_bag('vibrant plum').count_all_bags == 11
    assert Bag.get_new_bag('dark olive').count_all_bags == 7
    assert Bag.get_new_bag('shiny gold').count_all_bags == 32
