import math

with open("datanew.csv", 'r') as csvfile:
	# Read each row in csv file
	rows = csvfile.readlines()

	# Split each row based on tabs (to form columns)
	for i in range(len(rows)):
		rows[i] = rows[i].split('\t')

	# Total number of words, plus 2 (for SITE and WORD_COUNT)
	number_of_words = len(rows[0])

	# Get word count per columns
	total_column_word_count = [0] * number_of_words

	for row in range(1, len(rows)):
		for column in range(1, number_of_words):
			rows[row][column] = int(rows[row][column]) 	# Convert each string number to an actual number
			total_column_word_count[column] += rows[row][column]

	### Euclidean Distance Similarity ###
	euclidean_distance_between_pairs = []

	for row in range(1, len(rows)):
		distance_between_each_pair = []
		for pair in range(1, len(rows)):
			# Compute euclidean distance
			distance_between_each_pair.append(math.sqrt(sum((rows[row][column] - rows[pair][column]) ** 2 for column in range(2, number_of_words))))

			euclidean_distance_between_pairs.append(distance_between_each_pair)
	print(euclidean_distance_between_pairs[0])
	## Convert to similarity ##
	# Find maximum
	'''maximum = 0.000000001
	for row in euclidean_distance_between_pairs:
		for column in row:
			if maximum < column:
				maximum = column
	# Take 1 - (distance / max) to standardize it
	for row in range(len(euclidean_distance_between_pairs)):
		for column in range(len(euclidean_distance_between_pairs[row])):
			euclidean_distance_between_pairs[row][column] = 1 - (euclidean_distance_between_pairs[row][column] / maximum)

	euclidean_distance_similarity = euclidean_distance_between_pairs

	#print(euclidean_distance_between_pairs)

with open('troll.csv','w') as fo:
	for i in range(1,361):
		print(euclidean_distance_similarity[i],file=fo)


'''
'''
	### Cosine Similarity ###

	cosine_similarity = []

	for row in range(1, len(rows)):
		distance_between_each_pair = []
		for pair in range(1, len(rows)):
			# Compute cosine_similarity
			d1_times_d2 = 0
			distance_d1 = 0
			distance_d2 = 0

			for column in range(2, number_of_words):
				d1_times_d2 += rows[row][column] * rows[pair][column]
				distance_d1 += rows[row][column] ** 2
				distance_d2 += rows[pair][column] ** 2

			distance_d1 = math.sqrt(distance_d1)
			distance_d2 = math.sqrt(distance_d2)

			cosine = d1_times_d2 / (distance_d1 * distance_d2)
			if cosine > 1.0:
				cosine = 1.0

			distance_between_each_pair.append(cosine)

		cosine_similarity.append(distance_between_each_pair)

	print(cosine_similarity)

	### Jaccard Similarity (binary) ###

	jaccard_similarity = []

	for row in range(1, len(rows)):
		distance_between_each_pair = []
		for pair in range(1, len(rows)):
			# Compute Jaccard
			intersect = 0
			union = 0
			for column in range(2, number_of_words):
				if ((rows[row][column] > 0) and (rows[pair][column] > 0)):
					intersect += 1
					union += 1
				elif rows[row][column] > 0 or rows[pair][column] > 0:
					union += 1
			# Jaccard = union / intersect
			if union == 0:
				union = 1
			distance_between_each_pair.append(intersect / union)

		jaccard_similarity.append(distance_between_each_pair)

	print(jaccard_similarity)
	'''
