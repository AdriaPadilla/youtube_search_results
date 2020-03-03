import youtubexplorer.extraction.get_search as qy
import youtubexplorer.extraction.get_related as qr
import youtubexplorer.extraction.get_statistics as stats


queries = ["vacunas"]
max_results = 2
max_related = 2

def youtubexplore(queries, max_results):
	for query in queries:
		search_results = qy.get_search_results(query, max_results)
		related_results = qr.get_related_results(search_results, max_related)
		objects = stats.get_video_statistics(search_results, related_results)


		print("original search response")
		print(search_results)
		print("related videos")
		print(related_results)

if __name__ == "__main__":
	youtubexplore(queries, max_results)


