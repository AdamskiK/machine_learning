import pandas as pd
pd.set_option('max_rows', 50000)
xtrain_1 = pd.read_csv('xtrain_1.csv',low_memory=False)
y_train = pd.read_csv('y_train.csv')

%matplotlib inline
xtrain_1[['x48420','x97674']].boxplot(return_type='axes')

#1.2

def transform_binary(col):
    arr = pd.DataFrame(np.zeros((len(xtrain_1.loc[:,col]),len(xtrain_1.loc[:,col].value_counts()))))
    uniq = xtrain_1.loc[:,col].unique()
    arr.columns = np.delete(uniq,-1)
    for i in range(len(xtrain_1[col])):
        for j in range(len(uniq)-1):
            if xtrain_1[col][i] == uniq[j]:
                arr.iloc[i,j] = 1
    return arr
    
#1.3

from time import time
import datetime
def transform_date(col):
    time_col = xtrain_1[col]
    time_col = pd.to_datetime(time_col, format='%Y-%m-%d %H:%M:%S.%f')
    time_arr = []
    for i in range(len(time_col)):
        res = (time_col.iloc[i]-datetime.datetime(1970,1,1)).total_seconds()
        time_arr.append(res)
    time_arr = pd.DataFrame(time_arr)
    time_arr.columns = np.array([col])
    return time_arr
    
#1.4

def transform_lang(arg='lang'):
    lang_arr = []
    for i in range(len(xtrain_1.columns.str.contains(arg))):
        if pd.DataFrame(xtrain_1.columns.str.contains(arg)).iloc[i,0] == True:
            lang_arr.append(i)
    return xtrain_1.iloc[:,lang_arr]
    
#1.5A

def transform_country(arg='country'):
    lang_arr = []
    for i in range(len(xtrain_1.columns.str.contains(arg))):
        if pd.DataFrame(xtrain_1.columns.str.contains(arg)).iloc[i,0] == True:
            lang_arr.append(i)
    return xtrain_1.iloc[:,lang_arr]
    
#1.5B

country_df = transform_country()
def valid_country(arg=0):
    country_df['valid'] = (country_df.loc[:,'user_ip_country'] == country_df.loc[:,'country_code'])
    return country_df
    
#1.6

def transform_osver(arg='browser_string'):
    lang_arr = []
    for i in range(len(xtrain_1.columns.str.contains(arg))):
        if pd.DataFrame(xtrain_1.columns.str.contains(arg)).iloc[i,0] == True:
            lang_arr.append(i)
    return xtrain_1.iloc[:,lang_arr[0]]