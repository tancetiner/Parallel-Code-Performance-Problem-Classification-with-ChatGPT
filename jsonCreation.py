import pandas as pd
import json

df = pd.read_excel("./RQ1.xlsx")
commit_dict = {"commits": []}

column_list = ["Sub-Category", "Solution Main Category", "Link to commit"]


df.dropna(subset=column_list, how="any", inplace=True)
count = 0
for label, series in df.iterrows():
    new_commit = {key: series[key] for key in column_list}
    new_commit["Code Folder Index"] = count
    commit_dict["commits"].append(new_commit)
    count += 1

commit_json = json.dumps(commit_dict)
with open("./commits.json", "w") as f:
    f.write(commit_json)
print(count)
