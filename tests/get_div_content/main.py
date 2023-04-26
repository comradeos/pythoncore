import requests
import time
import json


def translate_from_en_uk(message:str) -> str:
    url = "https://www2.deepl.com/jsonrpc"
    original_text = message
    
    request = requests.post(
        url,
        json = {
            "jsonrpc":"2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs":[{
                    "kind":"default",
                    "raw_en_sentence": original_text,
                    "raw_en_context_before":[],
                    "raw_en_context_after":[],
                    "preferred_num_beams":4,
                    "quality":"fast"
                }],
                "lang":{
                    "user_preferred_langs":["FR","EN"],
                    "source_lang_user_selected":"auto",
                    "target_lang":"FR"
                },
                "priority":-1,
                "commonJobParams":{},
                "timestamp": int(round(time.time() * 1000))
            },
            "id": 40890008
        }
    )

    content_str = request.content.decode()
    content_json = json.loads(content_str)
    
    if "error" in content_json:
        return "Too many requests"
    
    translated_text = content_json["result"]\
        ["translations"][0]["beams"][0]\
            ["postprocessed_sentence"]
    
    return translated_text


print("Чекаємо 5 секунд :)")
print(translate_from_en_uk("Let's assume you received the following student, JSON"))