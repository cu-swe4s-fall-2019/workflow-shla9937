import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(
            description='Parsing operator.')

    parser.add_argument('--genes',
                        nargs='+',
                        type=str,
                        help='Names of genes',
                        required=True)

    parser.add_argument('--tissues',
                        nargs='+',
                        type=str,
                        help='Names of tissues',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='Output file name',
                        required=True)

    args = parser.parse_args()

    genes = args.genes
    tissues = args.tissues
    output_file = args.output_file

    gene_counts_files = get_gene_counts_files(genes)
    tissue_id_files = get_tissue_id_files(tissues)
    tissue_samples = make_tissue_samples(tissue_id_files)
    box_data = make_box_data(gene_counts_files, tissue_samples)
    boxplot(box_data, tissues, output_file)


def get_gene_counts_files(genes):
    gene_counts_files = []
    for gene in genes:
        gene_counts_files.append(gene+'_counts.txt')
    return gene_counts_files


def get_tissue_id_files(tissues):
    tissue_id_files = []
    for tissue in tissues:
        tissue_id_files.append(tissue+'_ids.txt')
    return tissue_id_files


def make_tissue_samples(tissue_id_files):
    tissue_samples = []
    for tissue_file in tissue_id_files:
        current_tissue = []
        current_tissue.append(tissue_file.rstrip('ids.txt').rstrip('_'))
        for line in open(tissue_file, 'r'):
            current_tissue.append(line.rstrip())
        tissue_samples.append(current_tissue)
    return tissue_samples


def make_box_data(gene_counts_files, tissue_samples):
    box_data = []
    for tissue_ids in tissue_samples:
        tissue = []
        tissue.append(tissue_ids[0])
        for gene_file in gene_counts_files:
            gene_data = []
            gene_name = gene_file.rstrip('_counts.txt')
            gene_data.append(gene_name)
            for line in open(gene_file, 'r'):
                current_line = line.rstrip().split()
                if current_line[0] in tissue_ids:
                    gene_data.append(current_line[1])
                else:
                    continue
            tissue.append(gene_data)
        box_data.append(tissue)
    return box_data


def boxplot(box_data, tissues, output_file):
    num_plots = len(tissues)
    fig, ax = plt.subplots(num_plots, 1)
    fig.subplots_adjust(hspace=1.5)

    plot_counter = 0
    for data in box_data:
        big_counter = 0
        tick_labels = []
        plotting_data = []
        for tissue in data:
            if big_counter == 0:
                ax[plot_counter].set_title(tissue)
                big_counter += 1
            else:
                counter = 0
                current_gene_counts = []
                for gene_counts in tissue:
                    if counter == 0:
                        tick_labels.append(gene_counts)
                        counter += 1
                    else:
                        current_gene_counts.append(float(gene_counts))
                plotting_data.append(current_gene_counts)

        ax[plot_counter].spines['right'].set_visible(False)
        ax[plot_counter].spines['top'].set_visible(False)
        ax[plot_counter].set_ylabel('Counts')
        ax[plot_counter].set_xticklabels(tick_labels, rotation='horizontal')
        ax[plot_counter].boxplot(plotting_data)
        plot_counter += 1
    plt.savefig(output_file, bbox_inches='tight')


if __name__ == '__main__':
    main()
