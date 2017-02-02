import numpy as np
import json
tweets=[]
for line in open('/home/ujjax/Desktop/data/black.txt'):
  try:
    tweets.append(json.loads(line))
  except:
    pass

ids = []
texts = []
times = []
screen_names=[]
names=[]
mentions1=[]
hashtags1=[]
urls1=[]
lats=[]
lons=[]
place_names=[]
place_types=[]

for tweet in tweets:
      string = str(tweet['text'].encode("utf-8"))
      string = string.replace(",", " , ")
      string = string.replace('"',' " ')
      string = string.replace("'", " ' ")
      string = string.replace("?", " ? ")
      string = string.replace("}", " } ")
      string = string.replace("{", " { ")
      string = string.replace("/", " / ")
      string = string.replace(".", " . ")
      string = string.replace("|", " | ")
      string = string.replace("\", " \ " )
      count =0
      #print string
      words = string.split()
      for word in words:
          if word[0] == '#':
              #print type(word[1:].lower())
              print word[1:]
              data[count,0]= word[1:]
              if 'created_at' in tweet:
                  #print type(tweet['created_at']encode("utf-8"))
                  data[count,1] = str(tweet['created_at'].encode("utf-8"))

              if 'user' in tweet:
                  if 'screen_name' in tweet['user']:
                      data[count,2]=tweet['user']['screen_name'].encode("utf-8")
                  if 'name' in tweet['user']:
                      data[count,2] = tweet['user']['name'].encode("utf-8")
              count += 1

print data

"""


  if 'created_at' in tweet:
      times.append(tweet['created_at'])
  if 'user' in tweet:
      if 'screen_name' in tweet['user']:
          screen_names.append(tweet['user']['screen_name'])
      if 'name' in tweet['user']:
          names.append(tweet['user']['name'])
  if 'entities' in tweet:
      if 'user_mentions' in tweet['entities']:
          if len(tweet['entities']['user_mentions']) >= 1:
              mentions1.append(tweet['entities']['user_mentions'][0]['screen_name'])
      if 'hashtags' in tweet['entities']:
          if len(tweet['entities']['hashtags']) >= 1:
              hashtags1.append(tweet['entities']['hashtags'][0]['text'])
      if 'urls' in tweet['entities']:
          if len(tweet['entities']['urls']) >= 1:
              urls1.append(tweet['entities']['urls'][0]['expanded_url'])
  if 'geo' in tweet:
      if tweet['geo']:
          lats.append(tweet['geo']['coordinates'][0])
          lons.append(tweet['geo']['coordinates'][1])
  if  'place' in tweet:
      if tweet['place']:
               place_names.append(tweet['place']['full_name'])
               place_types.append(tweet['place']['place_type'])
output = open('out.csv', 'w')
#print os.getcwd()
rows = zip(ids, times, texts, screen_names, names, mentions1, hashtags1, urls1, lats, lons, place_names, place_types)
from csv import writer
csv = writer(output)
i=0
for row in rows:
    values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
    csv.writerow(values)
output.close()

"""
