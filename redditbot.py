import praw
import time
import os
import requests


def authenticate():
    """
    Logs into reddit, using credentials from praw.ini file
    :return: Instance of Reddit
    """
    print('Authenticating')
    reddit = praw.Reddit('waifuResponder', user_agent='Waifu Comments')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def run_bot(reddit, comments_replied):
    """
    Reddit instance loops through all comments found on subreddit and replys to any comments with 'waifu' written
    :param reddit:
    :param comments_replied:
    """

    for comment in reddit.subreddit('kwespellTest').comments(limit=25):
        if '!waifu' in comment.body and comment.id not in comments_replied and not comment.author == reddit.user.me():
            print('Found string with id {}'.format(comment.id))

            comment_reply = "Also, here's a random Chuck Norris joke\n\n"

            chuck_norris_joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']

            comment_reply += ">" + chuck_norris_joke

            comment.reply('Your waifu is bad and you should feel bad' +
                          '\n\n [(Better Waifu)](https://cdn.awwni.me/woz3.jpg)')

            comment.reply(comment_reply)

            comments_replied.append(comment.id)

            with open("list_of_replied_comments.txt", "a") as txt:
                txt.write(comment.id + "\n")

    print('Pausing bot')
    time.sleep(10)


def get_saved_comments():
    if not os.path.isfile("list_of_replied_comments.txt"):
        comments_replied = []
    else:
        with open("list_of_replied_comments.txt", "r") as txt:
            comments_replied = txt.read()
            comments_replied = comments_replied.split("\n")
            comments_replied = filter(None, comments_replied)

    return list(comments_replied)


def main():
    reddit = authenticate()
    comments_replied = get_saved_comments()
    print(comments_replied)
    while True:
        run_bot(reddit, comments_replied)

if __name__ == '__main__':
    main()