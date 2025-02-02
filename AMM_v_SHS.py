# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:18:38 2022

@author: lawashburn
"""


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import csv
import matplotlib
import re
from datetime import datetime
now = datetime.now()
from user_input import prelim_AMM_out_file_name_path
from user_input import SHS_results_path_for_AMM
from user_input import AMM_v_SHS_out_path
from user_input import sample_name
print('start time:', datetime.now())

amm_results = prelim_AMM_out_file_name_path #Module 1 results
SHS_results = SHS_results_path_for_AMM #sequence homology search results
working_directory = AMM_v_SHS_out_path #output directory


SHS_results = pd.read_csv(SHS_results)
shs_seq = SHS_results['Sequence'].values.tolist() #list of SHS sequences

amm_results = pd.read_csv(amm_results)
#amm_seq = amm_results['Sequence'].values.tolist() #list of AMM sequences
seq_overview = pd.DataFrame()
seq_overview['PTM'] = amm_results['Sequence']
#removes ptms from AMM sequences to compare with SHS
#amm_seq_noptm = []
#for a in amm_seq:
#    remove_lower = lambda text: re.sub('[a-z]', '', text)
#    a = remove_lower(a)
#    a = ''.join(item for item in a if item.isalpha())
#    amm_seq_noptm.append(a)
#print(len(amm_seq_noptm))
#seq_overview = pd.DataFrame()
#seq_overview['PTM'] = amm_seq
#seq_overview['no PTM'] = amm_seq_noptm
    
#amm_unique = [] #list of unique amm, not in shs
#for b in amm_seq_noptm:
#    if b not in shs_seq:
#        amm_unique.append(b)

#amm_unique_nodups = []
#for c in amm_unique:
#    if c not in amm_unique_nodups:
#        amm_unique_nodups.append(c)

#shs_list_nodups = []
#for d in shs_seq:
#    if d not in shs_list_nodups:
#        shs_list_nodups.append(d)

#seq_overview['present'] = seq_overview['no PTM'].isin(amm_unique)
#seq_overview = seq_overview[seq_overview['present'] == True]

#match_w_ptm = seq_overview['PTM'].values.tolist()

from user_input import AMM_v_SHS_out_results
result_name = AMM_v_SHS_out_results

with open(result_name,'w',newline='') as file:
    writer = csv.writer(file)
    seq_overview.to_csv(file,index=False)
