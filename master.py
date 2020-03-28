import praw
import config
import getsubmissons
import http


def main():
    reddit = praw.Reddit(client_id=config.client_id,
                         client_secret=config.client_secret,
                         password=config.password,
                         user_agent=config.user_agent,
                         username=config.username)
    displayName = 'redditdev'
    print("You username is " + str(reddit.user.me()))
    getsubmissons.getSubmissions(reddit, displayName, 'submissions')


main()
