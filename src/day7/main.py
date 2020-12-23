import copy
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar

testfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day7/testinput.txt')
realfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day7/puzzleinput.txt')


@dataclass
class Bag:
    colour: str = ''
    content_definition_colour_to_count: dict = field(default_factory=dict)
    bags: list = field(default_factory=list)
    bags_loaded: bool = False
    flat_list_of_bags: ClassVar

    @staticmethod
    def load_all_definitions(file: Path):
        result = dict()
        with file.open('r') as f:
            for line in f.read().splitlines():
                bag = Bag()
                bag.load(line)
                result[bag.colour] = bag
        Bag.flat_list_of_bags = result

    @staticmethod
    def get_new_bag(colour: str):
        return copy.deepcopy(Bag.flat_list_of_bags[colour])

    def load(self, inputstring):
        a = re.match(r'(?P<bag_colour>\w+ \w+) bags contain (?P<bag_contents>.*)\.', inputstring)
        self.colour = a.group('bag_colour')
        for content in a.group('bag_contents').split(','):
            v = re.match(r'(?P<count>\d+) (?P<colour>\w+ \w+) bag[s]?', content.strip())
            if v:
                self.content_definition_colour_to_count[v.group('colour')] = int(v.group('count'))

    def contains_bag_of_this_colour(self, input_colour):
        if not self.bags_loaded:
            self.load_all_bags()

        for bag in self.bags:
            if bag.colour == input_colour:
                return True
            else:
                return bag.contains_bag_of_this_colour(input_colour)

    @property
    def has_bag_definitions(self):
        if self.content_definition_colour_to_count:
            return True
        return False

    def load_all_bags(self):
        self.bags_loaded = True
        if not self.has_bag_definitions:
            return

        for colour, count in self.content_definition_colour_to_count.items():
            for _ in range(count):
                self.bags.append(Bag.get_new_bag(colour))

        for bag in self.bags:
            bag.load_all_bags()

    @property
    def count_all_bags(self):}
        if not self.bags_loaded:
            self.load_all_bags()

        if not self.bags:
            return 0

        result = 0
        for bag in self.bags:
            result += 1 + bag.count_all_bags
        return result


if __name__ == '__main__':
    Bag.load_all_definitions(realfile)
    print(Bag.flat_list_of_bags)

    my_bag = Bag.get_new_bag('shiny gold')

    print(my_bag.count_all_bags)
