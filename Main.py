import praw
import random
import time
import Reply
import HandleComment

# static variables
REDDIT_USERNAME = 'BuggyMemeBot'

# login data
reddit = praw.Reddit(client_id='4aK_5w6Jenjlpw',
                     client_secret='n-HoTqZdcNMwdmBuD8bWCwT0dWc',
                     username=REDDIT_USERNAME,
                     password='bugbot2018',
                     user_agent='a cool bot by /u/kleecarim')

subreddit = reddit.subreddit('khazixmainstest')

print("Starting bot...")

#main loop
while True:
    try:
        for submission in subreddit.new(limit=3):
            for comment in submission.comments.list():
                HandleComment.SelectReplyMsg(comment)
    except Exception as e:
        print(e)
    time.sleep(10)

