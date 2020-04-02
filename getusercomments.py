import praw
import csv
import pandas as pd


def getComments(reddit, users, subredditOfOrgin):
    comments = []
    limit = int(input("How many comments per user do you want"))
    method = input(
        "Do you want to get data from their top comments, the hot comments, the comments posts, or the comments posts?")
    print(
        "Waiting... Depending on the amount of data you want, this may take a long time! Make sure this continues to run")
    if method.upper() == "NEW":
        for user in users:
            usercomments = reddit.redditor(str(user)).comments.new(limit=limit)
            for usercomment in usercomments:
                # print("Subreddit: " + subredditOfOrgin)
                # print("Submission: " + usercomment.submission.title)
                #  print("Comment: " + usercomment.body)
                comment = usercomment.body
                submission = usercomment.submission.title
                comments.append(
                    {'Comment': comment, 'SubredditofOrgin': subredditOfOrgin, 'Submission': submission, 'User': user})
    elif method.upper() == "HOT":
        for user in users:
            usercomments = reddit.redditor(str(user)).comments.hot(limit=limit)
            for usercomment in usercomments:
                # print("Subreddit: " + subredditOfOrgin)
                # print("Submission: " + usercomment.submission.title)
                #  print("Comment: " + usercomment.body)
                comment = usercomment.body
                submission = usercomment.submission.title
                comments.append(
                    {'Comment': comment, 'SubredditofOrgin': subredditOfOrgin, 'Submission': submission, 'User': user})
    elif method.upper() == "TOP":
        for user in users:
            usercomments = reddit.redditor(str(user)).comments.top(limit=limit)
            for usercomment in usercomments:
                # print("Subreddit: " + subredditOfOrgin)
                # print("Submission: " + usercomment.submission.title)
                #  print("Comment: " + usercomment.body)
                comment = usercomment.body
                submission = usercomment.submission.title
                comments.append(
                    {'Comment': comment, 'SubredditofOrgin': subredditOfOrgin, 'Submission': submission, 'User': user})
    elif method.upper() == "CONTROVERSIAL":
        for user in users:
            usercomments = reddit.redditor(str(user)).comments.controversial(limit=limit)
            for usercomment in usercomments:
                # print("Subreddit: " + subredditOfOrgin)
                # print("Submission: " + usercomment.submission.title)
                #  print("Comment: " + usercomment.body)
                comment = usercomment.body
                submission = usercomment.submission.title
                comments.append(
                    {'Comment': comment, 'SubredditofOrgin': subredditOfOrgin, 'Submission': submission, 'User': user})
    else:
        print('INVALID INPUT')
        # TODO add actual error handling
    pd.DataFrame(comments).to_csv(subredditOfOrgin + '.csv')
