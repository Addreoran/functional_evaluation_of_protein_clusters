from src.count_measures_to_clusters.measures import count_s_measure, count_C_measure


class AnaliseCluster:
    def __init__(self, enrichment_file, parameter_no):
        self.file_name = enrichment_file
        self.params_no = parameter_no
        self.clusters_info = {}
        self.c_value_cl = {}
        self.C_value = None
        self.cl_no = 0

    def count_c(self):
        for e, cl_name in enumerate(self.clusters_info.keys()):
            # print(cl_name, cl_name not in self.orphans, cl_name in self.clusters_main_GO)
            self.c_value_cl[cl_name] = count_s_measure(self.clusters_info["GO_sequences"],
                                                       self.clusters_info["cluster_size"])

    def count_C(self, cl=None):
        number_of_clusters_with_at_least_one_significant_GO = self.cl_no
        number_of_clusters = len(self.clusters_info)
        self.C_value = count_C_measure(number_of_clusters_with_at_least_one_significant_GO, number_of_clusters)

    def read_enrichment_results(self):
        cl_names = set()
        with open(self.file_name) as f:
            for l in f:
                if l.strip():
                    line = l.strip().split()
                    cluster, go, go_seq_no_div_seq_no, sequence_no, go_seq_no, cl_size, cluster_go_seq_no, hypergeom_p_val, hypergeom_test, bh_value, GO_in_cl, BH_bool_test = line
                    if cl_size > 1:
                        cl_names.add(cluster)
                        if cluster not in self.clusters_info and BH_bool_test == "True":
                            self.clusters_info[cluster] = {"GO": go, "GO_sequences": go_seq_no,
                                                           "cluster_size": cl_size}
                        if self.clusters_info[cluster]["GO_sequences"] < go_seq_no:
                            self.clusters_info[cluster] = {"GO": go, "GO_sequences": go_seq_no,
                                                           "cluster_size": cl_size}
        self.cl_no = len(cl_names)

    def save(self, file):
        with open(file, "w") as f:
            f.write(f"#C measure for parameters {str(self.params_no)}: {str(self.C_value)}\n")
            f.write(f"cluster_name;main GO;seq_no;s-measure\n")
            for cluster, cluster_data in self.clusters_info.items():
                f.write(f"{cluster};{cluster_data['GO']};{cluster_data['cluster_size']};{self.c_value_cl[cluster]}\n")


if __name__ == "__main__":
    analyse_cluster = AnaliseCluster("../../data/gbsc_enrichment/cluster_enrichment", "0")
    analyse_cluster.read_enrichment_results()
    analyse_cluster.save(out_file="../../data/gbsc_enrichment/c_s_values")
