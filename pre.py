import json
tweets = []

for line in open('foo/deepika.json'):
  try:
    tweets.append(json.loads(line))
  except:
    pass
print(len(tweets))

d = {}
value = 0
total = 0
for tweet in tweets :
    print(tweet['entities']['urls'][0])
    string = str(tweet['created_at'])
    string = string.replace(",", " , ")
    string = string.replace('"', ' " ')
    string = string.replace("'", " ' ")
    string = string.replace("?", " ? ")
    string = string.replace("}", " } ")
    string = string.replace("{", " { ")
    string = string.replace("/", " / ")
    string = string.replace(".", " . ")
    string = string.replace("|", " | ")

    words = string.split()
    count = 1

    s = ''

    for word in words :

      #  print(word)
        if count <=3  :
            s = s + ' ' + word
        elif count == 6 :
            s = s + ' ' + word
        count+= 1

    #print(s)


    if s in d :
       d[s] = d[s] + 1
    else :
       d[s] = 1

for k in d :
    value+=1
    total+=d[k]

if((total/value) >= 20) :
    print ('active')
else :
    print('inactive')
