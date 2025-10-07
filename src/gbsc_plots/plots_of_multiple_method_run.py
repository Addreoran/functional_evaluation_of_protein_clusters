from matplotlib import pyplot as plt


def get_params(path):
    params = {}
    with open(path) as f:
        for l in f:
            if l:
                if "#" in l:
                    last_params = l.replace("#", "").strip().replace("[", "").replace("]", "").split("_")[-1]
                if "GBSC_ALGORITHM_PARAMS" in l:
                    params_list = l.split("=")[-1].replace('"', '').strip().split(" ")
                    # print(params_list)
                    params[str(last_params.split("_")[-1])] = {
                        "w": int(params_list[1]),
                        "l": int(params_list[3]),
                        "g": int(params_list[5]),
                        "m": int(params_list[7]),
                        "x": int(params_list[9])
                    }
    if str(last_params.split("_")[-1]) not in params:
        params[str(last_params.split("_")[-1])] = {
            "w": int(params_list[1]),
            "l": int(params_list[3]),
            "g": int(params_list[5]),
            "m": int(params_list[7]),
            "x": int(params_list[9])
        }
    return params


def plot_C_value_vs_mean_seq_len_in_cl(path, data, data_len, params, parameter):
    xpoints = {}
    ypoints = {}
    for set_no, parameters_set in params.items():
        if set_no not in xpoints:
            xpoints[set_no] = []
            ypoints[set_no] = []
        xpoints[set_no].append(float(data[set_no]))
        ypoints[set_no].append(float(data_len[set_no]))
    # print(xpoints.keys())
    for param, list_params in xpoints.items():
        plt.plot(list_params, ypoints[param], 'o', label=param)
    plt.legend()
    plt.xticks(rotation=45)
    plt.xlabel("C value")
    plt.rc('xtick', labelsize=8)  # fontsize of the tick labels

    plt.ylabel("Mean len of sequences in clusters")
    plt.title(f"Plot C value-mean len of seq in cl by '{parameter}' parameter")

    # plt.show()
    plt.savefig(path)
    plt.close()


def plot_C_value_vs_mean_seq_in_cl(path, data, data_no, params, parameter):
    xpoints = {}
    ypoints = {}
    for set_no, parameters_set in params.items():
        if set_no not in xpoints:
            xpoints[set_no] = []
            ypoints[set_no] = []
        xpoints[set_no].append(float(data[set_no]))
        ypoints[set_no].append(float(data_no[set_no]))
    for param, list_params in xpoints.items():
        plt.plot(list_params, ypoints[param], 'o', label=param)
    plt.legend()
    plt.xticks(rotation=45)
    plt.rc('xtick', labelsize=8)  # fontsize of the tick labels

    plt.xlabel("C value")
    plt.ylabel("Mean number of sequences in clusters")
    plt.title(f"Plot C value-mean number of seq in cl by '{parameter}' parameter")
    plt.savefig(path)
    plt.close()


def read_stats_of_clusters(path):
    result = {}
    with open(path) as f:
        for l in f:
            line = l.strip()
            if line:
                line = line.split(";")
                result[line[0]] = line[1]
    return result


def main():
    params_path = "./data/tuning_params"
    params_length_of_sequences_path = "./data/length_of_sequences_by_parameters.csv"
    params_no_of_sequences_path = "./data/no_of_sequences_by_parameters.csv"
    c_measure_path = "./data/C_value_by_parameters.csv"
    params = get_params(params_path)
    data_len = read_stats_of_clusters(params_length_of_sequences_path)
    data_no = read_stats_of_clusters(params_no_of_sequences_path)
    information_additional = read_stats_of_clusters(c_measure_path)
    for param in ["w", "l", "g", "m", "x"]:
        plot_C_value_vs_mean_seq_len_in_cl(f"./result/plot_C_value_vs_mean_seq_len_in_cl_{param}.png",
                                           information_additional,
                                           data_len, params, param)
        plot_C_value_vs_mean_seq_in_cl(f"./result/plot_C_value_vs_mean_seq_in_cl_{param}.png",
                                       information_additional, data_no, params, param)
