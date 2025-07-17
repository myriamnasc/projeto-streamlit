
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finanças", page_icon=":moneybag:")

st.markdown("""
    
    # Boas vindas!

    ## Nosso APP Financeiro!
            
    Espero que você curta a experiência da nossa solução para organização financeira.
    
""")

#widget de upload de dados
file_upload = st.file_uploader(label="Faça upload dos dados aqui", type=['csv'])
#verifica se algum arquivo foi feito o upload
if file_upload:

    #leitura dos dados
    df = pd.read_csv(file_upload)
    df['Data'] = pd.to_datetime(df['Data'],format="%d/%m/%Y").dt.date

    #exibição dos dados no app
    exp1 = st.expander("Dados Brutos")
    colums_fmt = {"Valor":st.column_config.NumberColumn("Valor",format="R$ %f")}
    exp1.dataframe(df, hide_index=True, column_config=colums_fmt)

    #Visão Instituição
    exp2 = st.expander("Instituições")
    df_instituicao = df.pivot_table(index="Data", columns="Instituição", values="Valor")

    #Abas para diferentes visualizações

    tab_data, tab_history, tab_share = exp2.tabs(["Dados","Histórico","Distribuição"])

    #Exibe Dataframe

    with tab_data: 
        st.dataframe(df_instituicao)

    #Exibe Histórico
    with tab_history:
        st.line_chart(df_instituicao)

    #Exibe distribuição
    
    with tab_share:

        #Filtro de data
        date = st.selectbox("Filtro Data",options=df_instituicao.index)

        #Gráfico de distribuição
        st.bar_chart(df_instituicao.loc[date])


