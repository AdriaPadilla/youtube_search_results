from apiclient.discovery import build
from apiclient.errors import HttpError

### CREDENTIALS

import youtubexplorer.credentials.keys as cr

DEVELOPER_KEY = cr.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

### Autentication

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

### Init the class 

### Everything starts on explore() function (at the end of this code!).

class Video():
	def __init__(self,
		seed, 
		type,
		videoId,
		kind,
		channelId,
		channelTitle,
		description,
		liveBroadcastContent,
		publishedAt,
		title,
		viewCount,
		likeCount,
		dislikeCount,
		favoriteCount,
		commentCount,
		duration,
		dimension,
		definition,
		caption,
		licensedContent,
		):
		self.seed = seed
		self.type = type
		self.videoId = videoId
		self.kind = kind
		self.channelId = channelId
		self.channelTitle = channelTitle
		self.description = description
		self.liveBroadcastContent = liveBroadcastContent
		self.publishedAt = publishedAt
		self.title = title
		self.viewCount = viewCount
		self.likeCount = likeCount
		self.dislikeCount = dislikeCount
		self.favoriteCount = favoriteCount
		self.commentCount = commentCount
		self.duration = duration
		self.dimension = dimension
		self.definition = definition
		self.caption = caption
		self.licensedContent = licensedContent

