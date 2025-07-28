# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                if item.name  == "Aged Brie":
                    item.quality += 1
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 0:
                        item.quality = 0
                    elif item.sell_in <= 5:
                        item.quality += 3
                    elif item.sell_in <= 10:
                        item.quality += 2
                    else:
                        item.quality += 1

                else: # default item
                    item.quality = item.quality - 2 if item.sell_in < 0 else item.quality - 1
                    if item.quality <= 0:
                        item.quality = 1

                if item.quality > 50:
                    item.quality = 50
                item.sell_in = item.sell_in - 1