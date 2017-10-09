
# coding: utf-8

# In[15]:

import json
import pandas as pd
import re


# In[53]:

f= open('/home/shivam/Downloads/MumbaiRain (1).txt','r') 


# In[54]:

avail = ['bottled water','drinking water','suppl','electricity','cloth','food','shelter','bags of','medical aid','rescue','medic','camp','relie',
'volunt','offer','mone','donat','helicopter','bread','biscuit','rice','boat','ambul' ,'airline']


# In[55]:

need = ['requir','want food','send','need of','shelter','drinking water','help with','mone','need food']


# In[56]:

text = []
for line in f:
    try:
        if(str(json.loads(line)['text'])[:2] == 'RT'):
            continue
        flag = 1    
        for key in need:
            if key in (str(json.loads(line)['text']).lower()):
                text.append([json.loads(line)['text'],'1'])
                flag = 0
                break
        for key in avail and flag == 1:
            if key in (str(json.loads(line)['text']).lower()):
                text.append([json.loads(line)['text'],'0'])
                break                
    except:
        pass


# In[57]:

text[:1]


# In[58]:

def clean(strings):
        final=[]
        for stri in strings:
            string = stri[0]
            string = re.sub(r"http\S+", "", string)
            string = re.sub(r"@\S+", "", string)
            string = string.replace("#", " ")
            string = string.replace("\t"," ")
            string = string.replace(",", " ")
            string = string.replace(";", " ")
            string = string.replace('"', ' ')
            string = string.replace("'", " ")
            string = string.replace("?", " ")
            string = string.replace("}", " ")
            string = string.replace("{", " ")
            string = string.replace("/", " ")
            string = string.replace(".", " ")
            string = string.replace("|", " ")
            string = string.replace("\n", " ")
            string = string.lower()
            final.append((' '.join([w for w in string.split()]),stri[1]))
        return final


# In[59]:

text = clean(text)


# In[60]:

len(text)


# In[61]:

df= pd.DataFrame(text, columns = ['tweet','type'])


# In[62]:

df.head()


# In[63]:

df.to_csv('/home/shivam/Desktop/mumbai_preprocess.csv', sep=',', encoding='utf-8')


# In[ ]:



