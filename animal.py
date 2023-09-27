import pickle
import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv("Animal Dataset.csv")
similarity = pickle.load(open("similarity.pkl", "rb"))


def rec_animal(a):
    idx = df[df["Animal"] == a].index[0]
    distances = similarity[idx]
    animal_list = sorted(list(enumerate(distances)), reverse = True, key = lambda e : e[1])[1:]

    animal = []
    ht = []
    wt = []
    color = []
    lf = []
    diet = []
    habitat = []
    pred = []
    speed = []
    country = []
    conservation = []
    family = []
    period = []
    t_speed = []
    ss = []
    off = []
    for i in animal_list:
        animal.append(df.iloc[i[0]]["Animal"])
        ht.append(df.iloc[i[0]]["Height (cm)"])
        wt.append(df.iloc[i[0]]["Weight (kg)"])
        color.append(df.iloc[i[0]]["Color"])
        lf.append(df.iloc[i[0]]["Lifespan (years)"])
        diet.append(df.iloc[i[0]]["Diet"])
        habitat.append(df.iloc[i[0]]["Habitat"])
        pred.append(df.iloc[i[0]]["Predators"])
        speed.append(df.iloc[i[0]]["Average Speed (km/h)"])
        country.append(df.iloc[i[0]]["Countries Found"])
        conservation.append(df.iloc[i[0]]["Conservation Status"])
        family.append(df.iloc[i[0]]["Family"])
        period.append(df.iloc[i[0]]["Gestation Period (days)"])
        t_speed.append(df.iloc[i[0]]["Top Speed (km/h)"])
        ss.append(df.iloc[i[0]]["Social Structure"])
        off.append(df.iloc[i[0]]["Offspring per Birth"])

    return (animal[:20], ht[:20], wt[:20], color[:20], lf[:20], diet[:20], habitat[:20], pred[:20], speed[:20],
            country[:20], conservation[:20], family[:20], period[:20], t_speed[:20], ss[:20], off[:20])


st.title("Animal Similarity Model")

a = st.selectbox("Select Animal", ["None"] + sorted(df["Animal"].unique()))

if st.button("Show Similar Animals", use_container_width = True):
    r = rec_animal(a)
    st.table(pd.DataFrame({"Animal" : r[0], 'Height (cm)' : r[1], 'Weight (kg)' : r[2], 'Color' : r[3],
                           'Lifespan (years)' : r[4], 'Diet' : r[5], 'Habitat' : r[6], 'Predators' : r[7],
                           'Average Speed (km/h)' : r[8], 'Countries Found' : r[9], 'Conservation Status' : r[10],
                           'Family' : r[11], 'Gestation Period (days)' : r[12], 'Top Speed (km/h)' : r[13],
                           'Social Structure' : r[14], 'Offspring per Birth' : r[15]}, index = [i for i in range(1, 21)]))
