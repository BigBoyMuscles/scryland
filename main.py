import praw
import logging

target_format = ['[standard]']

def main():

    reddit = praw.Reddit('scryland')

    spikes = reddit.subreddit('scrylandbeta')


    for submission in spikes.stream.submissions():

        process_submission(submission)


# grab new submissions to /r/spikes and see if they match our targeted format
def process_submission(submission):

    normalized_title = submission.title.lower()

    for format in target_format:

        if format in normalized_title:

            #print('Discovered targeted post: {}'.format(submission.title))
            print("Text: ", submission.selftext)

            break

if __name__ == "__main__":
    main()
