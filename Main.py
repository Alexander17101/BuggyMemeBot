import praw
import random
import time
import Reply
import HandleComment

# static variables
REDDIT_USERNAME = 'BuggyMemeBot'

# login data
reddit = praw.Reddit(censured)

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

