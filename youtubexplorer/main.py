import youtubexplorer.classes.video as vid
import youtubexplorer.data.dataframing as frame

v = vid.Video

queries = ["coronavirus"]
seed_list = ["AyAd_3u-llY", "Z2mw6aglRuM"]


max_results = 1		## Nº of results in search 
get_related = True 	## ¿Want related videos? False / True (respect upper case in capital)
max_related = 1		## Max nº of related videos 
iteration_n = 0		## Nº of iterations over get related function

def explore_search(queries):

	for query in queries:

		videos = v.explore_videos(query, max_results, get_related, max_related, iteration_n)

		frame.export_data(videos)

def explore_related(seed_list):

		videos = v.explore_related(seed_list, max_related, iteration_n)

		frame.export_data(videos)
		
if __name__ == "__main__":
	explore_related(seed_list)


