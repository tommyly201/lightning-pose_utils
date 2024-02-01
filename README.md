# lightning-pose_utils: Lightning Pose Utilities

lightning-pose_utils provides utilities for training, analyzing, and deploying pose estimation models with a focus on efficiency and ease of use.

## Installation

First you'll have to install the lightning-pose package, which contains the base modeling code - follow the directions ([https://github.com/themattinthehatt/daart](https://github.com/danbider/lightning-pose/tree/main)). Then, in the command line, navigate to where you'd like to install the lightning-pose_utils package and move into that directory:

```bash
git clone https://github.com/tommyly201/lightning-pose_utils
cd lightning-pose_utils
pip install -r requirements.txt
```

Next, active the `lightning-pose` conda environment and locally install the `lightning-pose_utils` package.

```
$: conda activate lightning-pose
(lightning-pose) $: pip install -r requirements.txt
(lightning-pose) $: pip install -e .
```

## Set paths

To set user-specific paths that the scripts and notebooks can read from, create a file named
`lightning-pose_utils/lightning-pose/paths.py` that looks like the following:

```python

# where lightning-pose config files are stored, i.e. `data.yaml`, `model.yaml`, and `train.yaml`
config_path = '/path/to/configs'

# data path
# ---------
# for example, hand labels for a particular session are located at
#
# `data_path/output/<model_run_date>/<model_run_timestamp>/predictions_new_pixel_error.csv`
#

```

