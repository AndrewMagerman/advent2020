from src.day7.main import *


def test_load():
    a = Bag()
    a.load('light red bags contain 1 bright white bag, 2 muted yellow bags.')
    assert a.colour == 'light red'
    assert a.contentlist == '1 bright white bag, 2 muted yellow bags'
    assert 'bright white' in a.contents
    assert 'muted yellow' in a.contents


def test_sum_bags_containing():
    assert sum_bag_colours_containing() == 4


allbags = bags(testfile)


def test_contains():
    assert all_bags['bright white'].contains_colour('shiny gold')
    assert all_bags['muted yellow'].contains_colour('shiny gold')
    assert all_bags['dark orange'].contains_colour('shiny gold')
    assert all_bags['light red'].contains_colour('shiny gold')


def test_count_contained_bags():
    assert get_new_bag('faded blue').count_all_bags() == 0
    assert get_new_bag('dotted black').count_all_bags() == 0
    assert get_new_bag('vibrant plum').count_all_bags() == 11
    assert get_new_bag('dark olive').count_all_bags() == 7
    assert get_new_bag('shiny gold').count_all_bags() == 32
