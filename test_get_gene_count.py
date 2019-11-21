import unittest
import os
import random
import get_gene_counts


class TestGetGeneCounts(unittest.TestCase):

    def test_read_file(self):
        gene_reads_file = 'GTEx_Analysis_2017-06-05_v8_RNA'\
                        'SeQCv1.1.9_gene_reads.acmg_59.gct.gz'
        gene = 'MEN1'
        gene_reads = get_gene_counts.read_file(gene_reads_file, gene)
        r = gene_reads['GTEX-1117F-0226-SM-5GZZ7']
        self.assertEqual(r, 2556)

    def test_read_file_again(self):
        gene_reads_file = 'GTEx_Analysis_2017-06-05_v8_RNA'\
                        'SeQCv1.1.9_gene_reads.acmg_59.gct.gz'
        gene = 'LMNA'
        gene_reads = get_gene_counts.read_file(gene_reads_file, gene)
        r = gene_reads['GTEX-1117F-2426-SM-5EGGH']
        self.assertEqual(r, 16300)

    def test_create_file(self):
        gene_reads = {'orange': 1, 'red': 2, 'blue': 3}
        output_file = 'test_file.txt'
        r = get_gene_counts.write_reads_to_file(gene_reads, output_file)
        os.remove(output_file)
        self.assertTrue(r)

    def test_created_right_file(self):
        gene_reads = {'orange': 1, 'red': 2, 'blue': 3}
        output_file = 'test1_file.txt'
        r_dict = {}
        get_gene_counts.write_reads_to_file(gene_reads, output_file)
        f = open(output_file)
        for l in f:
            new_line = l.rstrip().split(' ')
            r_dict[new_line[0]] = new_line[1]
        f.close()
        os.remove(output_file)
        r = int(r_dict['orange'])
        self.assertEqual(r, 1)


if __name__ == '__main__':
    unittest.main()
