import pandas as pd
screen_time=[2,3,4,5,7,9]
sleep_hours=[4,5,6,7,8,3]
student_name=["Saketh","Balaya!","JaiBabu!","katterMummy","Bhahubali","kattapa"]
study_hours=[3,4,5,7,2,5]
dict1={
    "screen_time":screen_time,
    "sleep_hours":sleep_hours,
    "student_name":student_name,
    "study_hours":study_hours,
}
print(dict1)
df=pd.DataFrame(dict1)
print(df)
