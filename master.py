import praw
import config
import getsubmissons
import http


def main():
    # TODO Create setup insead of manually.
    reddit = praw.Reddit(client_id=config.client_id,
                         client_secret=config.client_secret,
                         password=config.password,
                         user_agent=config.user_agent,
                         username=config.username)

    displayName = input("What subreddit would you like to parse?")
    print("Fetching data with the username " + str(reddit.user.me()) + " and your user agent is " + config.user_agent)
    getsubmissons.getSubmissions(reddit, displayName, 'submissions')


main()
