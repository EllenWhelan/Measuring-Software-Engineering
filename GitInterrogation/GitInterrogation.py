import github3

username = "username"
password = "password"

userAccount = github3.login(username=username, password=password)
if(userAccount.followers >1): print ('Hello world' )
