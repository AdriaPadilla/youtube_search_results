from apiclient.discovery import build
from apiclient.errors import HttpError

import youtubexplorer.credentials.keys as cr
import youtubexplorer.classes.class_video as vi


DEVELOPER_KEY = cr.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_video_statistics(search_results, related_results):

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

	response_objects_list = []

	for result in search_results:
		result = result.__dict__		

		statistics_result = youtube.videos().list(
			id=result["videoId"],
			part="statistics",
			).execute()

		print(statistics_result)
