import re
import json
import subprocess
from github import Github
from gitlab import Gitlab

# load credentials from json file
with open("config.json") as f:
    data = f.read()
    GHAccessToken = json.loads(data)["GitHubAccessToken"]
    GLAccessToken = json.loads(data)["GitLabAccessToken"]

# authorise to github and gitlab
gh = Github(GHAccessToken)
gl = Gitlab(
    url="https://gitlab.com",
    private_token=GLAccessToken,
)
gl.auth()

# convert to appropriate git url
def convert_url(api_url):
    match = re.match(
        pattern="(https?:\/\/)api\.(github.com)\/repos(\/.*)", string=api_url
    )
    git_url = match[1] + match[2] + match[3] + ".git"
    return git_url


# get some information from accounts
me = gl.users.list(username=gl.user.username)[0]  # type: 'gitlab.v4.objects.User'
gh_user = gh.get_user()  # type: 'github.v3.objects.User'
gl_projects = gl.projects.list(visibility="public", owned=True)  # type: list
gh_projects = [
    (i.name, convert_url(i.url)) for i in gh.get_user(login=gh_user.name).get_repos()
]  # type: list


# check if gitlab project exists or not
def check_gitlab_project(folderName):
    project_name = folderName.replace(".git", "")
    lowerGlProjects_tmp = [i.name for i in gl_projects]
    if not project_name in lowerGlProjects_tmp:
        gl.projects.create({"name": project_name, "visibility": "public"})
    return


# clone repo with --mirror option
def clone_repo(repo):
    subprocess.call(["bash", "./scripts/clone.sh", repo[0], repo[1]])


# push repo to remote
def push_repo(repo):
    gitlab_url = f"https://oauth2:{GLAccessToken}@gitlab.com/{me.name}/" + repo[0]
    check_gitlab_project(repo[0])
    subprocess.call(["bash", "./scripts/push.sh", repo[0], gitlab_url])
    subprocess.call(["rm", "-rf", repo[0]])  # remove local folder


# main function
def main():
    for repo in gh_projects:
        clone_repo(repo)
        push_repo(repo)


if __name__ == "__main__":
    """ Run main function """
    main()
