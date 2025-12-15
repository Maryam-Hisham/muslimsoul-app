import requests

def get_surah():
    surah = requests.get("https://mp3quran.net/api/v3/suwar?language=eng")

    dictionary = surah.json()
    surahs = dictionary["suwar"]
    chapter_list = []
    chapter_number_list = []
    combined_dict = {}
    for surah in surahs:
        chapter_list.append(surah["name"].strip())
    for surah in surahs:
        chapter_number_list.append(surah["id"])

    combined_dict = dict(zip(chapter_list, chapter_number_list))
    return(chapter_list, chapter_number_list, combined_dict)




