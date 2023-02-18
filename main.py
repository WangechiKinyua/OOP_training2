#lass User:
#   pass


#user_1 = User()
#user_1.id = "001"
#user_1.username = "Caroline"
#
#print(user_1.username)
#
#user_2 = User()
#user_2.id = "002"
#user_2.username = "Wangechi"


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # is a constant value, no need to include it when the class User is initialised
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Caroline")   # when creating the object you must include the values added in the init function
# print(user_1.id)
user_2 = User("002", "Wangechi")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)



