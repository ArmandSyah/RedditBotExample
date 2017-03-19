import praw
import sys
import time


def botlogin():
    '''
    Logs into reddit, using credentials from praw.ini file
    :return: Instance of Reddit
    '''
    print('Logging in')
    return praw.Reddit('waifuResponder', user_agent='Kwespy v0.1')


def runbot(reddit):
    '''
    Reddit instance loops through all comments found on subreddit and replys to any comments with 'waifu' written
    :param reddit:
    '''
    for comment in reddit.subreddit('kwespellTest').comments(limit=25):
        if 'waifu' in comment.body:
            print("Found string")
            comment.reply("Your waifu is bad and you should feel bad [Better Waifu](https://cdn.awwni.me/woz3.jpg)")

    print('Pausing bot')
    time.sleep(10)


while True:
    try:
        reddit = botlogin()
    except praw.exceptions:
        print("failed login")
        sys.exit(1)
    runbot(reddit)