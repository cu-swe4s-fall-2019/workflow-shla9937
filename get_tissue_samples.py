import os.path
import argparse
import gzip


def main():
    parser = argparse.ArgumentParser(
               description='Parsing operator.')

    parser.add_argument('--sample_attributes_file',
                        type=str,
                        help='Name of file',
                        required=True)

    parser.add_argument('--tissue_group',
                        type=str,
                        help='Tissue of interest',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='Output file name',
                        required=True)

    args = parser.parse_args()

    sample_attributes_file = args.sample_attributes_file
    tissue_group = args.tissue_group
    output_file = args.output_file

    sample_ids = get_sample_ids(sample_attributes_file, tissue_group)
    file_status = write_ids_to_file(sample_ids, output_file)
    print('Created ids output file: '+str(file_status))


def get_sample_ids(sample_attributes_file, tissue_group):
    headers = None
    headers_dict = {}
    sample_ids = []
    header_idx = 0

    f = open(sample_attributes_file, 'rt')
    for l in f:
        if headers is None:
            headers = l.rstrip().split('\t')
            for header in headers:
                headers_dict[header] = header_idx
                header_idx += 1
            continue
        current_line = l.rstrip().split('\t')
        if current_line[headers_dict['SMTS']] == tissue_group:
            sample_ids.append(current_line[0])
    f.close()
    return sample_ids


def write_ids_to_file(sample_ids, output_file):
    out_file = open(output_file, 'w')
    for id in sample_ids:
        out_file.write(id+'\n')
    out_file.close()
    file_status = os.path.isfile(output_file)
    return file_status


if __name__ == '__main__':
    main()
