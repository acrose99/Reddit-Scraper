import praw
import getusercomments


def getSubmissions(reddit, displayName, data):
    subreddit = reddit.subreddit(displayName)
    subredditTitle = "/r/" + displayName
    users = []
    for submission in subreddit.top(limit=50):
        submissionTitle = submission.title
        # print(submissionTitle)
        comments = submission.comments
        for comment in comments:
            user = comment.author
            users.append(user)
            # print(subredditTitle)
            # print("Submission: " + submissionTitle)
            # print("Comment: " + comment.body)
            # print("User: " + str(user))
    getusercomments.getComments(reddit, users, subredditTitle)

def getUserComments(reddit, users, subredditOfOrgin):
    for user in users:
        getusercomments.getComments(reddit, user, subredditOfOrgin)
