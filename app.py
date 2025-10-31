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
# Adiciona parâmetros para forçar layout mobile: config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCJ9
POWER_BI_EMBED_URL_MOBILE = "https://app.powerbi.com/reportEmbed?reportId=a02c9e61-ca48-4fee-87fb-732616424882&autoAuth=true&ctid=04e74123-4ede-4a84-89ef-b7c6dfe29df8&actionBarEnabled=true&filterPaneEnabled=true&navContentPaneEnabled=true"

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
    
    # HTML completo com container, wrapper e iframe - tudo em um componente para posicionamento correto
    powerbi_html = f"""
    <div class="powerbi-container">
        <div class="powerbi-embed-wrapper">
            <iframe 
                id="powerbi-iframe" 
                title="acompanhamento_servicos_seinfra"
                width="100%" 
                height="100%" 
                src="{POWER_BI_EMBED_URL_DESKTOP}"
                frameborder="0" 
                allowFullScreen="true"
                allow="fullscreen; clipboard-read; clipboard-write; autoplay; camera; microphone; payment"
                style="position: absolute; top: 0; left: 0; border: none;"
            ></iframe>
        </div>
    </div>
    
    <script>
        // URLs das versões Desktop e Mobile
        const desktopUrl = "{POWER_BI_EMBED_URL_DESKTOP}";
        const mobileUrl = "{POWER_BI_EMBED_URL_MOBILE}";
        
        // IDs dos reports para verificação
        const MOBILE_REPORT_ID = 'a02c9e61-ca48-4fee-87fb-732616424882';
        const DESKTOP_REPORT_ID = '461bfacf-024d-4a61-8149-7f8966c1ee3b';
        
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
        function isMobileView() {{
            const width = getViewportWidth();
            const isMobile = width <= 768;
            console.log('[Power BI] Largura detectada:', width, 'px | É mobile?', isMobile, '| Breakpoint: 768px');
            return isMobile;
        }}
        
        // Função para verificar qual URL está sendo usada atualmente
        function getCurrentUrlType(currentSrc) {{
            if (currentSrc.includes(MOBILE_REPORT_ID)) {{
                return 'MOBILE';
            }} else if (currentSrc.includes(DESKTOP_REPORT_ID)) {{
                return 'DESKTOP';
            }}
            return 'UNKNOWN';
        }}
        
        // Função para atualizar o iframe baseado no tamanho da viewport
        function updatePowerBIUrl() {{
            const iframe = document.getElementById('powerbi-iframe');
            if (!iframe) {{
                console.log('[Power BI] Iframe não encontrado! Aguardando...');
                // Tenta novamente após 200ms
                setTimeout(updatePowerBIUrl, 200);
                return;
            }}
            
            const isMobile = isMobileView();
            const targetUrl = isMobile ? mobileUrl : desktopUrl;
            const currentSrc = iframe.src || '';
            const currentUrlType = getCurrentUrlType(currentSrc);
            
            // Verifica se precisa atualizar (verifica o reportId na URL)
            const hasMobileReport = currentSrc.includes(MOBILE_REPORT_ID);
            const hasDesktopReport = currentSrc.includes(DESKTOP_REPORT_ID);
            const shouldUpdate = isMobile ? !hasMobileReport : !hasDesktopReport;
            
            console.log('[Power BI] Estado atual:', {{
                largura: getViewportWidth(),
                isMobile: isMobile,
                urlAtual: currentUrlType,
                urlAlvo: isMobile ? 'MOBILE' : 'DESKTOP',
                deveAtualizar: shouldUpdate,
                srcAtual: currentSrc.substring(0, 100) + '...'
            }});
            
            // Atualiza o src do iframe se necessário
            if (shouldUpdate) {{
                console.log('[Power BI] ⚠️ Atualizando URL do Power BI para:', isMobile ? 'MOBILE' : 'DESKTOP');
                console.log('[Power BI] Nova URL:', targetUrl.substring(0, 100) + '...');
                
                // Força reload completo do iframe para garantir que o Power BI renderiza em mobile
                // Remove o iframe do DOM temporariamente e recria
                const iframeParent = iframe.parentNode;
                const iframeId = iframe.id;
                const iframeTitle = iframe.title;
                const iframeStyle = iframe.getAttribute('style');
                const iframeAllow = iframe.getAttribute('allow');
                
                // Remove o iframe atual
                iframe.remove();
                
                // Cria novo iframe com a URL correta
                setTimeout(function() {{
                    const newIframe = document.createElement('iframe');
                    newIframe.id = iframeId;
                    newIframe.title = iframeTitle;
                    
                    // IMPORTANTE: Define largura absoluta em pixels para mobile
                    // O Power BI detecta o tamanho do iframe para decidir se renderiza em mobile
                    const viewportWidth = getViewportWidth();
                    if (isMobile) {{
                        // Força largura pequena para mobile (em pixels)
                        newIframe.width = Math.min(viewportWidth, 768) + 'px';
                        console.log('[Power BI] Iframe mobile configurado com largura:', newIframe.width);
                    }} else {{
                        newIframe.width = '100%';
                    }}
                    
                    newIframe.height = '100%';
                    newIframe.src = targetUrl;
                    newIframe.frameBorder = '0';
                    newIframe.allowFullScreen = true;
                    newIframe.setAttribute('allow', iframeAllow || 'fullscreen; clipboard-read; clipboard-write; autoplay; camera; microphone; payment');
                    
                    // Define estilo com largura absoluta para mobile
                    if (isMobile) {{
                        newIframe.setAttribute('style', 'position: absolute; top: 0; left: 0; border: none; width: ' + Math.min(viewportWidth, 768) + 'px; max-width: 768px;');
                    }} else {{
                        newIframe.setAttribute('style', iframeStyle || 'position: absolute; top: 0; left: 0; border: none;');
                    }}
                    
                    // Adiciona atributo data-mobile para forçar detecção
                    if (isMobile) {{
                        newIframe.setAttribute('data-mobile', 'true');
                    }}
                    
                    // Adiciona o novo iframe de volta ao DOM
                    iframeParent.appendChild(newIframe);
                    
                    console.log('[Power BI] ✅ Iframe recriado com URL', isMobile ? 'MOBILE' : 'DESKTOP');
                    console.log('[Power BI] Largura do iframe:', newIframe.width);
                    console.log('[Power BI] Nova URL completa:', targetUrl);
                    
                    // Força redimensionamento após carregar para garantir que o Power BI detecte
                    newIframe.onload = function() {{
                        console.log('[Power BI] Iframe carregado. Largura atual:', newIframe.offsetWidth);
                        // Dispara um evento de resize para o Power BI detectar
                        if (isMobile && newIframe.contentWindow) {{
                            try {{
                                newIframe.contentWindow.dispatchEvent(new Event('resize'));
                            }} catch(e) {{
                                console.log('[Power BI] Não foi possível disparar resize no iframe:', e);
                            }}
                        }}
                    }};
                }}, 100);
            }} else {{
                console.log('[Power BI] ✓ URL já está correta:', currentUrlType);
            }}
        }}
        
        // Executa quando o DOM estiver pronto
        function initPowerBI() {{
            console.log('[Power BI] Inicializando detecção mobile/desktop...');
            // Aguarda um pouco para garantir que o iframe foi renderizado
            setTimeout(function() {{
                updatePowerBIUrl();
            }}, 200);
            
            // Tenta novamente após mais tempo (caso o iframe demore mais)
            setTimeout(function() {{
                updatePowerBIUrl();
            }}, 1000);
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
                updatePowerBIUrl();
            }}, 200);
        }});
        
        // Atualiza quando a orientação do dispositivo muda
        window.addEventListener('orientationchange', function() {{
            console.log('[Power BI] Orientação mudou, verificando...');
            setTimeout(updatePowerBIUrl, 300);
        }});
        
        // Monitora mudanças no tamanho usando ResizeObserver
        if (window.ResizeObserver) {{
            try {{
                const resizeObserver = new ResizeObserver(function(entries) {{
                    for (let entry of entries) {{
                        const width = entry.contentRect.width;
                        console.log('[Power BI] ResizeObserver detectou largura:', width);
                        updatePowerBIUrl();
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
            const currentIsMobile = currentWidth <= 768;
            
            // Verifica se mudou significativamente (mais de 10px) OU se mudou de mobile/desktop
            if (Math.abs(currentWidth - lastWidth) > 10 || (lastWasMobile !== null && lastWasMobile !== currentIsMobile)) {{
                if (lastWasMobile !== null && lastWasMobile !== currentIsMobile) {{
                    console.log('[Power BI] Polling detectou mudança de modo:', lastWasMobile ? 'MOBILE' : 'DESKTOP', '→', currentIsMobile ? 'MOBILE' : 'DESKTOP');
                }} else {{
                    console.log('[Power BI] Polling detectou mudança de largura:', lastWidth, '→', currentWidth);
                }}
                lastWidth = currentWidth;
                lastWasMobile = currentIsMobile;
                updatePowerBIUrl();
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
