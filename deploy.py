#Import Libraries

import pandas as pd
import streamlit as st 
from pickle import load
import sklearn
from PIL import Image

#Title of web page
st.title("Welcome to Mushroom Prediction")

#Image on webpage
img = Image.open("msh.jpg")
st.image(img)

#Audio
audio_good  = open('good.mp3', 'rb')
audio_bad   = open('bad.mp3', 'rb)
audio_goodr = audio_good.read()
audio_badr  = audio_badr.read()                  

#Title for sidebar
st.sidebar.title('User Input Parameters')

values = {'t': 'True', 'f': 'False'}
ln     = {'n': 'Narrow', 'b': 'Broad'}
dk     = {'k': 'Black', 'n': 'Brown', 'g': 'Gray', 'p': 'Pink', 'w': 'White', 'h':'Chocolate' , 'u':'Purple' , 'e':'Red' , 'b': 'Buff', 'r':'Green' ,'y':'Yellow' ,'o':'Orange'} 
kn     = {'u':'Urban', 'g':'Grasses', 'm':'Meadows' ,'d':'Woods' ,'p':'Paths' ,'w':'Waste' ,'l':'Leaves'}
ak     = {'k': 'Black','n':'Brown', 'u':'Purple', 'h':'Chocolate', 'w':'White', 'r':'Green', 'o':'Orange', 'y':'Yellow', 'b':'Buff'}
rh     = {'s':'Scattered', 'n':'Numerous', 'a':'Abundant', 'v':'Several', 'y':'Solitary', 'c':'Clustered'}
sd     = {'n':'Brown', 'y':'Yellow', 'w':'White', 'g':'Gray', 'e':'Red', 'p':'Pink', 'b':'Buff', 'u':'Purple', 'c':'Cinnamon', 'r':'Green'}
pn     = {'e':'Equal', 'c':'Club', 'b':'Bulbous', 'r':'Rooted'}
ap     = {'p':'Pungent', 'a':'Almond', 'l':'Anice', 'n':'None', 'f':'Foul', 'c':'Creosote', 'y':'Fishy', 's':'Spicy', 'm':'Musty'}
aa     = {'s':'Smooth', 'f':'Fibrous', 'k':'Silky', 'y':'Scaly'}


#Input variables               
def user_input_features():
    
    br  = st.sidebar.selectbox("Bruises", options=values.keys(), format_func=(lambda x: '{}'.format(values.get(x)) ))
    gs  = st.sidebar.selectbox("Gill-Size",options=ln.keys(), format_func=(lambda x: '{}'.format(ln.get(x)) ))
    gc  = st.sidebar.selectbox("Gill-Colour",options=dk.keys(), format_func=(lambda x: '{}'.format(dk.get(x)) ))
    hb  = st.sidebar.selectbox("Habitat",options=kn.keys(), format_func=(lambda x: '{}'.format(kn.get(x)) ))
    spr = st.sidebar.selectbox('Spore-Print Colour', options=ak.keys(), format_func=(lambda x: '{}'.format(ak.get(x)) ))
    pop = st.sidebar.selectbox('Population',options=rh.keys(), format_func=(lambda x: '{}'.format(rh.get(x)) ))
    cc  = st.sidebar.selectbox('Cap Colour',options=sd.keys(), format_func=(lambda x: '{}'.format(sd.get(x)) ))
    sro = st.sidebar.selectbox('Stalk-Root',options=pn.keys(), format_func=(lambda x: '{}'.format(pn.get(x)) ))
    odr = st.sidebar.selectbox('Odour',options=ap.keys(), format_func=(lambda x: '{}'.format(ap.get(x)) ))  
    ssr = st.sidebar.selectbox('Stalk-surface-above-ring',options=aa.keys(), format_func=(lambda x: '{}'.format(aa.get(x)) ))
    
    
    new = {'bruises': br,
           'gill-size': gs, 
           'gill-color': gc, 
           'habitat': hb,
           'spore-print-color': spr, 
           'population': pop, 
           'cap-color': cc, 
           'stalk-root': sro,
           'odor': odr,
           'stalk-surface-above-ring': ssr}
           
    features = pd.DataFrame(new, index=[0])
    return features
                  
#Running the function
df = user_input_features()
st.write('You have chosen following inputs: ')
st.write(df)

#Loading the model
model = load(open('Mushroom_intelligence.pkl', 'rb'))


#Predicting the model

result = model.predict(df)

if st.button('Predict'):
    #st.balloons()
    st.header('Predicted Result:')
    if result[0]=="e":
        st.success("Mushroom is fit for consumption!!")
        good = Image.open("gdl.jpg")
        st.image(good)
        st.audio(audio_goodr, format='audio/mp3')
        
        
    else:
        st.error('Poisonous Mushroom!!', icon="🚨")
        bad  = Image.open("cross.jpg")
        st.image(bad)
        

if __name__=='__user_input_features__':
    user_input_features()
