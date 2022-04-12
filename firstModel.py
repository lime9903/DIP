import numpy as np
import pandas as pd
from scipy import io

train_data = io.loadmat("train_outlier_remove_30_not_shuffled_same_std.mat")

print(train_data[1,1])