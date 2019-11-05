import github3


username = "username"
password = "password"

userAccount = github3.login(username=username, password=password)

for repo in userAccount.repositories_by(username):
    x=repo.git_url
    print(x[18+len(username):-4])

