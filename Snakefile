TISSUES = ['Brain', 'Heart', 'Blood', 'Skin']
GENES = ['SDHB', 'MEN1', 'KCNH2', 'MSH2', 'MYL2', 'BRCA2']
TISSUES_GENES = []
TISSUE_LIST = '-'.join([(p) for p in TISSUES])
GENE_LIST = '-'.join([(p) for p in GENES])
TISSUES_GENES.append(TISSUE_LIST)
TISSUES_GENES.append(GENE_LIST)

rule all:
    input:
        '_'.join([(p) for p in TISSUES_GENES]) + '.png'

rule boxplot:
    input:
        expand("{gene}_counts.txt", gene=GENES),
        expand("{tissue}_ids.txt", tissue=TISSUES),
    output:
        '_'.join([(p) for p in TISSUES_GENES]) + '.png'
    shell:
        'python box.py ' \
        + '--tissues ' + ' '.join([(p) for p in TISSUES]) \
        + ' --genes ' + ' '.join([(p) for p in GENES]) \
        + ' --output_file {output}'

rule tissue_ids:
    input:
        "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"
    output:
        expand("{tissue}_ids.txt", tissue=TISSUES)
    shell:
        "for tissue in {TISSUES}; do " \
        + "python get_tissue_samples.py --sample_attributes_file {input} --tissue $tissue --output_file $tissue\_ids.txt;"\
        + "done"

rule sample_tissue_data:
    output:
        "GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"
    shell:
        "wget https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"

rule gene_sample_counts:
    input:
        "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"
    output:
        expand("{gene}_counts.txt", gene=GENES)
    shell:
        "for gene in {GENES}; do " \
        +   "python get_gene_counts.py --gene_reads_file {input} --gene $gene --output_file $gene\_counts.txt;" \
        + "done"
        
rule gene_data:
    output:
        "GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"
    shell:
        "wget https://github.com/swe4s/lectures/raw/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"