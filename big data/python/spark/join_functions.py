def split_fileA(line):
    # split the input line in word and count on the comma
    keyValue = line.split(',')
    # turn the count to an integer  
    word = keyValue[0]
	count = int(keyValue[1])
    return (word, count)
	
def split_fileB(line):
    # split the input line into word, date and count_string
    keyValue = line.split(',')
	keys = keyValue[0].split(' ')
	date = keys[0]
	word = keys[1]
	count_string = keyValue[1]
    return (word, date + " " + count_string) 
	
	
	
	
def split_show_views(line):
    keyValue = line.split(',')
	show = keyValue[0]
	views = int(keyValue[1])
    return (show, views)

show_views = show_views_file.map(split_show_views)

show_channel_file = sc.textFile("/user/cloudera/input_join2/join2_genchan?.txt")

def split_show_channel(line):
    keyValue = line.split(',')
	show = keyValue[0]
	channel = keyValue[1]
    return (show, channel)
	
show_channel = show_channel_file.map(split_show_channel)


joined_dataset = show_views.join(show_channel) //[(u'PostModern_Cooking', (1038, u'DEF'))]
def extract_channel_views(show_views_channel): 
	views_channel = show_views_channel[1]
    channel = views_channel[1]
	views = views_channel[0]
    return (channel, views)
	
channel_views = joined_dataset.map(extract_channel_views)

def some_function(a, b):
    some_result = a + b
    return some_result
	
channel_views.reduceByKey(some_function).collect()