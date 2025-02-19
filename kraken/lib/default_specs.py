#
# Copyright 2020 Benjamin Kiessling
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.
"""
Default VGSL specs and hyperparameters
"""

# 1,1000,0,3 batch of 1, height=1000, 0 width (variable), 3 channels
# cr7,7,64,2,2: 7x7x64 convolution (relu) with 2x2 stride 
# Gn32: group normalization (32 groups, each normalized separately)
# cr3,3,128,2,2: 7x7x64 convolution (relu) with 2x2 stride 
# Gn32: group normalization 
# ... (series of 3x3 conv., with 256 features maps as an output) ...
# Lbx32: recurrent layer (x-axis).
# Lby32: recurrent layer (y-axis).
# Cr1,1,32: 

SEGMENTATION_SPEC = '[1,1800,0,3 Cr7,7,64,2,2 Gn32 Cr3,3,128,2,2 Gn32 Cr3,3,128 Gn32 Cr3,3,256 Gn32 Cr3,3,256 Gn32 Lbx32 Lby32 Cr1,1,32 Gn32 Lby32 Lbx32]' # NOQA

# For first, non-VGSL params, look at lib/train.py
# 1: batch
# 120: height
# 0: width
# 1: channel
# Cr3,13,32: 3x13 conv., 32 outputs                      |
# Do0.1,2: Dropout layer with p=0.1 in 2 dimensions      | x 2
# Mp2,2: Maxpool 2x2 rectangle                           |
# Cr3,9,64: 3x9 conv., 64 outputs
# Do0.1,2: Dropout layer with p=0.1 in 2 dimensions
# Mp2,2: Maxpool 2x2 rectangle
# Cr3,9,64: 9x3 conv., 64 outputs
# Do0.1,2: Dropout layer with p=0.1 in 2 dimensions
# S1(1x0)1,3: Split dimension 1, move one part to another (???)
# Lbx200: Bidirectional LSTM on the x-dimension with 200 outputs |
# Do0.1,2: Dropout layer with p=0.1 in 2 dimensions              | x 2
# Lbx200: Bidirectional LSTM on the x-dimension with 200 outputs
# Do: Dropout laye with p=.5 in 1 dimension
RECOGNITION_SPEC = '[1,120,0,1 Cr3,13,32 Do0.1,2 Mp2,2 Cr3,13,32 Do0.1,2 Mp2,2 Cr3,9,64 Do0.1,2 Mp2,2 Cr3,9,64 Do0.1,2 S1(1x0)1,3 Lbx200 Do0.1,2 Lbx200 Do0.1,2 Lbx200 Do]' # NOQA

RECOGNITION_PRETRAIN_HYPER_PARAMS = {'pad': 16,
                                     'freq': 1.0,
                                     'batch_size': 64,
                                     'quit': 'early',
                                     'epochs': -1,
                                     'min_epochs': 100,
                                     'lag': 5,
                                     'min_delta': None,
                                     'optimizer': 'Adam',
                                     'lrate': 1e-6,
                                     'momentum': 0.9,
                                     'weight_decay': 0.01,
                                     'schedule': 'cosine',
                                     'completed_epochs': 0,
                                     'augment': False,
                                     # lr scheduler params
                                     # step/exp decay
                                     'step_size': 10,
                                     'gamma': 0.1,
                                     # reduce on plateau
                                     'rop_factor': 0.1,
                                     'rop_patience': 5,
                                     # cosine
                                     'cos_t_max': 100,
                                     # masking parameters
                                     'mask_width': 4,
                                     'mask_prob': 0.5,
                                     'num_negatives': 100,
                                     'logit_temp': 0.1,
                                     'warmup': 32000,
                                     }

RECOGNITION_HYPER_PARAMS = {'pad': 16,
                            'freq': 1.0,
                            'batch_size': 16,
                            'quit': 'early',
                            'epochs': -1,
                            'min_epochs': 5500,
                            'lag': 10,
                            'min_delta': None,
                            'optimizer': 'Adam',
                            'lrate': 1e-3,
                            'momentum': 0.9,
                            'weight_decay': 0.0,
                            'schedule': 'constant',
                            'normalization': None,
                            'normalize_whitespace': False,
                            'completed_epochs': 0,
                            'augment': False,
                            # lr scheduler params
                            # step/exp decay
                            'step_size': 10,
                            'gamma': 0.1,
                            # reduce on plateau
                            'rop_factor': 0.1,
                            'rop_patience': 5,
                            # cosine
                            'cos_t_max': 50,
                            'warmup': 0,
                            'freeze_backbone': 0,
                            }

SEGMENTATION_HYPER_PARAMS = {'line_width': 8,
                             'padding': (0, 0),
                             'freq': 1.0,
                             'quit': 'dumb',
                             'epochs': 50,
                             'min_epochs': 0,
                             'lag': 10,
                             'min_delta': None,
                             'optimizer': 'Adam',
                             'lrate': 2e-4,
                             'momentum': 0.9,
                             'weight_decay': 1e-5,
                             'schedule': 'constant',
                             'completed_epochs': 0,
                             'augment': False,
                             # lr scheduler params
                             # step/exp decay
                             'step_size': 10,
                             'gamma': 0.1,
                             # reduce on plateau
                             'rop_factor': 0.1,
                             'rop_patience': 5,
                             # cosine
                             'cos_t_max': 50,
                             'warmup': 0,
                             }
