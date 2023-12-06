import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MaxAbsScaler, MinMaxScaler, RobustScaler
from .imbalance import Imbalance_Module
from .preprocess import preprosess_Module
from .encoder import Encoder_Module
from copy import deepcopy

def get_X(df_:pd.DataFrame, df_tst:pd.DataFrame, features:iter=None):
    '''Make feature vectors from a DataFrame.

    Args:
        df: DataFrame
        features: selected columns
    '''
    df_ = deepcopy(df_)
    df_tst = deepcopy(df_tst)
    """df.drop(df[(df['ECLO']==2)].index, inplace=True)
    df.drop(df[(df['ECLO']==3)].index, inplace=True)
    df.drop(df[(df['ECLO']==4)].index, inplace=True)
    df.drop(df[(df['ECLO']==5)].index, inplace=True)"""
    preprosess =preprosess_Module(df_)
    df, df_tst = preprosess.preprocess(df_, df_tst)
    
    #resample = Imbalance_Module()
    #df = resample.resample(df)
    print('resampling complete!\nshape:{} -> {}'.format(df_.shape, df.shape))
    df_tst.drop(['ID'], axis=1, inplace=True)
    df = df[df_tst.columns]
    print('shape of data:',df_.shape)
    return df.to_numpy(dtype=np.float32), df_tst.to_numpy(dtype=np.float32)

def get_y(df:pd.DataFrame, df_tst:pd.DataFrame):
    '''Make the target from a DataFrame.

    Args:
        df: DataFrame
    '''
    df = deepcopy(df)
    """df.drop(df[(df['ECLO']==2)].index, inplace=True)
    df.drop(df[(df['ECLO']==3)].index, inplace=True)
    df.drop(df[(df['ECLO']==4)].index, inplace=True)
    df.drop(df[(df['ECLO']==5)].index, inplace=True)"""
    preprosess =preprosess_Module(df)
    df, df_tst = preprosess.preprocess(df, df_tst)
    #resample = Imbalance_Module()
    #df = resample.resample(df)
    print('shape of data:',df.shape)
    df = df[['사망자수', '중상자수', '경상자수', '부상자수']]
    return df.to_numpy(dtype=np.float32)