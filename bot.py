import praw
import pdb
import re
import os
from config import *



if not  os.path.isfile("config.py"):
    print("You must create a config file with your username and password.")    
    exit(1)

myUserAgent= ("PyEng B0t 1.0")

r = praw.Reddit(user_agent = myUserAgent)
r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning=True)



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as file:
        posts_replied_to = f.read().split("\n")
        posts_replied_to = filter(None, posts_replied_to)
         
print(posts_replied_to)

subreddit = r.get_subreddit("learnpython")

for submission in subreddit.get_hot(limit = 5):
    if submission.id not in posts_replied_to:
        if re.search("EULER", submission.title, re.IGNORECASE):  
            #submission.add_comment("Botty bot says: Me too!!")                      
            print(submission.title)
            print(submission.selftext)
            print(submission.score)
            
            posts_replied_to.append(submission.id)



with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

