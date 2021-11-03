#As a backend angineer, you are tasked
#with developing a fast in-memory data
#structure to manage profile information (username,
#name and email) for 100 million users.
#It should allow the following operation to e performed
#efficiently:
#INSERT the profile info for a new user.
#FIND the profile info of a user, given username.
#UPDATE the profile info of a user, given username
#LIST all the users of the platfor, sorted by username.


# SOLUTION:
class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
       # print('User Created')
    #__repr__ function is used to show a string representation of the object.
    def __repr__(self):
        return "User(username={}, name={}, email={})".format(self.username,self.name,self.email)
    #__str__ functions show a string representatipn of your object.
    def __str__(self):
        return self.__repr__()


aakash=User('aakashsky','Aakash','aakash@redbug.com')
janet=User('gilljanet','Janet Gill','janet@redbug.com')
britto=User('britto','Britto Rodrigues','rodriguesbritto@redbug.com')
sam=User('samueljoe','Samuel Joe','joesam@redbug.com')
shriya=User('shepower','Shriya Sunil','shriyas@redbug.com')
karthik=User('melekarthik','Karthik Meledathu','karthim@redbug.com')
shuba=User('saishuba','Sai Shuba','saishuba@redbug.com')
sonia=User('augustinesonia','Sonia Augustine','soniaaugust@redbug.com')
chetan=User('sivachetan','Chetan Siva','sivachetan@redbug.com')
users=[aakash,janet,britto,sam,shriya,karthik,shuba,sonia,chetan]

'''
EDGE CASES
___________
INSERT:
-> inserting into an empty database
-> user already exists
FIND:
-> username not present in database
UPDATE:
-> username does not exist
LIST:
-> empty database
___________
IMPLEMENTATION
___________
INSERT: Loop through the list and add the new user at a position that keeps the list sorted.
FIND: Loop through the list and find the user object with the username matching the query.
UPDATE: Loop through the list and find the user object matching the username and update details.
LIST: Return the list of user objects.
___________
NOTE: Strings can be compared using comparison operators. 
'''


#Creating data structure using class:
class userDatabase:
    def __init__(self):
        self.users=[]
    def insert(self,new_user):
        i=0
        while(i<len(self.users)):
            #Finding the first username that is greater then new user's username:
            if(self.users[i].username > new_user.username):
                break
            i+=1
        self.users.insert(i,new_user)

#       pass
    def find(self,username):
        for user in self.users:
            if username == user.username:
                return user
#       pass
    def update(self,user):
        target = self.find(user.username)
        target.name=user.name
        target.email=user.email
#       pass
    def listAll(self):
        return self.users
#       pass

#Instantiating new userDatabase:
database= userDatabase()

#INSERTING SOME ENTRIES INTO DATABASE
database.insert(janet)
database.insert(sam)
database.insert(karthik)
database.insert(sonia)
database.insert(britto)

#FINDING A USER
user1 =database.find('melekarthik')
print("\n",user1,sep='')

#CHANGING INFO OF A USER
database.update(User(username='melekarthik',name='Karthik M',email='karthikmele@redbug.com'))

#RETRIEVE LIST OF ALL USERS IN ALPHABETICAL ORDER
print("\n\nList of all users in userDatabase:\n")
for each in database.listAll():
    print(each)



database.insert(shriya)
database.update(User(username='shepower',name='Shriya S',email='shriya@redbug.com'))
print("\nAFTER NEW INSERT AND UPDATE: \nList of all users in userDatabase:\n")
for each in database.listAll():
    print(each)



'''
COMPLEXITIES:
_____________
TIME COMPLEXITIES:
insert: runs throughout the length of users list in worst case scenario.
Hence, time complexity is O(N).
find: Like insert, runs throughout the length of users list to search for username in worst case scenario.
Hence, time complexity is O(N).
update: Like insert and find, runs throughout the length of users list to search for username and perform update operation in worst case scenario.
Hence, time complexity is O(N).
listAll: Simply returns all the users, without performing any functions(irrespective of the number of users in the list. 
Hence, it takes linear time, O(1).

SPACE COMPLEXITIES:
For all operations, it is O(1).
_____________
'''