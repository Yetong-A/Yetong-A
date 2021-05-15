from os import write
import pandas as pd
import numpy as np
import csv


person = pd.read_csv('person.csv')
preson_cv = pd.read_csv('person_cv.csv')
person_jobhist = pd.read_csv('person_job_hist.csv')
preson_project = pd.read_csv('person_project.csv')
person_procert = pd.read_csv('person_pro_cert.csv')
recruit = pd.read_csv('recruit.csv')
recruit_folder = pd.read_csv('recruit_folder.csv')

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
for per in person.index:
    person_numb = person.loc[per][0]
    person_xueli = person.loc[per][3]
    personidlist.append(person_numb)
    personidxuelilist.append(person_xueli)

jobidlist = []  #recruit表中jobid
jobidxuelilist = []   #recruit表中job要求学历
  
for job in recruit.index:
    job_numb = recruit.loc[job][0]
    job_xueli = recruit.loc[job][5]
    jobidlist.append(job_numb)
    jobidxuelilist.append(job_xueli)

for i in range(len(jobnumblist)):
    for j in jobidlist:
        if j == jobnumblist[i]:
            jobxuexue = jobidxuelilist[jobidlist.index(j)]
            print(i)
            print(jobxuexue)
            for k in personidlist:
                if k == personnumblist[i]:
                    personxuexue = personidxuelilist[personidlist.index(k)]
                    
                    print(personxuexue)
                    list.append(judgexueli(jobxuexue,personxuexue))
                    # print(judgexueli(jobxuexue,personxuexue))
                    break
            break

print("save in test!")               
with open('test.csv','a',newline='')as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(list)                    


            









# for i in range(len(jobnumblist)):
#     print(i)
#     for j in recruit.index:
#         jobnumb = recruit.loc[j][0]
#         if jobnumb ==jobnumblist[i]:
#             job_xueli = recruit.loc[j][5]
#             print(job_xueli)
# break








# for i in recruit_folder.index:
#     result_jobnumb = recruit_folder.loc[i][0]
#     result_personnumb = recruit_folder.loc[i][1]
#     jobxuexue = ''
#     personxuexue = ''
#     for j in recruit.index:
#         jobnumb = recruit.loc[j][0]
#         if jobnumb ==result_jobnumb:
#             job_xueli = recruit.loc[j][5]
#             jobxuexue = job_xueli
#             #jobxuelilist.append(job_xueli)
#             #print('工作要求学历: '+job_xueli)
#             break
#     for k in person.index:
#         personnumb = person.loc[k][0]
#         if personnumb == result_personnumb:
#             person_xueli = person.loc[k][3]
#             personxuexue = person_xueli
#             #personxuelilist.append(person_xueli)
#             #print('人的学历    ：'+person_xueli)
#             list.append(judgexueli(jobxuexue,personxuexue))
#             print('inlist is ok!')
#             #print(judgexueli(jobxuexue,personxuexue))
#             print(i)
#             break