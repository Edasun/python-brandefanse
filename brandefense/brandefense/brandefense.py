import praw

a = praw.Reddit(client_id="1zC_xQsR8EXST3u9zOSs7A",
                     client_secret="RS3PM-J_fBpS8FN_p9pHdXdkqFgzhg",
                     user_agent="script by u/TopManufacturer5831",
                     redirect_uri="http://localhost:8080")

b = a.subreddit("australia")

for post in b.new(limit=10):
    print(post.title)
    print(post.url)
    print(post.score)
    print(post.num_comments)
    print("     ")
