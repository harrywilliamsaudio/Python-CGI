import os.path
import re
import urllib.request


#cleaning text from html tags
def cleanhtml(raw_html):
  TAG_RE = re.compile(r'<[^>]+>')
  return TAG_RE.sub('', raw_html)


# check whether the provided URL is valid or not
def check_url(url):

    #check for local path
    if os.path.isfile(url):
        return True

    #otherwise, check for globle path
    urllib.request.urlopen(url)
    request = urllib.request.Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        print('########' + url)
        response = urllib.request.urlopen(request)
        return True
    except:
        return False

#download online resource whose url is provided
def download(t_url):
    response = urllib.request.urlopen(t_url)
    data = response.read()
    data = data.decode("utf-8", "ignore")
    txt_str = str(data)
    lines = txt_str.split("\\n")
    des_url = 'input/temp/abc.txt'
    fx = open(des_url,"w")
    for line in lines:
        fx.write(line+ "\n")
    fx.close()

#reading file to get text data
def get_file_data(fname):

    #check if the Url was globle then change file name downloaded earlier
    if fname.find('http') >= 0:
        download(fname)
        fname = 'input/temp/abc.txt'
        
    huge_list = ''
    with open(fname) as f:
        huge_list = f.read()

    return analyse_text(huge_list)

#analyse text accroding to provided rules
def analyse_text(text):
    new_text = ''
    text = cleanhtml(text)

    #removing checkers other than ASCII-letter, ASCII-digit, apostrophy, hyphen and uderscore
    for line in text:
        for char in line:
            if (not char.isalpha()) and (not char.isdigit()) and (not char == "'") and (not char == '_') and (not char == '-'):
                line = line.replace(char, ' ')
        new_text = new_text + line

    new_text = new_text.split()

    #reving words which do not end with [s']
    for item in new_text[:]:
      if len(item) > 1:
        if (not item[len(item)-1].isdigit()) and (not item[len(item)-1].isalpha()):
            if item[len(item)-1] == "'" and (not item[len(item)-2] == 's'):
              new_text.remove(item)
                

    #remving words whose last character is neither letter not digit      
    for item in new_text[:]:
      if len(item)>0:
        if (not item[len(item)-1].isalpha()) and (not item[len(item)-1].isdigit()) and  (not item[len(item)-1] == "'"):
          new_text.remove(item)

    
    for item in new_text[:]:
      if len(item) > 0:
        if (not item[0].isalpha()) and (not item[0] == "'"):
          new_text.remove(item)

    #check for words ending with [s']
    for item in new_text[:]:
      if len(item) >= 2:
        if ((item[0] == "'") and (not item[1].isalpha())):
          new_text.remove(item)

    #splitting words which are joined by delimitter '--' and '---'
    for item in new_text[:]:
      flag = False
      new_items = []
      if item.find('---') >= 0:
        new_items = item.split('---')
        new_text.remove(item)
        flag = True
      elif item.find('--') >= 0:
        new_items = item.split('--')
        new_text.remove(item)
        flag = True
      else:
        flag = False
      if flag == True:      
        for iitem in new_items:
          new_text.append(iitem)

        
    return new_text

def parse_into_dict(list):
    dictionary = dict()
    dictionary2 = dict()
    for i in list:
      if i in dictionary:
        dictionary[i]+=1
      else:
        dictionary[i] = 1
        

    count = 0
    for k, v in dictionary.items():
        count = count + v

    #print(counts)

    mdict = dict()
  
    for key, value in sorted(dictionary.items(), key = lambda t: t[1], reverse=True):
      mdict[key] = value
    
    for key, value in sorted(dictionary.items(), key = lambda t: t[1], reverse=False):
      dictionary2[key] = value


    return mdict, dictionary2, count
    



