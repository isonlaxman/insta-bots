from InstagramAPI import InstagramAPI

api = InstagramAPI("inoslaxman", "Nois1199@Instagram")

api.login()

print(api.getProfileData()) 