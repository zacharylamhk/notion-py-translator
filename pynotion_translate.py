import requests
import json
import langid
import re
import sys
from deep_translator import GoogleTranslator

def getBlockIdFromUrl(url):
    block_id= url[url.rfind("-")+1:]
    return block_id

def translate(url,token,t_target):
    translate_block(getBlockIdFromUrl(url),token,t_target)

def translate_block(block_id,token,t_target):
    url         =   "https://api.notion.com/v1/blocks/"+block_id
    url_child   =   url+"/children?page_size=100"
    headers =   {
        "Authorization":"Bearer "+token,
        "Notion-Version":"2022-02-22"
        }
    headers_patch    =   {
        "Authorization":"Bearer "+token,
        "Content-Type":"application/json",
        "Notion-Version":"2022-06-28"
        }
    response        =   requests.get(url_child, headers=headers)
    data            =   response.json()
    if data['object']=="error":
        print("404")
    elif data['object']=="list":
        #data=data['results']
        for i in range(len(data["results"])):
            block_type= data["results"][i]["type"]
            if  block_type=="paragraph" or block_type=="to_do" or block_type.find("heading")>-1 or  block_type=="bulleted_list_item" or block_type=="numbered_list_item" or block_type=="callout" or block_type=="quote" or block_type=="toggle":
                block=data["results"][i]["id"]
                print("working on block: "+ str(block))
                try:
                    if data["results"][i][block_type]['rich_text'][0]['annotations']['code'] == False :
                        try :
                            data["results"][i][block_type]["rich_text"][0]["text"]["content"]= GoogleTranslator(source='auto', target=t_target).translate(data["results"][i][block_type]["rich_text"][0]["text"]["content"])
                        except :
                            print("Except1")
                        try :
                            data["results"][i][block_type]["rich_text"][0]["plain_text"]=GoogleTranslator(source='auto', target=t_target).translate(data["results"][i][block_type]["rich_text"][0]["plain_text"])
                        except:
                            print("Except2")
                        patch_data={block_type:data["results"][i][block_type]}
                        url_patch   =   "https://api.notion.com/v1/blocks/"+block
                        reponse = requests.patch(url_patch, data=json.dumps(patch_data), headers=headers_patch)
                        if (reponse.json()['has_children']):
                            block_id=reponse.json()['id']
                            translate_block(block_id,token,t_target)

                except:
                    pass

def translate_text(text,language):
    return GoogleTranslator(source='auto', target=language).translate(text)


if __name__ == "__main__":
    url     =   sys.argv[3]
    token   =   sys.argv[1]
    ttarget =   sys.argv[2]
    translate_block(getBlockIdFromUrl(url),token,ttarget)

