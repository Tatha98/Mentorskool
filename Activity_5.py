import requests
import json
import pandas as pd
import sys
address="http://gateway.marvel.com/v1/public/characters"

def dfmaker(apk, Hsh):
    if(len(apk)==0 or len(Hsh)==0):
        raise Exception("APIKEY or Hash not found")
    else:
        address="http://gateway.marvel.com/v1/public/characters"
        for p in range(0,1600,100):
            parameterstt={"apikey":apk,"hash":Hsh,"ts":"1","limit":"100", "offset":p}
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
def filter_character_opt(dfp,x,filter_condition):
    return dfp.query(x+filter_condition)

if __name__=="__main__":
    args=sys.argv[1:]
    print(dfmaker(*args)['character_name'].nunique())