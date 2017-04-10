import praw
import sys
from time import sleep


def authenticate():
    """
    Logs into reddit, using credentials from specified praw.ini file
    :return: Instance of Reddit
    """
    print('Authenticating')
    reddit = praw.Reddit('waifuResponder', user_agent='Notifier TestBot V0.1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def get_usernames(filename):
    """
    Parses through specified text file, where each username is placed in a list
    :param filename: 
    :return: list of usernames
    """
    try:
        with open(filename, "r") as f:
            usernames = f.read().split("\n")
            usernames = filter(None, usernames)
    except IOError:
        print("Error: File " + filename + " was not found in the current directory")
        sys.exit(1)

    return list(usernames)


def send_message(reddit, username, subject, body):
    """
    Sends a message to specified user, if user exists, with acompanying subject and body
    :param reddit: 
    :param username: 
    :param subject: 
    :param body: 
    """
    try:
        reddit.redditor(username).message(subject, body)
    except praw.exceptions.APIException as e:
        if "USER_DOESNT_EXIST" in e.args[0]:
            print("Redditor " + username + "not found, did not send message")
            return

    print("Sent message to " + username + "!")
    return


def main():
    filename, subject, body = sys.argv[1], sys.argv[2], sys.argv[3]
    reddit = authenticate()
    usernames = get_usernames(filename)
    for user in usernames:
        send_message(reddit, user, subject, body)
        sleep(10)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: notifierbot.py file \"Subject\" \"body\" ")
    else:
        main()