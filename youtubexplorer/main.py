import youtubexplorer.extraction.get_videos as qy
import youtubexplorer.data.dataframing as frame
import youtubexplorer.data.graph as gg


queries = ["las vacunas matan"]
max_results = 10

def youtubexplore(queries, max_results):
	for query in queries:
		video_objects_list = qy.get_search_results(query, max_results)
		frame.export_data(video_objects_list)
		gg.create_graph(video_objects_list)


if __name__ == "__main__":
	youtubexplore(queries, max_results)


