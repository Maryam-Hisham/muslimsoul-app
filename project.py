import streamlit as st
import verse
import get_surah

def main():
    st.title("muslimsoul")

    tab1, tab2 = st.tabs(["How's your day?", "Listen to the Quran"])

    with tab1:
        st.header("How's your Day?")
        st.divider()
        emotion = emotions()
        st.divider()

        # the verse
        theverse = verseforemotion(emotion)
        st.write(theverse)
        st.divider()

        # the dua
        st.markdown("***Here's a Dua you can recite***")
        thedua = dua(emotion)
        st.write(thedua)

    with tab2:
        st.header("Listen to the Quran")
        get_audio()


def emotions():
    emotion = st.selectbox("How are you feeling?", ("Happy", "Distressed",
                           "Sad", "Lost", "Grateful", "Hopeful", "Fearful"), index=None)
    return emotion


def verseforemotion(emotion):

    comfort, hope, reassure = verse.verse()

    st.markdown("***Here's a verse from the Quran***")
    if emotion == None:
        return (f"Say how you are feeling to get a verse 💗")
    elif emotion in ["Happy", "Grateful", "Hopeful"]:
        return (hope)
    elif emotion in ["Distressed", "Sad"]:
        return (comfort)
    elif emotion in ["Lost", "Fearful"]:
        return (reassure)


def dua(emotion):

    if emotion == None:
        return (f"Say how you are feeling to get a dua to recite 💗")

    elif emotion in ["Happy", "Grateful", "Hopeful"]:
        return (f"Say 'Alhamdulillah'💗")

    elif emotion in ["Distressed", "Sad"]:
        return (f"\nلَا إِلَهَ إِلَّا اللَّهُ الْعَظِيمُ الْحَلِيمُ لَا إِلَهَ إِلَّا اللَّهُ رَبُّ الْعَرْشِ الْعَظِيمِ لَا إِلَهَ إِلَّا اللَّهُ رَبُّ السَّمَوَاتِ وَرَبُّ الْأَرْضِ وَرَبُّ الْعَرْشِ الْكَرِيمِ      \ntranslation: “There is no deity but Allah, the Knowing, the Clement. There is no deity but Allah, Lord of the Magnificent Throne. There is no deity but Allah, Lord of the heavens and Lord of the earth and Lord of the Noble Throne.” ")

    elif emotion in ["Lost", "Fearful"]:
        return (f" اللَّهُمَّ رَحْمَتَكَ أَرْجُو فَلَا تَكِلْنِي إِلَى نَفْسِي طَرْفَةَ عَيْنٍ وَأَصْلِحْ لِي شَأْنِي كُلَّهُ لَا إِلَهَ إِلَا أَنْتَ   \ntranslation: “O Allah, I hope for Your mercy. Do not leave me to myself even for a blink of an eye. Correct all of my affairs for me. There is none worthy of worship except You.”")

    elif emotion == None:
        return (f"Say how you are feeling to get a dua to recite 💗")


def url(number):
    url = "https://cdn.islamic.network/quran/audio-surah/128/ar.alafasy/" + number + ".mp3"
    return url

def surahs():
    names, numbers, dict = get_surah.get_surah()
    surah = st.selectbox("Choose a Surah", names , index=None)
    return surah

def get_audio():
    names, numbers, dictionary = get_surah.get_surah()
    surah = surahs()

    if surah:
        number = dictionary[surah]
        the_number = str(number)
        the_url = url(the_number)

        st.audio(the_url)
    if surah == None:
        st.write("Choose a surah to listen")



if __name__ == "__main__":
    main()
