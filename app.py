# -*- coding: utf-8 -*-
"""
Aplicação Web com Streamlit para Incorporação de Painel Power BI.

Este script Python utiliza o framework Streamlit para criar uma aplicação web.
O objetivo é incorporar um painel do Power BI de forma responsiva para
visualização em dispositivos móveis e desktop.
"""

import streamlit as st

# URL de incorporação (embed) do painel do Power BI fornecida pelo usuário.
# É importante notar que esta URL já contém os parâmetros de autenticação
# (autoAuth=true e ctid), o que simplifica a incorporação, mas em um
# ambiente de produção real, seria necessário um método de autenticação
# mais seguro (como o Power BI Embedded com Service Principal ou Master User).
POWER_BI_EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=461bfacf-024d-4a61-8149-7f8966c1ee3b&autoAuth=true&ctid=04e74123-4ede-4a84-89ef-b7c6dfe29df8"

# Configuração da página Streamlit
st.set_page_config(
    page_title="Power BI Embed Responsivo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado para responsividade e indicador de dispositivo
st.markdown("""
    <style>
        /*
        * Estilos CSS para garantir a responsividade e o layout.
        * O objetivo é que o iframe do Power BI ocupe a maior parte da tela.
        */

        /* Remove margens padrão do Streamlit */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        /* Oculta elementos padrão do Streamlit para layout limpo */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Container para o wrapper do Power BI */
        .powerbi-container {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 10px;
        }

        .powerbi-embed-wrapper {
            /* Define a largura máxima para o wrapper */
            width: 100%;
            /* Define a altura máxima para o wrapper */
            max-height: 90vh;
            /* Adiciona um aspecto de proporção para o iframe.
            * O Power BI geralmente tem uma proporção de 16:9 ou 4:3.
            * Usaremos um truque de padding-bottom para manter a proporção.
            * 56.25% = 9/16 * 100 (para 16:9)
            * 75% = 3/4 * 100 (para 4:3)
            * Vamos usar 75% para um aspecto mais quadrado, comum em relatórios.
            */
            padding-bottom: 75%; /* Proporção 4:3 */
            position: relative;
            /* Adiciona uma sombra para destacar o painel */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            /* Garante que o wrapper não ultrapasse a largura da tela */
            max-width: 1200px;
        }

        .powerbi-embed-wrapper iframe {
            /* O iframe deve ocupar 100% do espaço do wrapper */
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            /* Remove a borda padrão do iframe */
            border: none;
        }

        /*
        * Media Query para dispositivos móveis (largura máxima de 768px).
        * Em dispositivos móveis, o painel deve ocupar a largura total
        * e ter uma altura mais flexível para melhor visualização.
        */
        @media (max-width: 768px) {
            .powerbi-container {
                padding: 5px;
            }

            .powerbi-embed-wrapper {
                /* Em mobile, mantém a proporção 4:3 */
                padding-bottom: 75%;
                /* Garante que ocupe a largura total da tela */
                width: 100%;
                max-width: none;
            }

            /* Adiciona uma mensagem para indicar que é a visualização mobile */
            .device-indicator::before {
                content: "Visualização Mobile (Ajuste de Layout)";
                display: block;
                text-align: center;
                padding: 10px;
                background-color: #ffeb3b; /* Amarelo claro */
                color: #333;
                font-weight: bold;
                margin-bottom: 10px;
                border-radius: 5px;
            }
        }

        /*
        * Media Query para dispositivos desktop (largura mínima de 769px).
        */
        @media (min-width: 769px) {
            /* Adiciona uma mensagem para indicar que é a visualização desktop */
            .device-indicator::before {
                content: "Visualização Desktop (Layout Otimizado)";
                display: block;
                text-align: center;
                padding: 10px;
                background-color: #4caf50; /* Verde */
                color: white;
                font-weight: bold;
                margin-bottom: 10px;
                border-radius: 5px;
            }
        }

        /* Estilo para o cabeçalho/indicador */
        .device-indicator {
            width: 100%;
            max-width: 1200px; /* Mesma largura máxima do wrapper */
            margin: 0 auto;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)


def main():
    """
    Função principal da aplicação Streamlit.
    """
    # Título da aplicação
    st.title("📊 Power BI Embed Responsivo")
    
    # Indicador de dispositivo (Desktop/Mobile) usando HTML
    st.markdown('<div class="device-indicator"></div>', unsafe_allow_html=True)
    
    # Container para o Power BI
    st.markdown('<div class="powerbi-container">', unsafe_allow_html=True)
    st.markdown('<div class="powerbi-embed-wrapper">', unsafe_allow_html=True)
    
    # Incorporação do Power BI usando componentes do Streamlit
    st.components.v1.iframe(
        src=POWER_BI_EMBED_URL,
        height=600,
        scrolling=True
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Nota informativa
    with st.expander("ℹ️ Sobre esta aplicação"):
        st.markdown("""
        **Nota didática:**
        - A responsividade é alcançada principalmente pelo CSS.
        - O 'viewport' meta tag garante que a página se ajuste à largura do dispositivo.
        - As '@media queries' ajustam o layout e adicionam o indicador de dispositivo
          com base na largura da tela (<= 768px para mobile, > 768px para desktop).
        """)


if __name__ == '__main__':
    main()
