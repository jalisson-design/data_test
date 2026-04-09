import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.lines import Line2D

st.set_page_config(layout="wide")

# df= pd.read_csv('dataset_brasileiro.csv')

# team = st.sidebar.selectbox("Times", df['home_team'].unique())

df_liv = pd.read_csv('dataset_liv_v2.csv', sep=',', decimal='.')
df_psg = pd.read_csv('dataset_psg_v2.csv', sep=',', decimal='.')

df_last5_psg = df_psg.tail(6)
df_last5_liv = df_liv.tail(6)

##
# Substituindo nomes muito longos por versões mais curtas
dicionario_nomes = {
    'Wolverhampton Wanderers FC': 'Wolves',
    'Brighton & Hove Albion FC': 'Brighton',
    'Tottenham Hotspur FC': 'Tottenham'
}

# Aplica a substituição na coluna 'adversario' (ou o nome que estiver no seu dataframe do Liverpool)
df_last5_liv['adversario'] = df_last5_liv['adversario'].replace(dicionario_nomes)
##

#configs
color_win = '#2ecc71'  # Verde vibrante
color_draw = '#f1c40f' # Amarelo/Ouro
color_loss = '#e74c3c' # Vermelho
color_gray = '#808080' 
bg_color = '#0e1117'


col1, col2 = st.columns(2)
col3,col4,col5 = st.columns(3)

##################col 1
#Config visual
fig = plt.figure(figsize=(12,5), facecolor=bg_color)
ax = plt.gca()
ax.set_facecolor(bg_color)
cores_b = [color_win if r == 2 else color_draw if r == 1 else color_loss for r in df_last5_psg['resultado']]
#cores_a = [color_win if r == 2 else color_draw if r == 1 else color_loss for r in df_last5_liv['resultado']]
#infos
plt.plot(np.arange(0, 5), df_last5_psg['resultado'].iloc[:-1],'--', color='#000080', label='PARIS SAINT-GERMAIN')
#plt.plot(np.arange(0, 5), df_last5_liv['resultado'],'--',color='#51aff7',label='Fora')
# Adicione [:-1] na variável cores_b para ela ficar com 5 elementos também
plt.scatter(np.arange(0, 5), df_last5_psg['resultado'].iloc[:-1], color=cores_b[:-1], zorder=3)
for i, (idx, row) in enumerate(df_last5_psg.iloc[:-1].iterrows()):
    placar = f"{row['score_home']} - {row['score_away']}"
    ax.annotate(placar, (i, row['resultado']), xytext=(0, 15), 
                textcoords='offset points', color='white', 
                ha='center', fontsize=9, fontweight='bold', alpha=0.9)
#plt.scatter(np.arange(0, 5), df_last5_liv['resultado'], color=cores_a, zorder=3)
plt.legend(
    facecolor='#2c2c2c',  # Cor de fundo do box
    #edgecolor='gold',     # Cor da borda do box
    labelcolor='white'    # Cor do texto da legenda
 )
#plt.xlabel('Jogos Disputados', color='white')
plt.yticks([0, 1, 2], ['DERROTA', 'EMPATE', 'VITÓRIA'], color='white')
plt.xticks(np.arange(0, 5), df_last5_psg['adversario'].iloc[:-1], color='white')
plt.title('ÚLTIMOS 5 JOGOS', color='white', fontsize=18, fontweight='bold', pad=30, loc='left')
#mudar a cor da box
ax = plt.gca() # Pega o eixo atual
for spine in ax.spines.values():
    spine.set_edgecolor('gray') # Muda a cor das 4 linhas da moldura

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
# ax.spines['left'].set_color('#444444')
ax.spines['bottom'].set_color('#444444')
ax.grid(axis='y', linestyle=':', alpha=0.2, color='white')

###### col 2 
# Ultimos 5 jogos: LIV
#Config visual
fig2 = plt.figure(figsize=(12,5), facecolor=bg_color)
ax = plt.gca()
ax.yaxis.tick_right()
ax.set_facecolor(bg_color)
cores_b = [color_win if r == 2 else color_draw if r == 1 else color_loss for r in df_last5_liv['resultado']]
#infos
# plt.plot(np.arange(0, 5), df_last5_psg['resultado'],'--', color='#800020', label='FC BARCELONA')
plt.plot(np.arange(0, 5), df_last5_liv['resultado'].iloc[:-1],'--',color='#8b0000',label='LIVERPOOL')
# plt.scatter(np.arange(0, 5), df_last5_psg['resultado'], color=cores_b, zorder=3)
plt.scatter(np.arange(0, 5), df_last5_liv['resultado'].iloc[:-1], color=cores_b[:-1], zorder=3)
for i, (idx, row) in enumerate(df_last5_liv.iloc[:-1].iterrows()):
    placar = f"{row['score_home']} - {row['score_away']}"
    ax.annotate(placar, (i, row['resultado']), xytext=(0, 15), 
                textcoords='offset points', color='white', 
                ha='center', fontsize=9, fontweight='bold', alpha=0.9)
#plt.xlabel('Jogos Disputados', color='white')
plt.yticks([0, 1, 2], ['DERROTA', 'EMPATE', 'VITÓRIA'], color='white')
plt.xticks(np.arange(0, 5), df_last5_liv['adversario'].iloc[:-1], color='white')
plt.title('ÚLTIMOS 5 JOGOS', color='white', fontsize=18, fontweight='bold', pad=30, loc='left')
#PADRÃO PARA TODOS
plt.legend(
    facecolor='#2c2c2c',  # Cor de fundo do box
    #edgecolor='gold',     # Cor da borda do box
    labelcolor='white'    # Cor do texto da legenda
)
#mudar a cor da box
ax = plt.gca() # Pega o eixo atual
for spine in ax.spines.values():
    spine.set_edgecolor('gray') # Muda a cor das 4 linhas da moldura

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
#ax.spines['left'].set_color('#444444')
ax.spines['bottom'].set_color('#444444')
ax.grid(axis='y', linestyle=':', alpha=0.2, color='white')

#################################################################################################################################################

# Ultimos 5 jogos (features)
fig3 = plt.figure(figsize=(12,5), facecolor=bg_color)
ax = plt.gca()
ax.set_facecolor(bg_color)
cores_rate = [
    color_gray if pd.isna(r) or pd.isna(v) else color_win if r == 1 else color_loss 
    for r, v in zip(df_last5_psg['over_2_5'], df_last5_psg['resultado'])
]
#infos
# plt.bar(np.arange(0, 5), df_last5_liv['over_2_5'], color='#005e7a', label='OVER 2,5 GOAL')
plt.plot(np.arange(0, 6), df_last5_psg['team_over_2_5_rate'], '--',color='#ff5f5f',label='TAXA RECENTE: OVER 2,5 GOAL')
plt.scatter(np.arange(0, 6), df_last5_psg['team_over_2_5_rate'], color=cores_rate, zorder=3)
plt.xticks(np.arange(0, 6), df_last5_psg['adversario'], color='white')
if min(df_last5_psg['team_over_2_5_rate']) > 0.5:
 bottom= 0.5
else:
 bottom = min(df_last5_psg['team_over_2_5_rate']-0.05)
plt.ylim(bottom, 1.05)
#plt.xlabel('Jogos Disputados', color='white')
# plt.ylabel('TAXA RECENTE DE OVER 2,5', color='white')
plt.yticks(color='white')
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
plt.title('OVER 2,5 RECENTES: PARIS SAINT-GERMAIN', color='white', fontsize=18, fontweight='bold', pad=30, loc='left')
#legenda manual
legend_elements = [
    Line2D([0], [0], color='#ff5f5f', lw=2, linestyle='--', label='TAXA RECENTE OVER 2.5'),
    Line2D([0], [0], marker='o', color='w', label='OVER 2,5', markerfacecolor=color_win, markersize=8),
    Line2D([0], [0], marker='o', color='w', label='UNDER 2,5', markerfacecolor=color_loss, markersize=8),
    Line2D([0], [0], marker='o', color='w', label='PROX', markerfacecolor=color_gray, markersize=8)
]
#PADRAO PARA TODOS
plt.legend(
    handles=legend_elements, #TIRAR EM OUTROS
    facecolor='#2c2c2c',  # Cor de fundo do box
    #edgecolor='gold',     # Cor da borda do box
    labelcolor='white'    # Cor do texto da legenda
)
#mudar a cor da box
ax = plt.gca() # Pega o eixo atual
for spine in ax.spines.values():
    spine.set_edgecolor('gray') # Muda a cor das 4 linhas da moldura

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
#ax.spines['left'].set_color('#444444')
ax.spines['bottom'].set_color('#444444')
ax.grid(axis='y', linestyle=':', alpha=0.2, color='white')

###############################################################################################################################

# Ultimos 5 jogos (features)
fig4 = plt.figure(figsize=(12,5), facecolor=bg_color)
ax = plt.gca()
ax.yaxis.tick_right()
ax.set_facecolor(bg_color)
cores_rate = [
    color_gray if pd.isna(r) or pd.isna(v) else color_win if r == 1 else color_loss 
    for r, v in zip(df_last5_liv['over_2_5'], df_last5_liv['resultado'])
]
#infos
# plt.bar(np.arange(0, 5), df_last5_liv['over_2_5'], color='#005e7a', label='OVER 2,5 GOAL')
plt.plot(np.arange(0, 6), df_last5_liv['team_over_2_5_rate'], '--',color='#ff5f5f',label='TAXA RECENTE: OVER 2,5 GOAL')
plt.scatter(np.arange(0, 6), df_last5_liv['team_over_2_5_rate'], color=cores_rate, zorder=3)
plt.xticks(np.arange(0, 6), df_last5_liv['adversario'], color='white')
if min(df_last5_liv['team_over_2_5_rate']) > 0.5:
 bottom= 0.5
else:
 bottom = min(df_last5_liv['team_over_2_5_rate']-0.05)
plt.ylim(bottom, 1.05)
#plt.xlabel('Jogos Disputados', color='white')
# plt.ylabel('TAXA RECENTE DE OVER 2,5', color='white')
plt.yticks(color='white')
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
plt.title('OVER 2,5 RECENTES: LIVERPOOL', color='white', fontsize=18, fontweight='bold', pad=30, loc='left')
#legenda manual
legend_elements = [
    Line2D([0], [0], color='#ff5f5f', lw=2, linestyle='--', label='TAXA RECENTE OVER 2.5'),
    Line2D([0], [0], marker='o', color='w', label='OVER 2,5', markerfacecolor=color_win, markersize=8),
    Line2D([0], [0], marker='o', color='w', label='UNDER 2,5', markerfacecolor=color_loss, markersize=8),
    Line2D([0], [0], marker='o', color='w', label='PROX', markerfacecolor=color_gray, markersize=8)
]
#PADRAO PARA TODOS
plt.legend(
    handles=legend_elements, #TIRAR EM OUTROS
    facecolor='#2c2c2c',  # Cor de fundo do box
    #edgecolor='gold',     # Cor da borda do box
    labelcolor='white'    # Cor do texto da legenda
)
#mudar a cor da box
ax = plt.gca() # Pega o eixo atual
for spine in ax.spines.values():
    spine.set_edgecolor('gray') # Muda a cor das 4 linhas da moldura

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
#ax.spines['left'].set_color('#444444')
ax.spines['bottom'].set_color('#444444')
ax.grid(axis='y', linestyle=':', alpha=0.2, color='white')


############################################################################################################

win_liv = df_liv[df_liv['resultado'] == 2].shape[0]
loss_liv = df_liv[df_liv['resultado'] == 0].shape[0]
draw_liv = df_liv[df_liv['resultado'] == 1].shape[0]

win_psg = df_psg[df_psg['resultado'] == 2].shape[0]
loss_psg = df_psg[df_psg['resultado'] == 0].shape[0]
draw_psg = df_psg[df_psg['resultado'] == 1].shape[0]

liv_matches = [win_liv, draw_liv, loss_liv]
psg_matches = [win_psg, draw_psg, loss_psg]

cores = [color_win, color_draw, color_loss]
label = ['DERROTA', 'EMPATE', 'VITÓRIA']

fig5, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(6, 3), facecolor=bg_color)
ax = plt.gca()
ax.set_facecolor(bg_color)
ax2.pie(liv_matches,colors=cores,autopct=lambda p: f'{int(round(p * (win_liv+draw_liv+loss_liv) / 100.0))}',textprops={'color': 'white', 'fontweight': 'bold'})
ax2.axis('equal')
ax2.set_title('LIVERPOOL', color='white', fontweight='bold')
ax1.pie(psg_matches,colors=cores,autopct=lambda p: f'{int(round(p * (win_psg+draw_psg+loss_psg) / 100.0))}',textprops={'color': 'white', 'fontweight': 'bold'})
ax1.axis('equal')
ax1.set_title('PARIS SAINT-GERMAIN', color='white', fontweight='bold')
fig5.legend(
    label,
    facecolor='#2c2c2c',  # Cor de fundo do box
    loc='lower center',
    labelcolor='white'    # Cor do texto da legenda
)




##### Configs colum

col1, col2 = st.columns([0.5, 0.5])
col3, col4, col5 = st.columns([0.34, 0.30, 0.34])

with col1:
    st.subheader("Análise: PSG")
    st.pyplot(fig)

with col2:
    st.subheader("Análise: Liverpool")
    st.pyplot(fig2)

st.write("")
col3.pyplot(fig3)
col5.pyplot(fig4)
col4.pyplot(fig5)