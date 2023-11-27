class User():
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

#  User Data
userWithValidData = User("huy.ev.apaga.hk@gmail.com", "Amazon@Selenium@2023")
userWithInvalidPassword = User("huy.ev.apaga.hk@gmail.com", "wrongPassword")
userWithInvalidUsername = User("aaaaa", "Amazon@Selenium@2023")

# URLs
urlSignInPage = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
urlMainPage = "https://www.amazon.com/"

