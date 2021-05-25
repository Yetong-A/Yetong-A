import pandas as pd
import gc
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, roc_auc_score, classification_report
from tqdm import tqdm
import lightgbm as lgb
import os
import numpy as np

warnings.simplefilter('ignore')
pd.set_option('max_columns', None)
pd.set_option('max_rows', 500)
pd.options.display.max_colwidth = 10000

seed = 2021

df_train = pd.read_csv('recruit_folder.csv')
df_test = pd.read_csv('recruit_folder.csv')
df_test['LABEL'] = np.nan
df_feature = df_train.append(df_test, sort=False)
df_feature['LABEL'].mean()
print(df_feature['LABEL'].mean())


df_person = pd.read_csv('person.csv')
df_person = df_person.drop(columns=['LANGUAGE_REMARK', 'SPECILTY'], axis=1)
df_person.rename(columns={'MAJOR': 'PERSON_MAJOR'}, inplace=True)
df_person.head()
print(df_person.head())
#求职者信息打印
edu_map = {
    '其它': 0,
    '中专': 1,
    '高中（职高、技校）': 2,
    '大专': 3,
    '大学本科': 4,
    '硕士研究生': 5,
    '博士后': 6
}

df_person['HIGHEST_EDU'] = df_person['HIGHEST_EDU'].map(edu_map)

def major_clean(x):      #去掉所有的【】；
    if type(x) == float:
        return x

    x = x.replace('【', '').replace('】', '')
    return x
df_person['PERSON_MAJOR'] = df_person['PERSON_MAJOR'].apply(major_clean)
df_feature = df_feature.merge(df_person, how='left', on='PERSON_ID')
df_person_cv = pd.read_csv('person_cv.csv')
df_person_cv = df_person_cv.drop(columns=['REMARK', 'SELF_COMMENT'], axis=1)
df_person_cv.rename(columns={'LOCATION': 'CV_LOCATION'}, inplace=True)
df_person_cv.head()
#求职意向
df_feature = df_feature.merge(df_person_cv, how='left', on='PERSON_ID')
df_person_job_hist = pd.read_csv('person_job_hist.csv')
df_person_job_hist.head()
#工作经历
df_tmp = df_person_job_hist.groupby(['PERSON_ID']).size().reset_index()
df_tmp.columns = ['PERSON_ID', 'job_hist_cnt']
df_feature = df_feature.merge(df_tmp, how='left', on='PERSON_ID')
df_recruit = pd.read_csv('recruit.csv')
df_recruit = df_recruit.drop(columns=['DETAIL'], axis=1)
df_recruit.rename(columns={
    'LOCATION': 'RECRUIT_LOCATION',
    'MAJOR': 'RECRUIT_MAJOR'
},
                  inplace=True)
df_recruit.head()
#岗位信息
def major_clean(x):    #去掉【】；
    if type(x) == float:
        return x

    x = x.replace('【', '').replace('】', '')
    return x


df_recruit['RECRUIT_MAJOR'] = df_recruit['RECRUIT_MAJOR'].apply(major_clean)
df_recruit['LOWER_EDU'] = df_recruit['LOWER_EDU'].map(edu_map)
work_year_range_map = {
    '应届毕业生': 0,
    '0至1年': 1,
    '1至2年': 2,
    '3至5年': 3,
    '5年以上': 4,
    '不限': 5
}
df_recruit['WORK_YEARS_RANGE'] = df_recruit['WORK_YEARS_RANGE'].map(
    work_year_range_map)
df_feature = df_feature.merge(df_recruit, how='left', on='RECRUIT_ID')
print(df_feature)