import os.path
import argparse
import gzip


def main():
    parser = argparse.ArgumentParser(
               description='Parsing operator.')

    parser.add_argument('--gene_reads_file',
                        type=str,
                        help='Name of file',
                        required=True)

    parser.add_argument('--gene',
                        type=str,
                        help='Gene of interest',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='Output file name',
                        required=True)

    args = parser.parse_args()

    gene_reads_file = args.gene_reads_file
    gene = args.gene
    output_file = args.output_file

    gene_reads = read_file(gene_reads_file, gene)
    file_status = write_reads_to_file(gene_reads, output_file)
    print('Created reads ouput file: '+str(file_status))


def read_file(gene_reads_file, gene):
    version = None
    dim = None
    headers = None
    samples = {}
    sample_idx = 0
    gene_name_col = 1
    gene_reads = {}

    for l in gzip.open(gene_reads_file, 'rt'):
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if headers is None:
            headers = l.rstrip().split('\t')
            for sample in headers:
                if sample_idx == 0:
                    sample_idx += 1
                elif sample_idx == 1:
                    sample_idx += 1
                else:
                    samples[sample] = sample_idx
                    sample_idx += 1
            continue
        current_line = l.rstrip().split('\t')
        if current_line[1] == gene:
            for sample, sample_idx in samples.items():
                gene_reads[sample] = int(current_line[sample_idx])
    return gene_reads


def write_reads_to_file(gene_reads, output_file):
    out_file = open(output_file, 'w')
    for sample, read in gene_reads.items():
        out_file.write(sample+' '+str(read)+'\n')
    out_file.close()
    file_status = os.path.isfile(output_file)
    return file_status


if __name__ == '__main__':
    main()
