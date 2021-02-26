# -*- coding: utf-8 -*-
import random
import json 
import uuid

age_and_genre=['a young _ girl','a young _ boy','a young _ woman','a young _ men','an adult _ woman','an adult _ men','an old _ woman','an old _ man']
clothing=['t-shirt','shirt','sweater','jacket','dress','long coat','swimsuit','sweatshirt','wedding dress','hoodie','uniform','long-sleeve top','coat','sheath dress']
clothing_color=['black','gray','red','brown','blue','purple','white','green','orange','yellow']
hair_color=['blonde','brown','black','red','blue','purple','white','green','gray']
skin_color=['white','brown','black']

questions=['what is the age of the person?','what is the skin color of the person?',
          'what is the gender of the person?', 'what is the color of the person\'s hair?',
          'what is the color of the person\'s clothes?']
answers=[]
paragraphs=[]

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

for i in range(10000):
    ag_index=random.randint(0, len(age_and_genre)-1)
    cl_index=random.randint(0, len(clothing)-1)
    cc_index=random.randint(0, len(clothing_color)-1)
    hc_index=random.randint(0, len(hair_color)-1)
    sc_index=random.randint(0, len(skin_color)-1)
        
    context=age_and_genre[ag_index].replace('_', skin_color[sc_index])+' with '+hair_color[hc_index]+' hair wearing a '+clothing_color[cc_index]+' '+clothing[cl_index]

    answers.append(context[find_nth(context," ",1)+1:find_nth(context," ",2)])
    answers.append(skin_color[sc_index])
    answers.append(context[find_nth(context," ",3)+1:find_nth(context," ",4)])
    answers.append(hair_color[hc_index])
    answers.append(clothing_color[cc_index])
    
    qas=[]
    for count, value in enumerate(questions):
        if count == 0:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",1)+1,"text":answers[count]}]})
        elif count == 2:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",3)+1,"text":answers[count]}]})
        elif count == 1:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",2)+1,"text":answers[count]}]})
        elif count == 3:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",5)+1,"text":answers[count]}]})
        else:
            qas.append({"question":value,"is_impossible":False,"id":str(uuid.uuid4()),"answers":[{"answer_start":find_nth(context," ",9)+1,"text":answers[count]}]})
        
    paragraphs.append({"context":context,"qas":qas})

dictionary = {  
    "version": "v2.0",
	"data" : [{"title": "People search", "paragraphs": paragraphs}]
    #"version": "1.1"
} 

with open("train-v2.0.json", "w") as outfile: 
	json.dump(dictionary, outfile) 