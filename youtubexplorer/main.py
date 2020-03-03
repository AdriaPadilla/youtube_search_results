import youtubexplorer.extraction.get_videos as qy

queries = ["las vacunas matan"]
max_results = 2

def youtubexplore(queries, max_results):
	for query in queries:
		search_results = qy.get_search_results(query, max_results)

if __name__ == "__main__":
	youtubexplore(queries, max_results)


