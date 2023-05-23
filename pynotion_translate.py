import requests
import json
import langid
import re
import sys
from deep_translator import GoogleTranslator

def getBlockIdFromUrl(url):
    block_id= url[url.rfind("-")+1:]
    return block_id


def translate(url,token,ttarget):
    block_id    = getBlockIdFromUrl(url)
    url         =   "https://api.notion.com/v1/blocks/"+block_id
    url_child   =   url+"/children?page_size=1000"
    headers =   {
        "Authorization":"Bearer "+token,
        "Notion-Version":"2022-02-22"
        }

    headers_patch    =   {
        "Authorization":"Bearer "+token,
        "Content-Type":"application/json",
        "Notion-Version":"2022-06-28"
        }
    response        =   requests.get(url, headers=headers)
    data            =   response.json()
    if data['object']=="error":
        print("404")
    elif  data['object']=="block":
        title           =   data["child_page"]["title"]
        parent_id       =   data["id"]
        response        =   requests.get(url_child, headers=headers)
        data            =   response.json()
        for i in range(len(data["results"])):
            if  data["results"][i]["type"]=="paragraph":
                block=data["results"][i]["id"]
                try:
                    if data["results"][i]["paragraph"]['rich_text'][0]['annotations']['code'] == False :
                        try :
                            data["results"][i]["paragraph"]["rich_text"][0]["text"]["content"]= GoogleTranslator(source='auto', target=ttarget).translate(data["results"][i]["paragraph"]["rich_text"][0]["text"]["content"])
                        except :
                            pass
                        try :
                            data["results"][i]["paragraph"]["rich_text"][0]["plain_text"]=GoogleTranslator(source='auto', target=ttarget).translate(data["results"][i]["paragraph"]["rich_text"][0]["plain_text"])
                        except:
                            pass
                        patch_data={"paragraph":data["results"][i]["paragraph"]}
                        url_patch   =   "https://api.notion.com/v1/blocks/"+block
                        reponse = requests.patch(url_patch, data=json.dumps(patch_data), headers=headers_patch)
                        print(reponse.json())
                except:
                    pass
        print("Complete")


if __name__ == "__main__":
    url     =   sys.argv[1]
    token   =   sys.argv[2]
    ttarget =   sys.argv[3]
    translate(block_id,token,ttarget)
