import praw
import random
import time

# static variables
REDDIT_USERNAME = 'BuggyMemeBot'

# login data
reddit = praw.Reddit(client_id='4aK_5w6Jenjlpw',
                     client_secret='n-HoTqZdcNMwdmBuD8bWCwT0dWc',
                     username=REDDIT_USERNAME,
                     password='bugbot2018',
                     user_agent='a cool bot by /u/kleecarim')

# subreddit where to bot is active
subreddit = reddit.subreddit('khazixmainstest')

#list of keywords


# reply class, it does NOT decide what to reply, but only generate the message to reply!


class Reply:

    # TODO: how do i make a class static in python?

    @staticmethod
    def TinjusFacts():  # keyword: !tinjusfacts
        tinjusFactsList = ["Tinjus says a", "Tinjus says b", "Tinjus says c"]
        return random.choice(tinjusFactsList)

    @staticmethod
    def BugFacts():
        return 0

    @staticmethod
    def KhazixQuotes():  # !KhaZixQuotes
        quoteList = ["Change... is good.", "They fear me.", "Isolate and devour.", "One by one.", "Ah... delicious.",
                     "Blood in the air.", "Clever creatures.", "They fear me.", "Devour their bones.",
                     "Consume and adapt.", "Position for ambush.", "A different view.", "I sense worthy prey.",
                     "Endless hunger.", "This world is delicious!", "Sharpening my claws.", "Fear the Void.",
                     "No escape.", "They'll never see me."]
        return random.choice(quoteList)

    # annoying stuff and "easter eggs"
    @staticmethod
    def BotAnswer():
        return 'I have evolved beyond jokes. I am now a robot. Beep. Boop.'

#select the right reply method


print("Starting bot...")

#main loop
while True:
    for submission in subreddit.new(limit=3):
        print("Post Title: " + str(submission.title))
    time.sleep(10)






