import streamlit as  st
import pandas as pd 
st.set_page_config(page_title="Web Scrapper",page_icon=':🇦🇺:')
st.markdown("""
<style>
.css-d1b1ld-edgvbvh6
            {
            visibility: hidden;
            }        
 </style>
""",unsafe_allow_html=True)
table1=pd.DataFrame({"Column1":[1,2,3,4,5,6],"Column2":[1,2,3,4,5,6]})
st.title("Bank Application")
st.header("Bank Of America")
st.subheader("This is appliaction for consumers")
st.text("I am a text function")
st.markdown("**Hello** World")
st.markdown("[google](https://www.tcs.com/)")
st.caption("I am caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json={"a":"1,2,3","b":"1,2,3"}
st.json(json)
code="""Print("Hello World)
def bank():
  pass a
  """
st.code(code)
st.write(json)
st.metric(label="wind speed",value="120ms",delta="-1.4ms")
st.table(table1)
st.dataframe(table1)
st.image("salar.jpg",caption="SALAR",width=680)
st.audio("file_example_MP3_700KB.mp3")
st.video("video.mp4")
def change():
    print(st.session_state.checker)
state=st.checkbox("check",value=True,on_change=change,key="checker")
# if state:
#     st.write("hello")
# else:
#     pass
rad_but=st.radio("In Which country do you live",options=("US","UK","INDIA","CANADA"))
print(rad_but)
def btn_click():
    print("button clicked")
btn=st.button("submit",on_click=btn_click)
select=st.selectbox("Please select your country",options=("US","UK"))
m=st.multiselect("Please select your country",options=("US","UK"))
print(m)
st.title("Upload Fiels")
st.markdown("---")
img=st.file_uploader("Please upload your image",type=["jpg","png"],accept_multiple_files=True)
if img is not None:
    st.image(img)
st.slider("This is a slider",min_value=0,max_value=1000)
name=st.text_input("Please enter your name",max_chars=100)
d=st.text_area("Description of the course")
st.date_input("Enter Your time")
st.write(f"name is {d}")
print(name)

import time as t
from datetime import time
def convert(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s
val=st.time_input("Enter Your time",value=time(0,0,0))
if str(val) == "00:00:00":
    st.write("Please set Timer")
else:
    sec=convert(str(val))
    bar=st.progress(0)
    per=sec/100
    for i in range(100):
        bar.progress((i+1))
        t.sleep(per)

st.markdown("<h1 style='text-align: center;'>User Registration</h1>",unsafe_allow_html=True)
form=st.form("Form1")
form.text_input("Please Enter Your Name")
form.form_submit_button("submit")
with st.form("Form2"):
    Fname,Sname=st.columns(2)
    col1=Fname.text_input("Please Enter Your First Name")
    col2=Sname.text_input("Please Enter Your Last Name")
    st.text_input("Enter Your Email ID")
    st.date_input("Enter you Date Of Birth")
    sub=st.form_submit_button("submit")
    if sub:
        if col1 == "" and col2 == "":
            st.warning("Please Enter Your Full Name")
        else:
            st.success("Submitted Successfully")
from matplotlib import pyplot as pt
import numpy as np 
x=np.linspace(0,5,100)
barx=np.array([1,2,3,4,5,6,7])
opt=st.sidebar.radio("Select My Graph",options=("Line","Bar","Hbar"))
if opt=="Line":
    fig=pt.figure()
    pt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    pt.plot(x,np.sin(x))
    pt.plot(x,np.cos(x),'--')
    st.write(fig)
elif opt=="Bar":
    fig=pt.figure()
    pt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    pt.bar(barx,barx*10)
    st.write(fig)
elif opt=="Hbar":
    fig=pt.figure()
    pt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    pt.barh(barx,barx*10)
    st.write(fig)

#https://unsplash.com/s/photos/{keyword}
#div:rip16=>figure=>img:YVj9w
#st.image("https://plus.unsplash.com/premium_photo-1676648196796-8dabd4e80d6d")
st.markdown("<h1 style='text-align: center;'>Web Scrapper</h1>",unsafe_allow_html=True)
from bs4 import BeautifulSoup
import requests
placeholder=st.empty()
with st.form("search"):
    keyword=st.text_input("Enter Your Keyword")
    search=st.form_submit_button("search")
    if search:
        page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup=BeautifulSoup(page.content, 'lxml')
        rows=soup.find_all("div", class_="ripi6")
        col1,col2=placeholder.columns(2)
        for row in rows:
            figures=row.find_all("figure")
            for i in range(2):
                img=figures[i].find("img", class_="GFY23")
                list=img["src"].split("?")
                if i==0:
                    col1.image(list[0])
                else:
                    col2.image(list[0])


      
#Image Editor
from PIL import Image
st.markdown("<h1 style='text-align: center;'> Image Editor</h1>",unsafe_allow_html=True)
st.markdown("---")
img=st.file_uploader("Upload Your Image",type=["jpg","png","jpeg"])
size=st.empty()
mode=st.empty()
format=st.empty()
if img:
    Image.open(img)
    size.markdown(f"<h6> The Size is {img.size} </h6>",unsafe_allow_html=True)
    format.markdown(f"<h6> The Format is {img.size} </h6>",unsafe_allow_html=True)
    st.image(img)
    