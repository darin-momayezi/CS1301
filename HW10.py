class Video:

    def __init__(self, sound, minutes):
        self.sound = sound
        self.likes = 0
        self.comments = 0
        self.minutes = 1.0

    def __str__(self):
        return "Video has {} likes and is {} minute long.".format(self.likes, self.minutes)

    def __eq__(self, other):
        return self.sound == other.sound and self.comments == other.comments

    def __repr__(self):  # provided
        return f"Video({self.sound}, {self.likes}, {len(self.comments)}, {self.minutes})"


class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.following = []
        self.videos = []
        self.isPrivate = True

    def changePassword(self, oldPassword, newPassword):
        if oldPassword != self.password:
            return 'Invalid password.'
        else:
            self.password = newPassword

    def isInfluencer(self):
        if len(self.videos) >= 5:
            for video in self.videos:
                if video.likes >= 50000 and video.comments >= 1000 and video.isPrivate == False:
                    return True
                else:
                    return False

    def follow(self, followedAccount):
        self.following.append(followedAccount)
        followedAccount.followers += self

    def unfollow(self, unfollowedAccount):
        if unfollowedAccount in self.following:
            self.following.remove(unfollowedAccount)
            unfollowedAccount.followers.remove(self)
        else:
            pass

    def __lt__(self, other):
        myLikes = 0
        otherLikes = 0
        for video in self.videos:
            myLikes += video.likes
        for video in other.videos:
            otherLikes += video.likes
        if myLikes < otherLikes:
            return self < other
        elif myLikes > otherLikes:
            return other < self

    def __eq__(self, other):
        return self.username == other.username and self.password == other.password

    def __repr__(self):  # provided
        return f"Account({self.username}, {self.password}, {len(self.followers)}, {len(self.following)}, {len(self.videos)}, {self.isPrivate})"


class TikTok:
    def __init__(self):  # provided
        self.accounts = []
        self.followers = []
        self.following = []
        self.videos = []
        self.soundBase = []

    def makeAccount(self, username, password):
        if username in self.accounts:
            return "Username is already taken."
        else:
            newAccount = Account(username, password)
            self.accounts.append(newAccount)
            self.followers.append((username, newAccount.followers))
            self.following.append((username, newAccount.following))

    def changePrivacy(self, user):
        if user.isPrivate:
            user.isPrivate = False
        else:
            user.isPrivate = True

    def deleteAccount(self, user):
        if user in self.accounts:
            self.accounts.remove(user)
            self.followers.remove((user.username, user.followers))
            self.following.remove((user.username, user.following))

    def post(self, user, sound, minutes):
        seconds = 60 * minutes
        if user not in self.accounts:
            return "You must have a registered account to post."
        elif seconds < 15:
            return "Video must be at least 15 seconds."
        else:
            newVideo = Video(sound, minutes=minutes)
            self.videos.append(newVideo)

    def getInfluencers(self):
        influencers = []
        for account in self.accounts:
            if account.isInfluencer():
                influencers.append(account)

        return influencers

    def __repr__(self):  # provided
        return f"TikTok Object with {len(self.accounts)} accounts and {len(self.videos)} videos"
