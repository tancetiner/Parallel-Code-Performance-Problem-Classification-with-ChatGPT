import json

categories = []

commits_json = open("./commits.json", "r")
commits_dict = json.load(commits_json)

for commit in commits_dict["commits"]:
    if commit["Sub-Category"] not in categories:
        categories.append(commit["Sub-Category"])

categories_json = json.dumps({"categories": categories})
with open("./problemCategories.json", "w") as f:
    f.write(categories_json)
