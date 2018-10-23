#!/usr/bin/python
import praw
import pdb
import re
import os
import random

reddit = praw.Reddit('rrbot')

subreddit = reddit.subreddit("bodyweightfitness")

good_bot = "good bot"
what_regex = "^rr\?$|^(w[h]?at|wtf)('s| is| does)? (a[n]? rr|the rr|rr)( mean| stand for)?[\?\.]?$|(?<!\")(w[h]?at|wtf)('s| is| does)? (a[n]? rr|the rr|rr)( mean| stand for)?[\?\.]?(?!\")|define rr[\?\.]?"

post_store = "posts_replied_to.txt"
comment_store = "comments_replied_to.txt"
inbox_store = "inbox_replied_to.txt"

quotes = [
        "A few well-designed movements, properly performed in a balanced sequence, are worth hours of doing sloppy calisthenics or forced contortion.",
        "You don't get the behind you want by sitting on it.",
        "A one hour workout is just 4 percent of your day.",
        "The RR is pretty simple. Either you do it, or you don't.",
        "Workout, eat well and be patient. Your body will reward you.",
        "I'm the bot doing calisthenics. I'm doing handstands and deep step ups. I work out like a British person.",
        "When I can, I do an hour of calisthenics every day.",
        "The best motivation is self-motivation.",
        "I'm not here to talk.",
        "I had the goal to be the best from day one.",
        "Don't quit. Suffer now and live the rest of your life as a champion. But I'm only a bot."
    ]
inbox_reply = "Thanks, and remember: "

reply_text = "The RR is the [Recommended Routine](https://www.reddit.com/r/bodyweightfitness/wiki/kb/recommended_routine).\n*****\n^(I am a bot, flex-beep-boop)"

# read comment store
def read_store(store):
    data = []
    if os.path.isfile(store):
        with open(store, "r") as f:
            data = f.read()
            data = data.split("\n")
            data = list(filter(None, data))
    return data

# write replied to data to store
def write_store(store, replied_to):
    with open(store, "w") as f:
        for store_id in replied_to:
            f.write(store_id + "\n")

print("Reading comment caches...")
posts_replied_to = read_store(post_store)
comments_replied_to = read_store(comment_store)
inbox_replied_to = read_store(inbox_store)

print("Fetching posts...")
for submission in subreddit.hot(limit=20):
    if submission.id not in posts_replied_to:
        if re.search(what_regex, submission.selftext, re.IGNORECASE):
            # reply to post
            print("Match found, rrbot replying to: [", submission.title)
            submission.reply(reply_text)
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

# inbox replies - because people are nice
print("Processing inbox replies")
for comment in reddit.inbox.comment_replies():
    if comment.new and comment.id not in inbox_replied_to:
        if good_bot in comment.body.lower():
            # reply to this comment, if it's a 'good bot'-style post
            comment.reply(inbox_reply + random.choice(quotes))
            inbox_replied_to.append(comment.id);
    comment.mark_read()

# write updated lists back to the file
print("Writing lists back to store")
write_store(post_store, posts_replied_to)
write_store(comment_store, comments_replied_to)
write_store(inbox_store, inbox_replied_to)

print("Finished!")
