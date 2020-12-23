import copy
import re
from dataclasses import dataclass, field
from pathlib import Path

testfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day7/testinput.txt')
realfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day7/puzzleinput.txt')


def get_new_bag(colour):
    return copy.deepcopy(all_bags[colour])


@dataclass
class Bag:
    colour: str = ''
    contents: dict = field(default_factory=dict)
    contained_colours: list = field(default_factory=list)
    bags: list = field(default_factory=list)
    bags_loaded: bool = False

    def load(self, inputstring):
        a = re.match(r'(?P<colour>\w+ \w+) bags contain (?P<contentlist>.*)\.', inputstring)
        self.colour = a.group('colour')
        self.contentlist = a.group('contentlist')
        for content in self.contentlist.split(','):
            v = re.match(r'(?P<count>\d+) (?P<colour>\w+ \w+) bag[s]?', content.strip())
            if v:
                self.contents[v.group('colour')] = int(v.group('count'))
                self.contained_colours.append(v.group('colour'))
                # self.contents.append(v.group('colour'))
            else:
                print(f'could not parse |{content}|')

    def contains_colour(self, inputcolour):
        if inputcolour in self.contents:
            return True
        if self.contents:
            for content in self.contents:
                containedbag = all_bags[content]
                if containedbag.contains_colour(inputcolour):
                    return True
        else:
            return

    def load_all_bags(self):
        self.bags_loaded = True
        if not self.contents:
            return

        for colour, count in self.contents.items():
            for c in range(count):
                a = get_new_bag(colour)
                self.bags.append(a)

        for b in self.bags:
            load_all_bags(b)

    def count_all_bags(self):
        if not self.bags_loaded:
            self.load_all_bags()

        if not self.bags:
            return 0

        result = 0
        for b in self.bags:
            result += 1 + count_all_bags(b)
        return result


def bags(file: Path):
    result = dict()
    with file.open('r') as f:
        for line in f.read().splitlines():
            bag = Bag()
            bag.load(line)
            result[bag.colour] = bag
    return result


all_bags = bags(testfile)


def sum_bag_colours_containing():
    result = 0
    for key, value in all_bags.items():
        if value.contains_colour('shiny gold'):
            result += 1
    return result


def load_all_bags(bag: Bag):
    if not bag.contents:
        return

    for colour, count in bag.contents.items():
        for c in range(count):
            a = get_new_bag(colour)
            bag.bags.append(a)

    for b in bag.bags:
        load_all_bags(b)


def count_all_bags(bag: Bag):
    if not bag.bags:
        return 0

    result = 0
    for b in bag.bags:
        result += 1 + count_all_bags(b)
    return result


if __name__ == '__main__':
    my_bag = get_new_bag('shiny gold')
    print(my_bag.count_all_bags())
    print(my_bag)

