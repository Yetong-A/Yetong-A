from os import write
import pandas as pd
import numpy as np
import csv
import numpy as np
import numba
import nltk

person = pd.read_csv('person.csv')
preson_cv = pd.read_csv('person_cv.csv')
person_jobhist = pd.read_csv('person_job_hist.csv')
preson_project = pd.read_csv('person_project.csv')
person_procert = pd.read_csv('person_pro_cert.csv')
recruit = pd.read_csv('recruit.csv')
recruit_folder = pd.read_csv('submission.csv')
def judge(jobneed,persongender,jobxueli,personxueli):
    if judgexueli(jobxueli,personxueli):
        return genderjudge(jobneed,persongender)
    else:
        return 0    

def genderjudge(jobneed,persongender): #判断性别
    if '男' or '女' not in jobneed or '男女不限' or '男/女' or '女/男' or '男、女不限' or '性别不限' in jobneed:
        return 1
    if '，女' or '女,' or'女性' or '性别女' or '性别：女' or '性别:女' or '只招女生' or '女性优先' in jobneed:
        if persongender == '男':
            return 0
        else:
            return 1
    elif '男，' or '男性' or '性别：男' or '男,' or '男性优先' in jobneed:
        if persongender == '女':
            return 0
        else:
            return 1
    else:
        return 1
        
def judgexueli(jobxueli,personxueli):#判断学历
    if  jobxueli == '其他':
        jobn = 0
    elif jobxueli == '中专':
        jobn = 1
    elif jobxueli == '高中（职高、技校）':
        jobn = 2
    elif jobxueli == '大专':
        jobn = 3
    elif jobxueli == '大学本科':
        jobn = 4
    elif jobxueli == '硕士研究生':
        jobn = 5
    elif jobxueli == '博士后':
        jobn = 7
    else:
        jobn = 0

    if personxueli == '其他':
        pern = 0
    elif personxueli == '中专':
        pern = 1
    elif personxueli == '高中（职高、技校）':
        pern = 2
    elif personxueli == '大专':
        pern = 3
    elif personxueli == '大学本科':
        pern = 4
    elif personxueli == '硕士研究生':
        pern = 5
    elif personxueli == '博士研究生':
        pern = 6
    elif personxueli == '博士后':
        pern = 7
    else:
        pern = 0


    if pern >= jobn:
        return 1
    else:
        return 0

list = [] #after judge
jobnumblist = []   #result_folder中jobnumber
personnumblist = []#result_folder中personnumber

for res in recruit_folder.index:
    result_jobnumb = recruit_folder.loc[res][0]
    result_personnumb = recruit_folder.loc[res][1]
    jobnumblist.append(result_jobnumb)
    personnumblist.append(result_personnumb)

personidlist = [] #person表中id
personidxuelilist = []#person表中学历
personidgenderlist = []#person表中性别
for per in person.index:
    person_numb = person.loc[per][0]
    person_xueli = person.loc[per][3]
    person_gender = person.loc[per][1]
    personidlist.append(person_numb)
    personidxuelilist.append(person_xueli)
    personidgenderlist.append(person_gender)
jobidlist = []  #recruit表中jobid
jobidxuelilist = []   #recruit表中job要求学历
jobneedlist = []
for job in recruit.index:
    job_numb = recruit.loc[job][0]
    job_xueli = recruit.loc[job][5]
    job_need = recruit.loc[job][8]
    jobidlist.append(job_numb)
    jobidxuelilist.append(job_xueli)
    jobneedlist.append(job_need)

for i in range(len(jobnumblist)):
    for j in jobidlist:
        if j == jobnumblist[i]:
            jobxuexue = jobidxuelilist[jobidlist.index(j)]
            jobgengen = jobneedlist[jobidlist.index(j)] #jobneed用作判断gender
            print(i)
            #print(jobxuexue)
            for k in personidlist:
                if k == personnumblist[i]:
                    personxuexue = personidxuelilist[personidlist.index(k)]
                    persongengen = personidgenderlist[personidlist.index(k)]
                    #print(personxuexue)
                    list.append(judge(jobgengen,persongengen,jobxuexue,personxuexue)) #判断成功存入list
                    print(judge(jobgengen,persongengen,jobxuexue,personxuexue))
                    print('inlist is ok')
                    break
            break

    
with open('test2.csv','a',newline='')as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(list)                    
print("save in test!")           
