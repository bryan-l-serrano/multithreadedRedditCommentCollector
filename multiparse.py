#!usr/bin/env python
import praw, threading, re, sys

if len(sys.argv) == 2:
    number = int(sys.argv[1])
elif len(sys.argv) == 3:
    number = int(sys.argv[2])
else:
    number = int(input("How many subreddits would you like to collect the comments from: "))

def parse():
    r = praw.Reddit('CommentParser by u/captainpantsman')
    subreddit = r.get_subreddit('random')
    name = str(subreddit.display_name)
    print(name)
    f = open(name,'a+')
    for submission in subreddit.get_hot(limit=25):
        comments = praw.helpers.flatten_tree(submission.comments)
        for things in comments:
            things = str(things)
            things = re.sub(r'(\W){3}$', "", things)
            f.write(things)
            f.write(' ')
    f.close()


threads = []
for i in range(number):
    downloadThread = threading.Thread(target=parse)
    threads.append(downloadThread)
    downloadThread.start()

for things in threads:
    things.join()
print("Complete")