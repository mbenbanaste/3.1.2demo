# users, comments, posts

class User:
    def __init__(self, user_id, num_posts, reputation, mod_status, can_post):
        self.username = user_id
        self.num_posts = num_posts
        self.reputation = reputation
        self.mod_status = mod_status
        self.can_post = can_post

    def post_topic(self, title, tags, description):
        # post topic here
        topic = Topic(title, tags, description)
        return topic

class Topic:
    def __init__(self, title, tags, description):
        self.title = title
        self.tags = tags
        self.description = description
        # self.is_closed = False

    # def close(self):
    #     self.is_closed = True

class Comment:
    def __init__(self, text, up_votes, down_votes, moderated):
        self.text = text
        self.up_votes = up_votes
        self.down_votes = down_votes
        self.moderated = moderated

sarah = User(99, 0, 0, True, True)
smoothie_topic = sarah.post_topic(
    "smoothies",
    ["food", "healthy"],
    "smoothies are the best, love smoothies, can't get enough smoothies.",
)
# smoothie_topic.close()
