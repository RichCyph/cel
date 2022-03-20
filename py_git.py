

from github import Github
import os
OAuth_token = "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"
g = Github(OAuth_token)
repo = g.get_repo("RichCyph/cel")




all_files = []

def commit_file(file_name):
    with open(file_name, 'rb') as file:
        content = file.read()

        if(file_name in all_files):
            contents = repo.get_contents(file_name)
            repo.update_file(contents.path, "commiting update", content, contents.sha, branch="main")
            print(file_name + ' UPDATED')
        else:
            repo.create_file(file_name, 'committing new', content)
            print(file_name + ' CREATED')

contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
    else:
        #print(file_content)
        all_files.append(str(file_content).replace('ContentFile(path="','').replace('")',''))
#print(all_files)

#os.rmdir(".git")
for root, dirs, files in os.walk(".", topdown=False):

    for name in files:
        if "./.git" == os.path.join(root, name)[0:6] \
        or "./__py" == os.path.join(root, name)[0:6] \
        or ".png" == os.path.join(root, name)[-4:] \
        or ".jpg" == os.path.join(root, name)[-4:]:
            continue
        file_to_add = os.path.join(root, name)[2:]
        commit_file(file_to_add)
#s = "asdf.png"
#print(s.)
#print(repo)
#print(all_files)
    #for name in dirs:
    #    if "./.git" == os.path.join(root, name)[0:6]:
    #        continue
        #print(os.path.join(root, name)[0:3])
            #continue
    #    print(os.path.join(root, name))
# for creating a new repo
'''
user = g.get_user()
repo_name = 'test'
if repo_name not in [r.name for r in user.get_repos()]:
    user.create_repo(repo_name)
repo = user.get_repo(repo_name)
'''

#example adding a png
'''
with open('static/images/001.png', 'rb') as file:
    content = file.read()
    # File details
    #content = base64.b64encode(content)
    file_name       = 'py001.png'
    # Create file
    repo.create_file(file_name, 'commit', content)
'''

#issues = repo.get_issues(state="open")
#print(issues.get_page(0))
'''
for repo in g.get_user().get_repos():
      print(repo.name)
      repo.edit(has_wiki=False)
      # to see all the available attributes and methods
      print(dir(repo))
'''

#repo.create_file("test.txt", "test", "test", branch="test")
