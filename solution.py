import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

chat_id = 192196854

def solution(x: np.array, y: np.array) -> bool:    
    return stats.anderson_ksamp([x, y]).pvalue < 0.04 
