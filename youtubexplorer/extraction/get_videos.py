from apiclient.discovery import build
from apiclient.errors import HttpError

import youtubexplorer.credentials.keys as cr
import youtubexplorer.classes.class_video as vi


DEVELOPER_KEY = cr.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_search_results(query, max_results):

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

	video_objects_list = []

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

	for result in results:	

		print(result["snippet"]["title"])

		stats_response = youtube.videos().list(
			id=result["id"]["videoId"],
			part="statistics",
			).execute()

		stats = stats_response["items"][0]

		search_response_object = vi.Video(
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
			)
		video_objects_list.append(search_response_object)

	# GET RELATED VIDEOS

	related_videos_objects_list = []

	for seed in video_objects_list:
		seed = seed.__dict__
		seed_id = seed["videoId"]

		print("related videos for seed:" +seed_id)

		related_response = youtube.search().list(
			part="id,snippet",
			maxResults=10,
			relatedToVideoId=seed_id,
			type="video",
			order="relevance",
			safeSearch="none",
			videoDuration="medium", 
			).execute()

		results = related_response["items"]

		for result in results:

			print(result["snippet"]["title"])

			stats_response = youtube.videos().list(
			id=result["id"]["videoId"],
			part="statistics",
			).execute()

			stats = stats_response["items"][0]

			related_response_object = vi.Video(
				seed_id,
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
				)
			related_videos_objects_list.append(related_response_object)

	## ANOTHER ITERATION
	print("<<-- SECOND ITERATION -->")
	another_iteration_list = []

	for seed in related_videos_objects_list:
		seed = seed.__dict__
		seed_id = seed["videoId"]

		print("related videos for seed:" +seed_id)

		related_response = youtube.search().list(
			part="id,snippet",
			maxResults=10,
			relatedToVideoId=seed_id,
			type="video",
			order="relevance",
			safeSearch="none",
			videoDuration="medium", 
			).execute()

		results = related_response["items"]

		for result in results:

			print(result["snippet"]["title"])

			stats_response = youtube.videos().list(
			id=result["id"]["videoId"],
			part="statistics",
			).execute()

			stats = stats_response["items"][0]

			related_response_object = vi.Video(
				seed_id,
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
				)
			another_iteration_list.append(related_response_object)

	video_objects_list.extend(related_videos_objects_list, another_iteration_list)

	return(video_objects_list)