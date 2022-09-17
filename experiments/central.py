import random

import numpy as np

from utils import create_shell_files, populate_default_scripts

if __name__ == "__main__":
    hosts = np.array([19, 20, 21, 22, 23, 24])

    all_scripts = []
    datasets = ["mnist", "fashion", "svhn"]
    algorithms = ["central"]
    default_script = f"python3 ../main.py --should_log 1"

    default_scripts_dict = populate_default_scripts(
        datasets, algorithms, default_script
    )

    all_seeds = [1588, 1693, 7089, 4488, 3776]

    for seed in all_seeds:
        for default_script_name in default_scripts_dict.keys():
            cur_name = f"runs/{default_script_name}_seed={seed}"
            script = default_scripts_dict.get(default_script_name)

            all_scripts.append(f"{script} --seed {seed} --cur_run_name {cur_name}")

    print("Number of experiments:", len(all_scripts))

    random.shuffle(all_scripts)

    create_shell_files(all_scripts, hosts, "local_epochs")
