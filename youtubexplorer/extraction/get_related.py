from apiclient.discovery import build
from apiclient.errors import HttpError

import youtubexplorer.credentials.keys as cr
import youtubexplorer.classes.class_video as vi


DEVELOPER_KEY = cr.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_related_results(search_results, max_related):

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

	related_objects_list = []

	for seed in search_results:
		seed = seed.__dict__
		seed_id = seed["videoId"]

		print("related videos for seed:" +seed_id)

		related_response = youtube.search().list(
			part="id,snippet",
			maxResults=max_related,
			relatedToVideoId=seed_id,
			type="video",
			order="date",
			safeSearch="none",
			videoDuration="medium", 
			).execute()

		results = related_response["items"]

		for result in results:
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
			)
			related_objects_list.append(related_response_object)

	return(related_objects_list)