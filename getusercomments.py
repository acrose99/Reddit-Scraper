import praw
import csv
import pandas as pd

def getComments(reddit, users, subredditOfOrgin):
    comments = []
    for user in users:
        usercomments = reddit.redditor(str(user)).comments.new(limit=10)
        for usercomment in usercomments:
            # print("Subreddit: " + subredditOfOrgin)
            # print("Submission: " + usercomment.submission.title)
            #  print("Comment: " + usercomment.body)
            comment = usercomment.body
            submission = usercomment.submission.title
            comments.append({'Comment': comment, 'SubredditofOrgin': subredditOfOrgin, 'Submission': submission, 'User': user})
    pd.DataFrame(comments).to_csv('comments.csv')

