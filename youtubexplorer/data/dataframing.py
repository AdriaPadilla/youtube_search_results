import pandas as pd

def export_data(video_objects_list):

	all_data = []

	for video in video_objects_list:

		video_frame = pd.DataFrame({
			"Id": video.videoId,
			"seed": video.seed,
			"type": video.type,
			"publishedAt": video.publishedAt,
			"title": video.title,
			"description": video.description,
			"kind": video.kind,
			"channelId": video.channelId,
			"channelTitle": video.channelTitle,
			"liveBroadcastContent": video.liveBroadcastContent,
			"viewCount": video.viewCount,
			"likeCount": video.likeCount,
			"dislikeCount": video.dislikeCount,
			"favoriteCount": video.favoriteCount,
			"commentCount": video.commentCount,
			"link": "https://www.youtube.com/watch?v="+video.videoId,
			"duration": video.duration,
			"dimension": video.dimension,
			"definition": video.definition,
			"caption": video.caption,
			"licensedContent": video.licensedContent,
			}, index=[0])

		all_data.append(video_frame)

	all_data = pd.concat(all_data, ignore_index=True)
	all_data.to_excel("output.xlsx")
	print(all_data)
	
	return all_data


