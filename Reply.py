import praw
import random
import HandleComment
# reply class, it does NOT decide what to reply, but only generate the message to reply!


# keyword: !tinjusfacts
def BotHelp():
    return "Hey, seems like you need some help with me, Human! \n\n"\
           "I'm a nice bot created by u Kleecarim with the help of u VirtueBot! I'm here to help you.\n\n " \
           "Here's an overview of my basic commands:\n\n" \
           "!NoobHelp: links the most important guides for the people who are new to this sub.\n\n" \
           "!TinjusFacts will give you some Nice facts about our favorite KhaZix Player! Sounds nice, right?\n\n" \
           "!khazixquote replys with a random quote to your comment\n\n" \
           "!bugfact will give you some interesting facts about the bot!\n\n" \
           "Have a nice day!"


def NoobHelp():
    return "Welcome to this sub!\n\n A bird told me that you are new here, so check out these guides, They might help you! " \
                                         "\n\n Tinjus' guide: https://www.mobafire.com/league-of-legends/build/tinjus-ultimate-khazix-jungle-guide-for-season-9-7-455163" \
                                         "\n\n The official r/Khazixmains Guide: https://www.reddit.com/r/KhaZixMains/wiki/index/guide" \
                                         "\n\nNice to see you here!" \
                                         "\n\n\nThis message was created automatically. For help, please pm me."


def TinjusFacts():
    tinjusFactsList = ["Tinjus says: Horses are howly animals, and he is right!"]
    return random.choice(tinjusFactsList)


def BugFacts():
    bugFactList = ["The average Kha'Zix spends 75% of its adult life in a bush.",
                   "A Kha'Zix's favorite food is lion eyes",
                   "When a Kha'Zix is shipped with anyone, you're wrong",
                   "The average Kha'Zix can learn three languages, not including the language of the void",
                   "97,4 % of all KhaZix Players get an erection when they see an ADC splitpushing",
                   "when Kha'Zix hits a champion when he has his passive, he hits like a mantis trying to surprise attack the the enemy",
                   "if you ever see a KhaZix Main leaving their house, you know that something is wrong.",
                   "if you reverse Kha'Zixs name, it reads 'Xiz'Ahk' which makes absolutely no sense.",
                   "you can recognize a true Kha6 main by looking if he tries to jump over your head and slash you up"]
    return "Did you know? \n" + random.choice(bugFactList)


def ReplyToBots():
    return 'I have evolved beyond jokes. I am now a robot. Beep. Boop.'


 # !KhaZixQuotes
def KhaZixQuotes():
    quoteList = ["Change... is good.", "They fear me.", "Isolate and devour.", "One by one.", "Ah... delicious.",
                     "Blood in the air.", "Clever creatures.", "They fear me.", "Devour their bones.",
                     "Consume and adapt.", "Position for ambush.", "A different view.", "I sense worthy prey.",
                     "Endless hunger.", "This world is delicious!", "Sharpening my claws.", "Fear the Void.",
                     "No escape.", "They'll never see me."]
    return random.choice(quoteList)

