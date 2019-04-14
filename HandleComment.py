import praw
import Reply

alreadyDone = []

KhaZixQuoteKeywordList = ['!khazixquote', '!Khazixquote', '!KhaZixQuote',
                           "Change... is good.", "They fear me.", "Isolate and devour.", "One by one.",
                            "Ah... delicious.","Blood in the air.", "Clever creatures.", "Devour their bones.",
                            "Consume and adapt.", "Position for ambush.", "A different view.", "I sense worthy prey.",
                            "Endless hunger.", "This world is delicious!", "Sharpening my claws.", "Fear the Void.",
                            "No escape.", "They'll never see me."]


TinjusFactKeywordList = ['!tinjusfacts', '!Tinjusfacts', '!TinjusFacts', 'Horse', "!horsefacts", "!horsefact",
                         '!tinjusfact', '!Tinjusfact', '!TinjusFact', "horse"]

BugFactKeywordList = ["bug", "Bug", "!bugfact", "!Bugfact", "!BugFact", "!khazixfact", "!KhaZixFact"]

NoobHelpKeywordList = ["I'm new", "Im new", "im new", "i'm new", "!noobHelp", "!NoobHelp", "!noobhelp", "!Noobhelp"]

BotHelpKeywordList = ["!help", "bugbot commands", "BuggyMemeBot commands", "!Help"]


def SelectReplyMsg(comment):
    KeywordInComment = False        #ik it would be less work to set it on true and set it on false in an else case
                                    #but this version leaves less room for errors
    try:
        for x in range(0, len(KhaZixQuoteKeywordList)): #khazix quotes
            if KhaZixQuoteKeywordList[x] in comment.body:
                msg = Reply.KhaZixQuotes()
                KeywordInComment = True

        for x in range(0, len(TinjusFactKeywordList)): #tinjus facts
            if TinjusFactKeywordList[x] in comment.body:
                msg = Reply.TinjusFacts()
                KeywordInComment = True

        for x in range(0, len(BugFactKeywordList)): #bug facts
            if BugFactKeywordList[x] in comment.body:
                msg = Reply.NoobHelp()
                KeywordInComment = True

        for x in range(0, len(BugFactKeywordList)): #bug facts
            if BugFactKeywordList[x] in comment.body:
                msg = Reply.BugFacts()
                KeywordInComment = True

        for x in range(0, len(BotHelpKeywordList)): #bug facts
            if BotHelpKeywordList[x] in comment.body:
                msg = Reply.BotHelp()
                KeywordInComment = True

        if KeywordInComment == True:
            ReplyToComment(msg, comment)

    except Exception as e:
        print(e)


def ReplyToComment(CommentToReply, comment):
    try:
        if comment.author != "BuggyMemeBot" and comment.id not in alreadyDone:
            comment.reply(CommentToReply)
            print("Comment delivered! I wrote: " + CommentToReply)
            alreadyDone.append(comment.id)
    except Exception as e:
        print(e)
    finally:
        if len(alreadyDone) > 250:
            alreadyDone.pop(0);     #goddamn it that so fucking dirty code, but it still works. Lets just assume that this sub will never have 250 comments in 3 posts


