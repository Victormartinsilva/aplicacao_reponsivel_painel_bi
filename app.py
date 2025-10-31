# -*- coding: utf-8 -*-
"""
Aplicação Web com Streamlit para Incorporação de Painel Power BI.

Este script Python utiliza o framework Streamlit para criar uma aplicação web.
O objetivo é incorporar um painel do Power BI de forma responsiva para
visualização em dispositivos móveis e desktop, trocando automaticamente
entre diferentes URLs do Power BI baseado no tamanho da viewport.
"""

import streamlit as st

# URL de incorporação (embed) do painel do Power BI
# Usamos a MESMA URL para ambos - o Power BI detecta automaticamente o tamanho do iframe
# e renderiza em mobile quando a largura do iframe é <= 768px
POWER_BI_EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=a02c9e61-ca48-4fee-87fb-732616424882&autoAuth=true&ctid=04e74123-4ede-4a84-89ef-b7c6dfe29df8&actionBarEnabled=true"

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
        
        /* Força largura máxima do wrapper e iframe em mobile */
        @media (max-width: 768px) {
            .powerbi-embed-wrapper {
                max-width: 767px !important;
                width: 100% !important;
            }
            
            .powerbi-embed-wrapper iframe {
                max-width: 767px !important;
            }
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

            /* Adiciona uma mensagem para indicar que é a visualização mobile (padrão) */
            .device-indicator::before {
                content: "Visualização Mobile (Layout Inicial)";
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
            /* Adiciona uma mensagem para indicar que é a visualização desktop (ao dar zoom > 768px) */
            .device-indicator::before {
                content: "Visualização Desktop - Layout Web (Zoom > 768px)";
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
        
        /* Remove margens e paddings do componente Streamlit */
        iframe[data-testid="stIFrame"] {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Remove espaçamento do componente HTML do Streamlit */
        .stApp > div > div > div > div > div {
            margin-top: 0 !important;
        }
        
        /* Ajusta o espaçamento após o indicador */
        div[data-testid="stVerticalBlock"] {
            gap: 0 !important;
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
    
    # HTML completo com container, wrapper e div para embed do Power BI usando API JavaScript
    powerbi_html = f"""
    <!-- Carrega a biblioteca JavaScript do Power BI -->
    <script src="https://cdn.jsdelivr.net/npm/powerbi-client@2.21.1/dist/powerbi.min.js"></script>
    
    <div class="powerbi-container">
        <div class="powerbi-embed-wrapper">
            <div id="powerbi-embed-container" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0;"></div>
        </div>
    </div>
    
    <script>
        // URL do Power BI
        const powerBIUrl = "{POWER_BI_EMBED_URL}";
        // Extrai reportId da URL
        const reportIdMatch = powerBIUrl.match(/reportId=([^&]+)/);
        const reportId = reportIdMatch ? reportIdMatch[1] : null;
        const embedUrl = powerBIUrl.split('?')[0].replace('/reportEmbed', '/view') + '?' + powerBIUrl.split('?')[1];
        
        console.log('[Power BI] Report ID:', reportId);
        console.log('[Power BI] Embed URL:', embedUrl);
        
        // Função para obter largura da viewport (funciona mesmo em iframe)
        function getViewportWidth() {{
            // Tenta acessar window.parent se estiver em iframe
            try {{
                if (window.parent && window.parent !== window) {{
                    return window.parent.innerWidth || window.parent.document.documentElement.clientWidth || window.parent.document.body.clientWidth;
                }}
            }} catch(e) {{
                // Se não conseguir acessar parent (CORS), usa o window atual
            }}
            // Fallback para window atual
            return window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth || screen.width;
        }}
        
        // Função para verificar se deve usar versão mobile (baseado na largura da viewport)
        // INVERSO: Começa mobile, vira desktop quando > 768px
        function isMobileView() {{
            const width = getViewportWidth();
            // INVERTIDO: <= 768px = desktop (pois queremos começar mobile e trocar para web ao dar zoom)
            // Agora: > 768px = mobile, <= 768px = desktop (invertido)
            const isDesktop = width > 768;
            const isMobile = !isDesktop; // Invertido: mobile é o padrão, desktop quando > 768px
            console.log('[Power BI] Largura detectada:', width, 'px | É desktop?', isDesktop, '| Troca para web quando > 768px');
            return isMobile; // Retorna true quando queremos manter mobile (width <= 768px)
        }}
        
        // Variável global para armazenar o embed do Power BI
        let powerbiEmbed = null;
        
        // Função para criar/atualizar o embed do Power BI usando API JavaScript
        function updatePowerBIEmbed() {{
            const container = document.getElementById('powerbi-embed-container');
            if (!container) {{
                console.log('[Power BI] Container não encontrado! Aguardando...');
                setTimeout(updatePowerBIEmbed, 200);
                return;
            }}
            
            const isMobile = isMobileView();
            const viewportWidth = getViewportWidth();
            
            console.log('[Power BI] Estado atual:', {{
                largura: viewportWidth,
                isMobile: isMobile,
                containerWidth: container.offsetWidth
            }});
            
            // Verifica se a biblioteca Power BI está carregada
            if (typeof powerbi === 'undefined') {{
                console.log('[Power BI] Biblioteca Power BI ainda não carregou. Aguardando...');
                setTimeout(updatePowerBIEmbed, 500);
                return;
            }}
            
            // Verifica se reportId foi extraído
            if (!reportId) {{
                console.error('[Power BI] Não foi possível extrair reportId da URL!');
                return;
            }}
            
            // Determina o layoutType baseado no tamanho
            // INVERTIDO: isMobile = <= 768px (queremos mobile)
            // Quando > 768px, queremos desktop/web
            const layoutType = isMobile ? powerbi.models.LayoutType.MobilePortrait : powerbi.models.LayoutType.Master;
            
            const mobileWidth = 767;
            
            // Configura largura do container
            if (isMobile) {{
                container.style.width = mobileWidth + 'px';
                container.style.maxWidth = mobileWidth + 'px';
                container.style.minWidth = mobileWidth + 'px';
                
                // Força também o wrapper e container pai
                const wrapper = container.parentElement;
                const containerParent = wrapper ? wrapper.parentElement : null;
                
                if (wrapper) {{
                    wrapper.style.width = mobileWidth + 'px';
                    wrapper.style.maxWidth = mobileWidth + 'px';
                    wrapper.style.minWidth = mobileWidth + 'px';
                }}
                
                if (containerParent) {{
                    containerParent.style.width = mobileWidth + 'px';
                    containerParent.style.maxWidth = mobileWidth + 'px';
                }}
            }} else {{
                container.style.width = '100%';
                container.style.maxWidth = 'none';
                container.style.minWidth = 'none';
                
                const wrapper = container.parentElement;
                const containerParent = wrapper ? wrapper.parentElement : null;
                
                if (wrapper) {{
                    wrapper.style.width = '100%';
                    wrapper.style.maxWidth = 'none';
                    wrapper.style.minWidth = 'none';
                }}
                
                if (containerParent) {{
                    containerParent.style.width = '100%';
                    containerParent.style.maxWidth = 'none';
                }}
            }}
            
            console.log('[Power BI] Configurando layout:', isMobile ? 'MOBILE (MobilePortrait)' : 'DESKTOP (Master/Web)');
            
            // Se já existe um embed, remove antes de criar novo
            if (powerbiEmbed) {{
                try {{
                    powerbiEmbed.destroy();
                    console.log('[Power BI] Embed anterior destruído');
                }} catch(e) {{
                    console.log('[Power BI] Erro ao destruir embed anterior:', e);
                }}
                powerbiEmbed = null;
            }}
            
            // Limpa o container
            container.innerHTML = '';
            
            // Configuração do embed
            const embedConfig = {{
                type: 'report',
                id: reportId,
                embedUrl: embedUrl,
                accessToken: '', // Vazio pois estamos usando autoAuth na URL
                tokenType: powerbi.models.TokenType.Aad,
                settings: {{
                    layoutType: layoutType,
                    filterPaneEnabled: true,
                    navContentPaneEnabled: true,
                    actionBarEnabled: true
                }}
            }};
            
            console.log('[Power BI] Configuração do embed:', embedConfig);
            
            // Tenta criar o embed
            try {{
                powerbiEmbed = powerbi.embed(container, embedConfig);
                console.log('[Power BI] ✅ Embed criado com layout:', layoutType);
                
                // Aguarda o embed carregar
                powerbiEmbed.on('loaded', function() {{
                    console.log('[Power BI] ✅ Embed carregado com sucesso!');
                    console.log('[Power BI] Layout atual:', layoutType);
                }});
                
                powerbiEmbed.on('error', function(event) {{
                    console.error('[Power BI] ❌ Erro ao carregar embed:', event.detail);
                }});
            }} catch(e) {{
                console.error('[Power BI] ❌ Erro ao criar embed:', e);
                console.error('[Power BI] Tentando fallback com iframe simples...');
                
                // Fallback: usa iframe simples se a API falhar
                const iframe = document.createElement('iframe');
                iframe.id = 'powerbi-iframe-fallback';
                iframe.src = powerBIUrl;
                iframe.frameBorder = '0';
                iframe.allowFullScreen = true;
                iframe.style.cssText = 'width: 100%; height: 100%; border: none; position: absolute; top: 0; left: 0;';
                container.appendChild(iframe);
            }}
        }}
        
        // Executa quando o DOM estiver pronto
        function initPowerBI() {{
            console.log('[Power BI] Inicializando detecção mobile/desktop...');
            // Aguarda biblioteca Power BI carregar
            function waitForPowerBI() {{
                if (typeof powerbi === 'undefined') {{
                    console.log('[Power BI] Aguardando biblioteca Power BI carregar...');
                    setTimeout(waitForPowerBI, 200);
                    return;
                }}
                console.log('[Power BI] Biblioteca carregada! Criando embed...');
                // Aguarda um pouco mais para garantir
                setTimeout(function() {{
                    updatePowerBIEmbed();
                }}, 500);
            }}
            waitForPowerBI();
            
            // Tenta novamente após mais tempo
            setTimeout(function() {{
                updatePowerBIEmbed();
            }}, 2000);
        }}
        
        // Executa quando a página carrega
        if (document.readyState === 'loading') {{
            document.addEventListener('DOMContentLoaded', initPowerBI);
        }} else {{
            initPowerBI();
        }}
        
        // Atualiza quando a janela é redimensionada (inclui zoom)
        let resizeTimeout;
        window.addEventListener('resize', function() {{
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(function() {{
                console.log('[Power BI] Janela redimensionada, verificando...');
                updatePowerBIEmbed();
            }}, 300);
        }});
        
        // Atualiza quando a orientação do dispositivo muda
        window.addEventListener('orientationchange', function() {{
            console.log('[Power BI] Orientação mudou, verificando...');
            setTimeout(updatePowerBIEmbed, 500);
        }});
        
        // Monitora mudanças no tamanho usando ResizeObserver
        if (window.ResizeObserver) {{
            try {{
                const resizeObserver = new ResizeObserver(function(entries) {{
                    for (let entry of entries) {{
                        const width = entry.contentRect.width;
                        console.log('[Power BI] ResizeObserver detectou largura:', width);
                        updatePowerBIEmbed();
                    }}
                }});
                
                // Observa o container
                const container = document.querySelector('.powerbi-container');
                if (container) {{
                    resizeObserver.observe(container);
                    console.log('[Power BI] ResizeObserver configurado no container');
                }}
                
                // Também observa o body/document
                resizeObserver.observe(document.body);
            }} catch(e) {{
                console.log('[Power BI] ResizeObserver não disponível ou erro:', e);
            }}
        }}
        
        // Polling adicional como fallback (verifica a cada 2 segundos se o tamanho mudou)
        let lastWidth = getViewportWidth();
        let lastWasMobile = null;
        setInterval(function() {{
            const currentWidth = getViewportWidth();
            // INVERTIDO: mobile quando <= 768px (padrão), desktop quando > 768px
            const currentIsMobile = currentWidth <= 768;
            
            // Verifica se mudou significativamente (mais de 10px) OU se mudou de modo
            if (Math.abs(currentWidth - lastWidth) > 10 || (lastWasMobile !== null && lastWasMobile !== currentIsMobile)) {{
                if (lastWasMobile !== null && lastWasMobile !== currentIsMobile) {{
                    console.log('[Power BI] Polling detectou mudança de modo:', lastWasMobile ? 'MOBILE (<=768px - padrão)' : 'DESKTOP (>768px - zoom)', '→', currentIsMobile ? 'MOBILE (<=768px - padrão)' : 'DESKTOP (>768px - zoom)');
                }} else {{
                    console.log('[Power BI] Polling detectou mudança de largura:', lastWidth, '→', currentWidth);
                }}
                lastWidth = currentWidth;
                lastWasMobile = currentIsMobile;
                updatePowerBIEmbed();
            }}
        }}, 2000);
        
        console.log('[Power BI] Script de detecção mobile/desktop carregado!');
    </script>
    """
    
    # Incorpora o HTML completo usando st.components.v1.html()
    # A altura será controlada pelo CSS padding-bottom do wrapper
    st.components.v1.html(powerbi_html, height=650, scrolling=False)
    
    # Nota informativa e ajuda com autenticação
    with st.expander("ℹ️ Sobre esta aplicação"):
        st.markdown("""
        **Nota didática:**
        - A responsividade é alcançada através de JavaScript que monitora o tamanho da viewport.
        - O sistema detecta automaticamente quando a largura da tela é <= 768px (incluindo zoom).
        - Quando detecta visualização mobile, troca automaticamente para a URL do Power BI mobile.
        - Funciona tanto em dispositivos reais quanto ao dar zoom na página.
        - As '@media queries' CSS ajustam o layout e exibem o indicador de dispositivo.
        
        **⚠️ Problemas de Autenticação - SOLUÇÃO:**
        
        **Passo 1 - Permitir Cookies de Terceiros:**
        - No Chrome: Configurações → Privacidade e segurança → Cookies → Permitir cookies de terceiros
        - No Edge: Configurações → Cookies e permissões de site → Permitir cookies de terceiros
        - No Firefox: Configurações → Privacidade → Não rastrear → Desativar (temporariamente para testar)
        
        **Passo 2 - Autenticar no Power BI:**
        1. Abra uma nova aba no mesmo navegador
        2. Acesse: https://app.powerbi.com
        3. Faça login na sua conta Microsoft/Office 365
        4. Verifique se consegue ver o relatório diretamente no Power BI
        5. Volte para esta aplicação e recarregue a página (F5)
        
        **Passo 3 - Testar URL Diretamente:**
        - Abra em nova aba: [URL Mobile](https://app.powerbi.com/reportEmbed?reportId=a02c9e61-ca48-4fee-87fb-732616424882&autoAuth=true&ctid=04e74123-4ede-4a84-89ef-b7c6dfe29df8&actionBarEnabled=true)
        - Se abrir diretamente mas não no iframe, o problema pode ser bloqueio de cookies de terceiros
        
        **Passo 4 - Verificar Console (F12):**
        - Pressione F12 → Console
        - Procure por erros relacionados a "cookie", "authentication" ou "CORS"
        - Compartilhe os erros se persistir
        """)


if __name__ == '__main__':
    main()
