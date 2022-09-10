import numpy as np

from utils import create_shell_files

if __name__ == "__main__":
    hosts = np.array([19, 20, 21, 22, 23, 24])

    all_scripts = []

    # FedVAE tuning (use the same values for OneFedVAE)
    algorithm = "fedvae"
    num_users = 10
    glob_epochs = 1
    alpha = 0.01
    sample_ratio = 1.0
    beta = 1.0
    classifier_num_train_samples = 5000
    decoder_num_train_samples = 5000
    use_adam = 1
    should_log = 1
    local_LR = 0.001
    decoder_LR = 0.01
    should_weight = 1

    dataset_vals = ["svhn"]
    z_dim_vals = [25, 50, 100]
    decoder_num_epochs_vals = [10, 15, 20, 40]
    classifier_num_epochs_vals = [3, 5, 7, 20]
    local_epochs_vals = [25, 40, 50, 80]
    transform_exp_vals = [0, 1]

    for dataset in dataset_vals:
        for z_dim in z_dim_vals:
            for decoder_num_epochs in decoder_num_epochs_vals:
                for classifier_num_epochs in classifier_num_epochs_vals:
                    for local_epochs in local_epochs_vals:
                        for transform_exp in transform_exp_vals:
                            all_scripts.append(
                                f"python3 ../main.py --should_log {should_log} --use_adam {use_adam} "
                                f"--algorithm {algorithm} --dataset {dataset} --num_users {num_users} --alpha {alpha} "
                                f"--sample_ratio {sample_ratio} --glob_epochs {glob_epochs} --local_epochs {local_epochs} "
                                f"--z_dim {z_dim} --beta {beta} "
                                f"--classifier_num_train_samples {classifier_num_train_samples} "
                                f"--decoder_num_train_samples {decoder_num_train_samples} "
                                f"--classifier_epochs {classifier_num_epochs} --decoder_epochs {decoder_num_epochs} "
                                f"--local_LR {local_LR} --decoder_LR {decoder_LR} --should_weight {should_weight} "
                                f"--transform_exp {transform_exp} --heterogeneous_models_exp 0"
                            )

    # # One-shot FL tuning
    # algorithm = "oneshot"
    # num_users = 10
    # glob_epochs = 1
    # alpha = 0.01
    # sample_ratio = 0.5
    # user_data_split = 0.8
    # use_adam = 1
    # should_log = 1
    #
    # dataset_vals = ["mnist", "fashion"]
    # local_epochs_vals = [5, 10, 15]
    # local_LR_vals = [0.01, 0.001, 0.0001]
    # K_vals = [3, 5, 7]
    #
    # # one_shot_sampling_vals = ["random", "data", "validation", "all"]
    # one_shot_sampling_vals = ["random", "data"]
    # for dataset in dataset_vals:
    #     for local_epochs in local_epochs_vals:
    #         for local_LR in local_LR_vals:
    #             for one_shot_sampling in one_shot_sampling_vals:
    #                 for K in K_vals:
    #                     all_scripts.append(
    #                         f"python3 ../main.py --should_log {should_log} --use_adam {use_adam} --algorithm {algorithm} "
    #                         f"--num_users {num_users} --glob_epochs {glob_epochs} --local_epochs {local_epochs} "
    #                         f"--alpha {alpha} --sample_ratio {sample_ratio} --dataset {dataset} --local_LR {local_LR} "
    #                         f"--one_shot_sampling {one_shot_sampling} --K {K}"
    #                     )
    #
    # one_shot_sampling = "validation"
    # for dataset in dataset_vals:
    #     for local_epochs in local_epochs_vals:
    #         for local_LR in local_LR_vals:
    #             for K in K_vals:
    #                 all_scripts.append(
    #                     f"python3 ../main.py --should_log {should_log} --use_adam {use_adam} --algorithm {algorithm} "
    #                     f"--num_users {num_users} --glob_epochs {glob_epochs} --local_epochs {local_epochs} --alpha {alpha} "
    #                     f"--sample_ratio {sample_ratio} --one_shot_sampling {one_shot_sampling} "
    #                     f"--user_data_split {user_data_split} --dataset {dataset} --local_LR {local_LR} --K {K}"
    #                 )
    #
    # one_shot_sampling = "all"
    # for dataset in dataset_vals:
    #     for local_epochs in local_epochs_vals:
    #         for local_LR in local_LR_vals:
    #             all_scripts.append(
    #                 f"python3 ../main.py --should_log {should_log} --use_adam {use_adam} --algorithm {algorithm} "
    #                 f"--num_users {num_users} --glob_epochs {glob_epochs} --local_epochs {local_epochs} --alpha {alpha} "
    #                 f"--sample_ratio {sample_ratio} --one_shot_sampling {one_shot_sampling} --dataset {dataset} "
    #                 f"--local_LR {local_LR}"
    #             )
    #

    # FedAvg Tuning
    algorithm = "fedavg"
    num_users = 10
    glob_epochs = 1
    alpha = 0.01
    sample_ratio = 1.0
    use_adam = 1
    should_log = 1

    dataset_vals = ["svhn"]
    local_LR_vals = [0.001]
    local_epochs_vals = [10, 15, 20, 30]

    for dataset in dataset_vals:
        for local_LR in local_LR_vals:
            for local_epochs in local_epochs_vals:
                all_scripts.append(
                    f"python3 ../main.py --should_log {should_log} --use_adam {use_adam} --algorithm {algorithm} "
                    f"--num_users {num_users} --glob_epochs {glob_epochs} --alpha {alpha} "
                    f"--sample_ratio {sample_ratio} --dataset {dataset} --local_LR {local_LR} "
                    f"--local_epochs {local_epochs}"
                )

    print("Number of experiments:", len(all_scripts))

    create_shell_files(all_scripts, hosts, "final_tuning")
