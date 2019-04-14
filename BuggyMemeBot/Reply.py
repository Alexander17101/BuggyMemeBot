import praw
import random
import HandleComment
# reply class, it does NOT decide what to reply, but only generate the message to reply!


# keyword: !tinjusfacts
def TinjusFacts():
    tinjusFactsList = ["Tinjus says a", "Tinjus says b", "Tinjus says c"]
    return random.choice(tinjusFactsList)


def BugFacts():
    return 0


def PrintA():
    print("a")


 # !KhaZixQuotes
def KhaZixQuote():
    quoteList = ["Change... is good.", "They fear me.", "Isolate and devour.", "One by one.", "Ah... delicious.",
                     "Blood in the air.", "Clever creatures.", "They fear me.", "Devour their bones.",
                     "Consume and adapt.", "Position for ambush.", "A different view.", "I sense worthy prey.",
                     "Endless hunger.", "This world is delicious!", "Sharpening my claws.", "Fear the Void.",
                     "No escape.", "They'll never see me."]
    return random.choice(quoteList)

# annoying stuff and "easter eggs"


def BotAnswer():
    return 'I have evolved beyond jokes. I am now a robot. Beep. Boop.'
