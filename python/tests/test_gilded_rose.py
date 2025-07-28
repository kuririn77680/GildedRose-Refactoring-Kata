# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 2),
                 Item("Backstage passes to a TAFKAL80ETC concert", 7, 30),
                 Item("Sulfuras, Hand of Ragnaros", 0, 80),
                 Item("Aged Brie", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[2].name)
        self.assertEqual(0, items[2].sell_in)
        self.assertEqual(80, items[2].quality)

        self.assertEqual("foo", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
        self.assertEqual(6, items[1].sell_in)
        self.assertEqual(32, items[1].quality)

        self.assertEqual("Aged Brie", items[3].name)
        self.assertEqual(1, items[3].sell_in)
        self.assertEqual(11, items[3].quality)



        
if __name__ == '__main__':
    unittest.main()
