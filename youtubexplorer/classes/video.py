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


	###
	### - This is the first request. You'll get n (= max_results) videos for query
	###

	def get_videos(query, max_results):

		video_list = []

		print("searching "+str(max_results)+" videos for query: "+str(query))

		search_response = youtube.search().list(
			q=query,
			part="id,snippet",
			maxResults=max_results,
			order="relevance",
			type="video",
			safeSearch="none",
			videoDuration="medium", 
			).execute()

		results = search_response["items"]

		###
		### - For each video, we request metrics, statistics, etc...
		###

		for result in results:	

			print(result["snippet"]["title"])

			vid_statistics = youtube.videos().list(
				id=result["id"]["videoId"],
				part="statistics, contentDetails",
				).execute()

			stats = vid_statistics["items"][0]

			search_response_object = Video(
				query,
				result["id"].get("kind", "Nan"),
				result["id"].get("videoId", "Nan"),
				result.get("kind", "Nan"),
				result["snippet"].get("channelId", "Nan"),
				result["snippet"].get("channelTitle", "Nan"),
				result["snippet"].get("description", "Nan"),
				result["snippet"].get("liveBroadcastContent", "Nan"),
				result["snippet"].get("publishedAt", "Nan"),
				result["snippet"].get("title", "Nan"),
				stats["statistics"].get("viewCount", "Nan"),
				stats["statistics"].get("likeCount", "Nan"),
				stats["statistics"].get("dislikeCount", "Nan"),
				stats["statistics"].get("favoriteCount", "Nan"),
				stats["statistics"].get("commentCount", "Nan"),
				stats["contentDetails"].get("duration", "Nan"),
				stats["contentDetails"].get("dimension", "Nan"),
				stats["contentDetails"].get("definition", "Nan"),
				stats["contentDetails"].get("caption", "Nan"),
				stats["contentDetails"].get("licensedContent", "Nan"),
				)
			video_list.append(search_response_object)

		return video_list

	##
	## - "get_related_videos" function is very similar to the one above, but this use the IDs 
	##   of the videos obtained in the first search, to find related videos.
	##
	## - If "get_related" (in main.py) equals True, the function will be activated. Else, will pass.
	##
	## - if "iteration_n" > 0, "while" condition will be activated and results 
	##   will be iterated in this function. IDs from related videos will be used to find new related videos.
	##

	def get_related_videos(seed_list, related_max):

		related_videos_list = []

		for seed in seed_list:

			print("related videos for seed:" +seed)

			response = youtube.search().list(
				part="id,snippet",
				maxResults=related_max,
				relatedToVideoId=seed,
				type="video",
				order="relevance",
				safeSearch="none",
				videoDuration="medium", 
				).execute()

			videos = response["items"]

			for video in videos:

				print(video["snippet"]["title"])

				stats_response = youtube.videos().list(
				id=video["id"]["videoId"],
				part="statistics, contentDetails",
				).execute()

				stats = stats_response["items"][0]

				related_video = Video(
					seed,
					video["id"].get("kind", "Nan"),
					video["id"].get("videoId", "Nan"),
					"related_video",
					video["snippet"].get("channelId", "Nan"),
					video["snippet"].get("channelTitle", "Nan"),
					video["snippet"].get("description", "Nan"),
					video["snippet"].get("liveBroadcastContent", "Nan"),
					video["snippet"].get("publishedAt", "Nan"),
					video["snippet"].get("title", "Nan"),
					stats["statistics"].get("viewCount", "Nan"),
					stats["statistics"].get("likeCount", "Nan"),
					stats["statistics"].get("dislikeCount", "Nan"),
					stats["statistics"].get("favoriteCount", "Nan"),
					stats["statistics"].get("commentCount", "Nan"),
					stats["contentDetails"].get("duration", "Nan"),
					stats["contentDetails"].get("dimension", "Nan"),
					stats["contentDetails"].get("definition", "Nan"),
					stats["contentDetails"].get("caption", "Nan"),
					stats["contentDetails"].get("licensedContent", "Nan"),			
					)
				related_videos_list.append(related_video)

		return related_videos_list
    

	##	- Explore_videos need 4 variables defined in main.py
	##	>> query = the keyword to search on youtube search module.
	##	>> max_results = The number of results you'll get from search response
	##	>> get_related = (Bool) True or False. If True, you'll get related videos for search response.
	##										   If False, function will skip this step. You'll get only search response.
	##	>> max_related = The number of related videos you'll get for each seed. 
	##	>> iteration_n = The number of iterations over get_related_videos
	##
	##	Note: Seeds to iterate over get_related_videos == the previous itertion videos IDs. 


	def explore_videos(query, max_results, get_related, max_related, iteration_n):

		videos = Video.get_videos(query, max_results)

		if get_related == True:

			seed_list = []

			for video in videos:
				seed = video.videoId
				seed_list.append(seed)

			related_videos_list = Video.get_related_videos(seed_list, max_related)

			videos.extend(related_videos_list)

			more_related_videos = related_videos_list

			iteration_counter = 0

			while iteration_counter < iteration_n:

				seed_list = []

				for video in more_related_videos:
					seed = video.videoId
					seed_list.append(seed)

				more_related_videos = Video.get_related_videos(seed_list, max_related)
				videos.extend(more_related_videos)
				iteration_counter += 1
				
		else:
			pass

		return videos

	##	- explore_related starts froma a list of seeds. Seed == videos IDs, defined in main.py
	##										  
	##	>> max_related = The number of related videos you'll get for each seed. 
	##	>> iteration_n = The number of iterations over get_related_videos
	##
	##	Note: Seeds to iterate over get_related_videos == the previous itertion videos IDs. 

	def explore_related(seed_list, max_related, iteration_n):

		videos = []

		related_videos = Video.get_related_videos(seed_list, max_related)

		videos.extend(related_videos)

		more_related_videos = related_videos

		iteration_counter = 0

		while iteration_counter < iteration_n:

			seed_list = []

			for video in more_related_videos:
				seed = video.videoId
				seed_list.append(seed)

			more_related_videos = Video.get_related_videos(seed_list, max_related)
			videos.extend(more_related_videos)
			iteration_counter += 1

		return videos