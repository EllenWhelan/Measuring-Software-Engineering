import github3

username = "EllenWhelan"
password = "lamagh+mal_1998"

userAccount = github3.login(username=username, password=password)
if(userAccount.followers >1): print ('Hello world' )
