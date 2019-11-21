import unittest
import os
import random
import get_tissue_samples


class TestGetTissueSamples(unittest.TestCase):

    def test_read_file(self):
        sample_attributes_file = 'GTEx_Analysis_v8_Annotations'\
                                '_SampleAttributesDS.txt'
        tissue_group = 'Brain'
        sample_ids = get_tissue_samples.get_sample_ids(
            sample_attributes_file, tissue_group)
        r = len(sample_ids)
        self.assertEqual(r, 3326)

    def test_create_file(self):
        sample_ids = ['orange', 'red', 'blue']
        output_file = 'test_file.txt'
        r = get_tissue_samples.write_ids_to_file(sample_ids, output_file)
        os.remove(output_file)
        self.assertTrue(r)

    def test_created_right_file(self):
        sample_ids = ['orange', 'red', 'blue']
        output_file = 'test1_file.txt'
        r_ids = []
        get_tissue_samples.write_ids_to_file(sample_ids, output_file)
        f = open(output_file)
        for l in f:
            r_ids.append(l.rstrip())
        f.close()
        os.remove(output_file)
        r = ('orange' in r_ids)
        self.assertTrue(r)


if __name__ == '__main__':
    unittest.main()
