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