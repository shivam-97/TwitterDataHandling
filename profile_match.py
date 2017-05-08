import json
import datetime
from glob import glob


for file_name in glob('foo/*.json'):
    with open(file_name) as f :
        name = []
        data = []
        url = []
        file_name = file_name[4:-7]
        name.append(file_name)
        #try :
        #data.append(json.loads(f.read()))
        #print(1)
        tweets = []
        for line in f:
            try:
               tweets.append(json.loads(line))
            except:
               pass
        length = (len(tweets))
        d = {}

        v = 0
        total = 0
        y=0



        for tweet in tweets:
            y+=1
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
            string2 = str(tweet['text'])
            string2 = string2.replace(",", " , ")
            string2 = string2.replace('"', ' " ')
            string2 = string2.replace("'", " ' ")
            string2 = string2.replace("?", " ? ")
            string2 = string2.replace("}", " } ")
            string2 = string2.replace("{", " { ")
            string2 = string2.replace("/", " / ")
            string2 = string2.replace(".", " . ")
            string2 = string2.replace("|", " | ")
            words = string.split()
            words2 = string2.split()
            count = 1
            stri = tweet['user']['url']
            if stri is None :
                url.append(stri)
            else :
                url.append(tweet['user']['entities']['url']['urls'][0]['expanded_url'])
            s = ''

            for word in words:

                #print(word)
                if count <= 3 :
                    s = s + ' ' + word
                elif count == 6:
                    s = s + ' ' + word

                count += 1

            #print(s)
            flag = 0
            for w in words2:
                # print(w)
                if w == 'RT':
                    flag = 1

            if flag == 0:
                if s in d:
                    d[s] = d[s] + 1
                else:
                    d[s] = 1
        for k in d:
            v += 1
            total += d[k]
        #print(value)
        #print(total)

        url = list(set(url))
        if(v !=0 and (total/v) >= 20) :
            data.append('active')
            print(file_name)
        else :
            data.append('inactive')
        output = open('out/'+file_name+'.csv', 'w')
        # print os.getcwd()
        rows = zip(name,data,url)
        from csv import writer

        csv = writer(output)
        i = 0
        for row in rows:
            values = [(value if hasattr(value, 'encode') else value) for value in row]
            csv.writerow(values)
            #except :
                #pass
        output.close()

