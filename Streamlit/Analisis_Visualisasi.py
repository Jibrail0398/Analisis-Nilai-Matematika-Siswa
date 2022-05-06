from bleach import clean
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_cleansing import clean_data
import streamlit as st

def pie_chart():
    fig, ax = plt.subplots()
    ax.pie(clean_data.loc[:,'Ethnic'].value_counts().values, 
        labels = clean_data.loc[:,'Ethnic'].value_counts().index,
        autopct='%.2f%%',textprops={'fontsize': 16})
    fig.set_figheight(5)
    fig.set_figwidth(5)
    plt.title('Persentase Siswa Berdasarkan Etnis',fontsize=20)
    st.pyplot(fig)

def demo_bar_chart():
    ethnic_gender = pd.pivot_table(clean_data, index = 'Ethnic', 
                               columns = 'Gender', 
                               aggfunc = 'count', 
                               values = 'Score')
    plt.figure(figsize =(10,15))
    ax = ethnic_gender.plot(kind = 'bar')
    plt.title('Jumlah Siswa Berdasarkan Etnis',fontsize=15)
    plt.xlabel('Etnis',fontsize=15)
    plt.ylabel('Jumlah Siswa',fontsize=15)
    plt.legend(bbox_to_anchor=(1,1),loc='upper left')
    for container in ax.containers:
        ax.bar_label(container,size=11)
    st.pyplot()
def score_ethnic():
    plt.figure(figsize=(10,5))
    ax = sns.barplot(x = 'Ethnic', y = 'Score' , 
                    hue = 'Gender',data = clean_data, 
                    ci = None, palette = 'hls')
    plt.ylabel('Nilai',fontsize=15)
    plt.xlabel('Etnis',fontsize=15)
    plt.title('Rata-Rata Nilai Berdasarkan Etnis',fontsize=20,color='red')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    for container in ax.containers:
        ax.bar_label(container)
    st.pyplot()
def score_Learning_Method():
    plt.figure(figsize=(4,4))
    ax = sns.barplot(x = 'Learning Method', 
                    y = 'Score',
                    data= clean_data,
                    ci=None,
                    palette='mako')
    plt.title('Rata-Rata Nilai Berdasarkan Metode Belajar',
            fontsize=15,
            color='green')
    plt.ylabel('Nilai',fontsize=16)
    plt.xlabel('Metode Belajar',fontsize=16)
    ax.bar_label(ax.containers[0],size=12)
    st.pyplot()
def score_Learning_Method1():
    plt.figure(figsize=(8,6))
    ax = sns.barplot(x = 'Ethnic',
                    y = 'Score',
                    hue ='Learning Method',
                    data=clean_data,
                    ci=None,
                    palette='Blues')
    plt.title('Rata-Rata Nilai Berdasarkan Metode Belajar',
            fontsize=15,
            color='green')
    plt.ylabel('Nilai',fontsize=16)
    plt.xlabel('Etnis',fontsize=16)
    plt.legend(bbox_to_anchor=(1, 1), 
            loc='upper left',
            title='Metode Belajar',
            fontsize=12)
    for container in ax.containers:
        ax.bar_label(container,size=11)
    st.pyplot()
def score_by_teacher():
    plt.figure(figsize=(5,5))
    ax = sns.barplot(x='Teacher', y='Score', data=clean_data, palette='CMRmap_r',ci=None)
    plt.title('Rata-Rata Nilai Matematika berdasarkan Guru yang Mengajar',fontsize=14)
    plt.xlabel('Nama Guru',fontsize=12)
    plt.ylabel('Nilai',fontsize=12)
    ax.bar_label(ax.containers[0])
    st.pyplot()
def score_by_teacher1():
    teacher_score = pd.pivot_table(clean_data, index = 'Ethnic',
                               columns = 'Teacher', 
                               aggfunc = 'mean', 
                               values = 'Score')
    ax = teacher_score.round().plot(kind='barh')
    plt.title('Rata-Rata Nilai Matematika berdasarkan Guru yang Mengajar',fontsize=15)
    plt.xlabel('Nama Guru',fontsize=12)
    plt.ylabel('Nilai',fontsize=12)
    plt.legend(bbox_to_anchor=(1,1),loc='upper left')
    for container in ax.containers:
        ax.bar_label(container,size=11)
    st.pyplot()
def score_by_freeredu():
    plt.figure(figsize=(5,5))
    ax = sns.barplot(x='Freeredu', y='Score', data=clean_data, orient='v',palette='CMRmap_r',ci=None)
    plt.title('Rata-Rata Nilai Matematika\nBerdasarkan Freeredu',fontsize=18)
    plt.xlabel('Jenis Makan Siang',fontsize=15)
    plt.ylabel('Nilai',fontsize=15)
    ax.bar_label(ax.containers[0])
    st.pyplot()
