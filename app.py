# -*- coding: utf-8 -*-
"""
Aplicação Web com Streamlit para Incorporação de Painel Power BI.

Este script Python utiliza o framework Streamlit para criar uma aplicação web.
O objetivo é incorporar um painel do Power BI de forma responsiva para
visualização em dispositivos móveis e desktop, trocando automaticamente
entre diferentes URLs do Power BI baseado no tamanho da viewport.
"""

import streamlit as st

# URLs de incorporação (embed) do painel do Power BI
# URL para visualização Desktop
POWER_BI_EMBED_URL_DESKTOP = "https://app.powerbi.com/reportEmbed?reportId=461bfacf-024d-4a61-8149-7f8966c1ee3b&autoAuth=true&ctid=04e74123-4ede-4a84-89ef-b7c6dfe29df8"

# URL para visualização Mobile
POWER_BI_EMBED_URL_MOBILE = "https://app.powerbi.com/reportEmbed?reportId=a02c9e61-ca48-4fee-87fb-732616424882&autoAuth=true&ctid=04e74123-4ede-4a84-89ef-b7c6dfe29df8"

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
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        /* Oculta elementos padrão do Streamlit para layout limpo */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Reduz espaçamento do título */
        h1 {
            margin-bottom: 0.5rem !important;
            padding-bottom: 0 !important;
        }

        /* Container para o wrapper do Power BI */
        .powerbi-container {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 5px 10px;
            margin-top: 0;
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
                padding: 5px 10px;
                margin-top: 0;
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
                margin-bottom: 5px;
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
                margin-bottom: 5px;
                border-radius: 5px;
            }
        }

        /* Estilo para o cabeçalho/indicador */
        .device-indicator {
            width: 100%;
            max-width: 1200px; /* Mesma largura máxima do wrapper */
            margin: 0 auto;
            padding: 5px 10px;
            margin-bottom: 0;
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
    
    # HTML com JavaScript para detectar tamanho da viewport e trocar URL dinamicamente
    # Isso funciona mesmo com zoom, pois monitora o tamanho real da viewport
    powerbi_html = f"""
    <iframe 
        id="powerbi-iframe" 
        title="acompanhamento_servicos_seinfra"
        width="100%" 
        height="100%" 
        src="{POWER_BI_EMBED_URL_DESKTOP}"
        frameborder="0" 
        allowFullScreen="true"
        style="position: absolute; top: 0; left: 0; border: none;"
    ></iframe>
    
    <script>
        // Função para verificar se deve usar versão mobile (baseado na largura da viewport)
        function isMobileView() {{
            return window.innerWidth <= 768;
        }}
        
        // Função para atualizar o iframe baseado no tamanho da viewport
        function updatePowerBIUrl() {{
            const iframe = document.getElementById('powerbi-iframe');
            const isMobile = isMobileView();
            
            // URLs das versões Desktop e Mobile
            const desktopUrl = "{POWER_BI_EMBED_URL_DESKTOP}";
            const mobileUrl = "{POWER_BI_EMBED_URL_MOBILE}";
            
            // Define a URL baseado no tamanho da viewport
            const targetUrl = isMobile ? mobileUrl : desktopUrl;
            
            // Atualiza o src do iframe apenas se for diferente
            if (iframe.src !== targetUrl) {{
                iframe.src = targetUrl;
                console.log('Power BI URL atualizada para:', isMobile ? 'MOBILE' : 'DESKTOP');
            }}
        }}
        
        // Atualiza quando a página carrega
        updatePowerBIUrl();
        
        // Atualiza quando a janela é redimensionada (inclui zoom)
        let resizeTimeout;
        window.addEventListener('resize', function() {{
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(updatePowerBIUrl, 150);
        }});
        
        // Atualiza quando a orientação do dispositivo muda
        window.addEventListener('orientationchange', function() {{
            setTimeout(updatePowerBIUrl, 200);
        }});
    </script>
    """
    
    # Incorpora o HTML com JavaScript usando st.components.v1.html()
    st.components.v1.html(powerbi_html, height=600)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Nota informativa
    with st.expander("ℹ️ Sobre esta aplicação"):
        st.markdown("""
        **Nota didática:**
        - A responsividade é alcançada através de JavaScript que monitora o tamanho da viewport.
        - O sistema detecta automaticamente quando a largura da tela é <= 768px (incluindo zoom).
        - Quando detecta visualização mobile, troca automaticamente para a URL do Power BI mobile.
        - Funciona tanto em dispositivos reais quanto ao dar zoom na página.
        - As '@media queries' CSS ajustam o layout e exibem o indicador de dispositivo.
        """)


if __name__ == '__main__':
    main()
