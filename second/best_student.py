import pandas as pd

def getBestStudent():
    studlList = pd.read_csv("./second/group_list.csv")
    gradeList = pd.read_csv("./second/group_grades.csv")

    groupedTable = pd.merge(studlList, gradeList, how="inner", on=["student_id"])
    avgTable = groupedTable.groupby(['first_name', 'middle_name', 'last_name', 'student_id'], as_index=False)['grade'].mean().sort_values(by="grade", ascending=False)

    return groupedTable.loc[groupedTable['student_id'] == avgTable['student_id'].iloc[0]]



print(getBestStudent())