import json
import datetime
from glob import glob


for file_name in glob('foo/*.json'):
    with open(file_name) as f :
        name = []
        data = []
        file_name = file_name[5:-5]
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
        mon = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
                  "Nov": 11, "Dec": 12}
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

            s = ''
            '''
            m = 0
            da = 0
            year = 0
            '''
            for word in words:

                #print(word)
                if count <= 3 :
                    s = s + ' ' + word
                elif count == 6:
                    s = s + ' ' + word
                '''
                if(y==1 or y == length - 1) :
                    if count == 2 :
                        m = d[word]
                    if count == 3 :
                        da = int(word)
                    if count == 6 :
                        year = int(word)
                    if y == 1 :
                        d1 = datetime.datetime(year, m, da)
                    if y == length - 1 :
                        d2 = datetime.datetime(year, m, da)
                        value = (d2 - d1).days
                '''
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
        if(v !=0 and (total/v) >= 20) :
            data.append('active')
        else :
            data.append('inactive')
        output = open('out/'+file_name+'.csv', 'w')
        # print os.getcwd()
        rows = zip(name,data)
        from csv import writer

        csv = writer(output)
        i = 0
        for row in rows:
            values = [(value if hasattr(value, 'encode') else value) for value in row]
            csv.writerow(values)
            #except :
                #pass
        output.close()

