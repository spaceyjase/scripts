#!/usr/bin/python
import praw
import pdb
import re
import os

reddit = praw.Reddit('rrbot')

subreddit = reddit.subreddit("bodyweightfitness")

post_store = "posts_replied_to.txt"
comment_store = "comments_replied_to.txt"

reply_text = "The RR is the [Recommended Routine](https://www.reddit.com/r/bodyweightfitness/wiki/kb/recommended_routine) (I am a bot, flex-beep-boop)."

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

for submission in subreddit.new(limit=10):
    if submission.id not in posts_replied_to:
        if re.search("what is the rr", submission.selftext, re.IGNORECASE) or re.search("what's the rr", submission.selftext, re.IGNORECASE):
            # reply to post
            submission.reply(reply_text)
            print("Match found, rrbot replying to: [", submission.title)
            # store the submission id into our list
            posts_replied_to.append(submission.id)
        # also search comments
        for comment in submission.comments.list():
            if comment.id not in comments_replied_to:
                # print("\tcomment: [" + comment.id + "]")
                if re.search("what is the rr", comment.body, re.IGNORECASE) or re.search("what's the rr", comment.body, re.IGNORECASE):
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

