from github import Github
import argparse, json, requests


class GithubApi:
    def __init__(self):
        self.github = Github(
            "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"
        )

    def get_repo(self, owner_name, repo_name):
        repo = self.github.get_repo(f"{owner_name}/{repo_name}")
        return repo

    def get_commit(self, repo, commit_id):
        commit = repo.get_commit(f"{commit_id[:6]}")
        return commit

    def get_file_contents(self, repo, file_name, parent_commit_sha):
        contents = repo.get_contents(file_name, ref=parent_commit_sha)
        return contents

    def get_commit_info(self, commit_url):
        commit_url_list = commit_url.split("/")

        owner_name = commit_url_list[3]
        repo_name = commit_url_list[4]
        commit_id = commit_url_list[6]

        commit_info = requests.get(
            f"https://api.github.com/repos/{owner_name}/{repo_name}/commits/{commit_id}"
        ).text

        commit_info_dict = json.loads(commit_info)
        return commit_info_dict

    def get_owner_and_repo_name(self, url):
        commit_url_list = url.split("/")

        owner_name = commit_url_list[3]
        repo_name = commit_url_list[4]

        return owner_name, repo_name
