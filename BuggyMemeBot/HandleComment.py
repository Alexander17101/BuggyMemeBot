import praw
import Reply

KhaZixQuoteKeywordList = ['!khazixquote', '!Khazixquote', '!KhaZixQuote',
                           "Change... is good.", "They fear me.", "Isolate and devour.", "One by one.", "Ah... delicious.",
                            "Blood in the air.", "Clever creatures.", "They fear me.", "Devour their bones.",
                            "Consume and adapt.", "Position for ambush.", "A different view.", "I sense worthy prey.",
                            "Endless hunger.", "This world is delicious!", "Sharpening my claws.", "Fear the Void.",
                            "No escape.", "They'll never see me."]


TinjusFactKeywordList = ['!tinjusfacts', '!Tinjusfacts', '!TinjusFacts', 'Horse',]

def SelectReplyMsg(comment):
    KeywordInComment = False #ik it would be less work to set it on true and set it on false in an else case but this version leaves less room for errors
    for x in range(0, len(KhaZixQuoteKeywordList)):
        if KhaZixQuoteKeywordList[x] in comment.body:
            msg = Reply.KhaZixQuote()
            KeywordInComment = True

    if KeywordInComment == True:
        ReplyToComment(msg, comment)
    return 0


def ReplyToComment(CommentToReply, comment):
    try:
        comment.reply(CommentToReply)
        print("Comment delivered! I wrote: " + CommentToReply)
    except:
        


