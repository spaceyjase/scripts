#!/usr/bin/python
import praw
import pdb
import re
import os

reddit = praw.Reddit('rrbot')

subreddit = reddit.subreddit("bodyweightfitness")

what_regex = "w[h]?at('s| is| does) (the rr|rr)( stand for)?|where do i find the acronyms\?"

post_store = "posts_replied_to.txt"
comment_store = "comments_replied_to.txt"

reply_text = "The RR is the [Recommended Routine](https://www.reddit.com/r/bodyweightfitness/wiki/kb/recommended_routine) (I am a bot, flex-beep-boop) ^[(PM)](https://www.reddit.com/message/compose?to=spaceyjase)."

if not os.path.isfile(post_store):
    posts_replied_to = []
else:
    with open(post_store, "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

if not os.path.isfile(comment_store):
    comments_replied_to = []
else:
    with open(comment_store, "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

print("Fetching posts...")

for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        if re.search(what_regex, submission.selftext, re.IGNORECASE):
            # reply to post
            submission.reply(reply_text)
            print("Match found, rrbot replying to: [", submission.title)
            # store the submission id into our list
            posts_replied_to.append(submission.id)
        # also search comments
        for comment in submission.comments.list():
            if comment.id not in comments_replied_to and hasattr(comment, 'body'):
                # print("\tcomment: [" + comment.id + "]")
                if re.search(what_regex, comment.body, re.IGNORECASE):
                    print("\tMatch found, replying to [" + comment.id + "]")
                    comment.reply(reply_text)
                    comments_replied_to.append(comment.id)

# write updated lists back to the file
with open(post_store, "w") as f:
    for posts_id in posts_replied_to:
        f.write(post_id + "\n")

with open(comment_store, "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")

print("Finished!")
