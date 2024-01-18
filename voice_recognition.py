import streamlit as st
from pydub import AudioSegment, silence
import speech_recognition as sr
recog=sr.Recognizer()
import os
#recog=sr.Recognizer()
st.set_page_config(page_title="Voice Transalation To Text",page_icon=':🇦🇺:')
final_result=""
final_result=""
st.markdown("<h1 style='text-align: center;'>Audio To Text Converter</h1>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)
audio=st.file_uploader("Upload Your Audio File", type=['mp3', 'wav'])
if audio:
    st.audio(audio)
    audio_segment=AudioSegment.from_file(audio)
    chunks=silence.split_on_silence(audio_segment,min_silence_len=500,silence_thresh=audio_segment.dBFS-20,keep_silence=100)
    for index,chunk in enumerate(chunks):
        chunk.export(str(index)+".wav",format="wav")
        print(chunk)
        with sr.AudioFile(str(index)+".wav") as source:
            recorded=recog.record(source)
            try:
                text=recog.recognize_google(recorded)
                final_result=final_result+" "+text
            except:
                print("Not Converted Audio")
    with st.form("Result"):
        result=st.text_area("",value=final_result)
        d_sbtn=st.form_submit_button("Download")
        env=os.environ
        loc=env.get('USERPROFILE')
        local_d=loc+"\Downloads\\transcript.txt"
        if d_sbtn:
            #with open("transcript.txt",'w') as file:
             with open(local_d,'w') as file:
                file.write(result)


