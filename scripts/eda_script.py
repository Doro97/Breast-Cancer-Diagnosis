import pandas as pd
import numpy as np

#number of unique values per column
def unique_values(df):
    unique_values=pd.DataFrame(df.apply(lambda x: len(x.value_counts(dropna=False)), axis=0), 
                           columns=['Unique Value Count']).sort_values(by='Unique Value Count', ascending=True)
    return unique_values


def missing_values(x):
    # Total number of elements in the dataset
    totalCells = x.size
    #Number of missing values per column
    missingCount = x.isnull().sum()
    #Total number of missing values
    totalMissing = missingCount.sum()
    # Calculate percentage of missing values
    print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

def column_missingdata(df):
    #check for missing values per column
    values=df.isnull().sum().sort_values(ascending=False)
    #percentage of missing values per column
    percentage=df.isnull().mean()*100
    return values,percentage

#replace missing values with mean 
def fill_mean(dataframe,column):
    dataframe[column].fillna(dataframe[column].mean(), inplace = True)
    return dataframe

# replacing with the median
def fill_median(dataframe,column):
    dataframe[column].fillna(dataframe[column].median(), inplace = True)
    return dataframe

#fill with mode
def fill_mode(dataframe,column):
    dataframe[column].fillna(dataframe[column].mode(), inplace = True)
    return dataframe

#replaces all missing values with 0
def fill_with_0(dataframe):
    dataframe.fillna(0, inplace=True)
    return dataframe# fill missing with ffill method for columns (diag_1, diag_2, diag_3)

def fix_missing_ffill(df, col):
    df[col] = df[col].fillna(method='ffill')
    return df[col]


def fix_missing_bfill(df, col):
    df[col] = df[col].fillna(method='bfill')
    return df[col]

## OUTLIERS ##

 # Identifying outliers using IQR score
def IQR_Score(df:pd.DataFrame):
    """This function prints out the IQR Score of each of 
    the columns/ features"""
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    print(IQR)

#Identify outliers using the Z score
from scipy import stats
def Z_Score(df:pd.DataFrame):
    z = np.abs(stats.zscore(df))
    print(z)   