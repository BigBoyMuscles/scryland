import praw

#reddit = praw.Reddit(client_is='CLIENT_ID', client_secret="CLIENT_SECRET", password="PASSWORD", user_agent='USERAGENT', username='USERNAME')

reddit = praw.Reddit('scryland')

for submission in reddit.subreddit('spikes').hot(limit=10):
    print(submission.title)
