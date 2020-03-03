from apiclient.discovery import build
from apiclient.errors import HttpError

import youtubexplorer.credentials.keys as cr
import youtubexplorer.classes.class_video as vi


DEVELOPER_KEY = cr.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_search_results(query, max_results):

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

	response_objects_list = []

	search_response = youtube.search().list(
		q=query,
		part="id,snippet",
		maxResults=max_results,
		order="date",
		type="video",
		safeSearch="none",
		videoDuration="medium", 
		).execute()

	results = search_response["items"]

	for result in results:
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
		)
		response_objects_list.append(search_response_object)

	return(response_objects_list)