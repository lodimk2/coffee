# COFFEE: COnsensus single cell-type speciFic inFerence for GEnE regulatory networks

The inference of gene regulatory networks (GRNs) is crucial to understanding the regulatory mechanisms that govern biological processes. GRNs may be represented as edges in a graph, and hence have been inferred computationally for scRNA-seq data. A wisdom of crowds approach to integrate edges from several GRNs to create one composite GRN has demonstrated improved performance when compared to individual algorithm implementations on bulk RNA-seq and microarray data. In an effort to extend this approach to scRNA-seq data, we present COFFEE (COnsensus single cell-type speciFic inFerence for gEnE regulatory networks), a Borda voting based consensus algorithm that integrates information from 10 established GRN inference methods. We conclude that COFFEE has improved performance across synthetic, curated and experimental datasets when compared to baseline methods. Additionally, we show that a modified version of COFFEE can be leveraged to improve performance on newer cell-type specific GRN inference methods. Overall, our results demonstrate that consensus based methods with pertinent modifications continue to be valuable for GRN inference at the single cell level. 

## Installation Requirements

COFFEE has been tested on Python 3.8.8, and consists of a singular Python script, titled `coffee_consensus.py`. We recommend using a Python Virtual Environment, and installing the dependenceis from the corresponding requirements.txt file found in this repository. 

## Usage 

COFFEE for input requires a directory of tab separated (tsv) files, with headers of "Gene1, Gene2, EdgeWeight". It also takes as argument the desired COFFEE threshold, which is the confidence score cutoff ranging from 0 to 1. A lower threhsold includes more edges in the final consensus network, while a higher threshold includes less edges in the final consensus network. As a third argument, COFFEE accepts a path to a desired output directory. 

For output, the coffee script will create a directory and place the consensus edges ranked list as a tsv file. The directories are automatically named by the user defined COFFEE threshold. 

## Example

To test COFFEE, we provide a network from a Synthetic Dataset provided by BEELINE, in the directory titled "example_networks" (Pratapa et al. 2020). Before running COFFEE please ensure all of the requirements are met. To make sure COFFEE is able to run on your system, try the following command using the example data provided. 

`python coffee_consensus.py example_networks 0.65 {output_dir}`


## Citation

Please cite the following manuscript: {LINK MANUSCRIPT HERE ONCE ON BIORXIV}

