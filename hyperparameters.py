# hyperparameters.py

import numpy as np
import tensorflow as tf

# File paths
path = 'C:/Users/ideapad 5 15ITL05/Desktop/TFM/Notebooks/Datasets/'
path_era_slp_entry = 'slp_ERA20_1900-2010.nc'
path_era_slp_output = 'psl_1m_ERA5_197901_202012_grid1.nc'
path_had_sst = 'HadISST1_sst_1870-2019.nc'

# Time limits
time_lims = [1900, 2020]

# SLP limits
lat_lims_slp = [70, 20]
lon_lims_slp = [-40, 30]

# SST limits
lat_lims_sst = [55, -20]
lon_lims_sst = [-70, 20]

# SLP months
months_slp = [1, 2, 12]

# Years
years = np.arange(1900, 2021, 1)

# SLP months to skip
months_skip_slp = ['1900-01', '1900-02', '2020-12']

# Years for SLP finally
years_finally_slp = np.arange(1900, 2020, 1)

# Reference period
reference_period = [1950, 2000]

# SST months
months_sst = [9, 10, 11]

# SST months to skip
months_skip_sst = [None]

# Train, validation, and testing years
train_years = [1900, 1990]
validation_years = [1991, 1999]
testing_years = [2000, 2020]

# Neural network hyperparameters
layer_sizes = [1024, 256, 64]
activations = [tf.keras.activations.linear, tf.keras.activations.linear, tf.keras.activations.linear]
dropout_rates = [0.05]
kernel_regularizer = 'l1_l2'
learning_rate = 0.0001
epochs = 2500

# Plotting parameters
mapbar = 'bwr'
titulo1 = 'Comparison of DJF anomalies SLP'
titulo2 = 'SST anomaly'
subtitulo1 = 'Predictions'
periodo = 'SON'
subtitulo2 = 'Observations'
unidades = 'hPa'
titulo_corr= 'Atlantic'

# Regions of interest
lon_nino3, lat_nino3 = [-150, -90], [5, -5]
lon_iceland, lat_iceland = [-40, -20], [70, 60]
lon_macaronesian, lat_macaronesian = [-40, -20], [40, 20]
Azores, icelandia = [35, 335], [64.136319, 360-21.948231]

# Outputs path
outputs_path = "C:/Users/ideapad 5 15ITL05/Desktop/TFM/Notebooks/Outputs/sst_son_slp_djf_Atlantico_with_ERA5/"