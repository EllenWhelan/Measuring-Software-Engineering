import github3
#globals
myRepos= []

# login stuff
username = "username"
password = "password"
userAccount = github3.login(username=username, password=password)


def listingRepos (username):
    # listing users repos
    i = 1
    for repo in userAccount.repositories_by(username):
        x = repo.git_url
        myRepos.append(repo)
        print(str(i) + '.' + x[18 + len(username):-4])
        i = i + 1
    print('Please enter the number of the repo you would like to view.')
    repoNum = input()
    detailingRepo(repoNum)

def detailingRepo (repoNum):
    # displaying repo details
    print(myRepos[repoNum - 1].git_url)
    print(myRepos[repoNum-1].)
    print ('Enter 1 to exit')
    if input() == 1 :listingRepos(username)


#running functions
listingRepos(username)
