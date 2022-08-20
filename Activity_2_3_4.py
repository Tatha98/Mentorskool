import requests
import json
import pandas as pd

#Activity 2
## I haven't used namestartswith filter, instead I ran for loop over the whole json file to extract all the characters(1562)

sk= "8a3209d890b869300ba3b8541d6e3349"
address="http://gateway.marvel.com/v1/public/characters"
parameters={"apikey":"8a3209d890b869300ba3b8541d6e3349","hash":"75d95764bc6d8b35b9b53c47d35fbf4d","ts":"1", "limit":"100"}
response= requests.get(url=address, params=parameters)
re=response.json()

temp=[]
main_list=[]
for j in range(len(re['data']['results'])):
    character_name=re['data']['results'][j]['name']
    number_of_event_appearances=re['data']['results'][j]['events']['available']
    number_of_series_appearances=re['data']['results'][j]['series']['available']
    number_of_stories_appearances=re['data']['results'][j]['stories']['available']
    number_of_comics_appearances=re['data']['results'][j]['comics']['available']
    character_id=re['data']['results'][j]['id']
    temp=[character_name,number_of_event_appearances,number_of_series_appearances,number_of_stories_appearances,number_of_comics_appearances,character_id]
    main_list.append(temp)
df=pd.DataFrame(main_list, columns=['character_name','number_of_event_appearances','number_of_series_appearances','number_of_stories_appearances','number_of_comics_appearances','character_id'])

dfc=df.copy()
dfcc=df.copy()

for off in range(100,1600,100):
    parameterst={"apikey":"8a3209d890b869300ba3b8541d6e3349","hash":"75d95764bc6d8b35b9b53c47d35fbf4d","ts":"1", "limit":"100", "offset":off}
    responset= requests.get(url=address, params=parameterst)
    ret=responset.json()
    temp1=[]
    main_list1=[]
    for j in range(len(ret['data']['results'])):
        character_name=ret['data']['results'][j]['name']
        number_of_event_appearances=ret['data']['results'][j]['events']['available']
        number_of_series_appearances=ret['data']['results'][j]['series']['available']
        number_of_stories_appearances=ret['data']['results'][j]['stories']['available']
        number_of_comics_appearances=ret['data']['results'][j]['comics']['available']
        character_id=ret['data']['results'][j]['id']
        temp1=[character_name,number_of_event_appearances,number_of_series_appearances,number_of_stories_appearances,number_of_comics_appearances,character_id]
        main_list1.append(temp1)
    dft=pd.DataFrame(main_list1, columns=['character_name','number_of_event_appearances','number_of_series_appearances','number_of_stories_appearances','number_of_comics_appearances','character_id'])
    dfc=pd.concat([dfc,dft],join='outer')

print(dfc)

#Activity 3
def dfmaker(apk, Hsh):
    if(len(apk)==0 or len(Hsh)==0):
        raise Exception("APIKEY or Hash not found")
    else:
        address="http://gateway.marvel.com/v1/public/characters"
        for p in range(0,1600,100):
            parameterstt={"apikey":apk,"hash":Hsh,"ts":"1", "limit":"100", "offset":p}
            responsett= requests.get(url=address, params=parameterstt)
            rett=responsett.json()
            temp2=[]
            main_list2=[]
            for j in range(len(rett['data']['results'])):
                character_name=rett['data']['results'][j]['name']
                number_of_event_appearances=rett['data']['results'][j]['events']['available']
                number_of_series_appearances=rett['data']['results'][j]['series']['available']
                number_of_stories_appearances=rett['data']['results'][j]['stories']['available']
                number_of_comics_appearances=rett['data']['results'][j]['comics']['available']
                character_id=rett['data']['results'][j]['id']
                temp2=[character_name,number_of_event_appearances,number_of_series_appearances,number_of_stories_appearances,number_of_comics_appearances,character_id]
                main_list2.append(temp2)
                dftt=pd.DataFrame(main_list2, columns=['character_name','number_of_event_appearances','number_of_series_appearances','number_of_stories_appearances','number_of_comics_appearances','character_id'])
            if(p==0):
                dfccc=dftt
            else:
                dfccc=pd.concat([dftt,dfccc], join='outer')
        return dfccc
dfp=dfmaker("8a3209d890b869300ba3b8541d6e3349","75d95764bc6d8b35b9b53c47d35fbf4d")
print(dfp)

#Activity 4
#optimized function for filtering
def filter_character_opt(dfp,x,filter_condition):
    return dfp.query(x+filter_condition)
ans= filter_character_opt(dfp,'character_name','.str.startswith("C")')
print(ans)



