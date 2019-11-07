import github3
#globals
myRepos= []

# login stuff
username = "username"
password = "password"
userAccount = github3.login(username=username, password=password)

def detailinguserprofile (username):
    #print(user.bio)
    print('hello')
    user =userAccount.me()
    print("My User Profile")
    print("Name: " +str(user.name))
    print("Bio: " +str(user.bio))
    print("Company: " +str(user.company))
    print("Email" + str(user.email))
    print("Followers: " +str(user.followers_count))
    print("Following: " +str(user.following_count))
    print("Location: " +str(user.location))
    print("Press 1 to exit")
    if(input()==1) :homePage(username)


def homePage(username):
    print ('1. User profile')
    print ('2. Users Repositories')
    print("Press number of feature you would like to view: ")
    i=input()
    if(i==1):detailinguserprofile(username)
    if(i==2):listingRepos(username)
    else: print("Error: invalid input")
    homePage(username)


def listingRepos (username):
    # listing users repos
    i = 1
    for repo in userAccount.repositories_by(username):
        x = repo.git_url
        myRepos.append(repo)
        print(str(i) + '.' + x[18 + len(username):-4])
        i = i + 1
    print('Please enter the number of the repo you would like to view or -1 to exit.')
    i =input()
    if(i!=-1): detailingRepo(i)
    if(i==-1): homePage(username)

def detailingRepo (repoNum):
    # displaying repo details
    print(myRepos[repoNum - 1].git_url)
    #print contributors
    print("Contributors:")
    for contributor in myRepos[repoNum-1].contributors() :
        print(contributor.login + '\n')

    print("Last updated: " + str(myRepos[repoNum-1].pushed_at))
    print('Enter 1 to exit')
    if input() == 1 :listingRepos(username)


#running functions
homePage(username)
