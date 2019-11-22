import unittest
import os
import random
import box


class TestBox(unittest.TestCase):

    def test_get_gene_counts_files(self):
        tests = ['blue', 'orange', 'yellow']
        r = box.get_gene_counts_files(tests)
        s = ['blue_counts.txt', 'orange_counts.txt', 'yellow_counts.txt']
        self.assertEqual(r, s)

    def test_get_tissue_id_files(self):
        tests = ['blue', 'orange', 'yellow']
        r = box.get_tissue_id_files(tests)
        s = ['blue_ids.txt', 'orange_ids.txt', 'yellow_ids.txt']
        self.assertEqual(r, s)


if __name__ == '__main__':
    unittest.main()
