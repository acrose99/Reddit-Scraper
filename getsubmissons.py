import praw
import getusercomments


def getSubmissions(reddit, displayName, data):
    subreddit = reddit.subreddit(displayName)
    subredditTitle = "/r/" + displayName
    users = []
    method = input(
        "Do you want to get data from the top posts, the hot posts, the new posts, or the controversial posts?")
    limit = int(input("How many posts do you want to parse from the subreddit?"))
    if method.upper() == "NEW":
        for submission in subreddit.new(limit=limit):
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
    elif method.upper() == "HOT":
        for submission in subreddit.hot(limit=limit):
            submissionTitle = submission.title
            # print(submissionTitle)
            comments = submission.comments
            for comment in comments:
                user = comment.author
                users.append(user)
                # print(subredditTitle)
                # print("Submission: " + submissionTitle)
                # print("Comment: " + comment.body)
                # print("User: " +  str(user))
    elif method.upper() == "TOP":
        for submission in subreddit.top(limit=limit):
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
    elif method.upper() == "CONTROVERSIAL":
        for submission in subreddit.controversial(limit=limit):
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
    else:
        print('INVALID INPUT')
    getusercomments.getComments(reddit, users, subredditTitle)
