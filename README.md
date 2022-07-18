# FedVAE

### Description
This project implements a variety of Federated Learning models as well as a novel model FedVAE.

### Prerequisites
1. Python 3.9.x+
2. `pip`

### Set up
Install Python 3.9 and `pip`. We recommend using the package pyenv, which is described in this article.
Create and enter a new virtual environment and run:
```
pip3 install -r requirements.txt
```
This will install the necessary dependencies.

### Algorithms
#### FedAvg
Run the following from command line.
```
python3 main.py --algorithm fedavg --dataset mnist --num_users 10 --alpha 0.1 --sample_ratio 0.5 --glob_epochs 5 --local_epochs 1 --should_log True
```

#### One-shot ensembled FL
Run the following from command line.
```
python3 main.py --algorithm oneshot --num_users 5 --alpha 1.0 --sample_ratio 0.1 --local_epochs 5 --should_log True --one_shot_sampling random --user_data_split 0.9 --K 3
```
`--one_shot_sampling` can take on the following values:
- `random` (sample a random subset of K users to ensemble)
- `validation` (split each user's data into training and validation and choose the K best scoring user models on the validation set)
- `data` (choose the K users with the most data)
- `all` (ensemble all user models)

You can also adjust model specific parameters `--K` to adjust how many users are sampled for ensembling and `--user_data_split` to adjust the user train/validation split.


### Logging
1. Enable logging by adding the command line argument `--should_log True` to `python3 main.py`.
2. Run `tensorboard --logdir=runs` and navigate to [http://localhost:6006/](http://localhost:6006/).

### Format
1. Run `black .` from the repo root.
2. Run `isort .` also from the repo root.

### Multi-GPU Example
https://pytorch.org/tutorials/beginner/former_torchies/parallelism_tutorial.html
