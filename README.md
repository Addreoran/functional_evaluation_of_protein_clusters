# Functional evaluation of protein clusters

Implementation of functional evaluation of protein clusters based on Gene Ontology enrichment. The method was initially
created to assess GBSC method clusters.

## C measure

The C-measure quantifies the quality of clustering results. It allows comparison of the functional similarity of
proteins that are grouped according to a given set of method parameters.
The implementation of the C-measure can be found in ./src/count_measures_to_clusters/measures.py.

## s measure

The s-measure allows comparison of protein sequence clusters that are annotated with Gene Ontology terms.
The implementation of the s-measure can be found in ./src/count_measures_to_clusters/measures.py.

## Tuning GBSC

The measures were created to assess the results of the GBSC method using different parameter sets. To evaluate these
parameters, we generated plots implemented in src/gbsc_plots/plots_of_multiple_method_run.py.