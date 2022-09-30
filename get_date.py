import datetime
debug = False
'''
datetime_object = datetime.datetime.now()
print(datetime_object)

print(datetime_object.strftime("%d/%m/%Y, %H:%M:%S"))
'''

def find_text(t,sub1,sub2=''):

    start=([m.start() for m in re.finditer(sub1, t)])
    if sub2 != '':
        end=([m.start()+4 for m in re.finditer(sub2, t)])
        return start, end
    return start

# f= open("/home/pi/Documents/Python/streaming/match.txt","r")
# match_file = f.read()
# f.close()

# define an empty list
places = []
# open file and read the content in a list
with open('/home/pi/Documents/Python/streaming/match.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1].split(',')
        if len(currentPlace)==4:
            # add item to the list
            places.append(currentPlace)

# print(places[7])
# for i in range(4):
#     print(places[7][i])

# create dictionary from list
dict={}
for name2,url2,image2,fanart2 in places[7:-4]:
    d={}
    name2 = name2.replace('\'','')
    url2 = url2.replace('\'','')
    name2 = name2.replace(')','')
    name2 = name2.replace('(','')
    name2 = name2.replace('[COLOR white]','')
    name2 = name2.replace('[COLORwhite]','')
    name2 = name2.replace('[COLOR gold]','')
    name2 = name2.replace('[COLOR pink]','')
    name2 = name2.replace('[COLORred]','')
    name2 = name2.replace('[B]','')
    name2 = name2.replace('[/COLOR]','\r\n')
    name2 = name2.replace('[/I]','')
    name2 = name2.replace('[I]','')
    name2 = name2.replace('[/B]','')
    
    if 'sublink' in url2:
        #rectify bad url
        index=url2.find('sublink')
        url2=url2[index:]
        #replace tags
        url2 = url2.replace('sublink:LISTSOURCE:','<a href="')
        url2 = url2.replace('ublink:LISTSOURCE:','<a href="')
        url2 = url2.replace('::LISTNAME:','" target="new">')
        url2 = url2.replace('::#','</a>')
        url2 = url2.replace('\\\\r\\\\n', '\r\n')
        url2 = url2.replace('[COLORgold]','')
        url2 = url2.replace('[COLORorchid][/COLOR]','Link to video')
        url2 = url2.replace('[COLORorchid]','')
        url2 = url2.replace('[COLORred]','')
        url2 = url2.replace('[COLORwhite]','')
        url2 = url2.replace('[/COLOR]','')
    if debug:print(name2, url2)
    d['url']=url2
    d['img']=image2
    d['fanart']=fanart2
    dict[name2.strip()]=d

# end creating dictionary
print(len(dict))


# saving dict to file 
import json
import pickle

def save2file(dict):
    # save as json file
    a_file = open("data.json", "w")
    json.dump(dict, a_file)
    a_file.close()
    # save as pickle file
    a_file = open("data.pkl", "wb")
    pickle.dump(dict, a_file)
    a_file.close()

#save2file(dict)

file_name= 'data.pkl'
def read_pkl(file_name):
    a_file = open(file_name, "rb")
    output = pickle.load(a_file)
    print(output)

file_name= 'data.json'
def read_json(file_name):
    a_file = open(file_name, "r")
    output = a_file.read()
    print(output)

def get_key(dict, k):
    # using loop
    for j,i in enumerate(dict):
        if (j == k):
            print ('key',k,i)
            return i        
    

print('Last movie\n',dict[get_key(dict,0)])

print('\n5 last movies from dict')
for i,k in enumerate(dict.keys()):
    if i<5:
        print(i,k,dict[k]['url'])


print('\nMovies from search\n')
#search='2020'
search='night'
n = 0
for i,k in enumerate(dict.keys()):    
    if search in k.lower():
        print(i,k,dict[k]['url'])
        n+=1
print(n,' movies found')