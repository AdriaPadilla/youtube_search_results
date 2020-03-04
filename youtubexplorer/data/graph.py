import pandas as pd

def create_graph(video_objects_list):

	edges_list = []

	for video in video_objects_list:

		source = video.seed
		target = video.videoId

		node_pair = str(source)+";"+str(target)
		edges_list.append(node_pair)

		print("creating graph: "+node_pair)

	edges_list_frame = pd.DataFrame(edges_list)
	edges_list_frame.to_csv("edges_graph.csv", index=False, header=False)