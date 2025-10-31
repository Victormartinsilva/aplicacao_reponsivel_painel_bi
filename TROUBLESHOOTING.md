# 🔍 Troubleshooting - Por que o Power BI não troca para mobile?

## Possíveis Causas

### 1. **Layout Mobile não configurado no Power BI Desktop**
O Power BI só renderiza em mobile se você configurou um layout mobile no Power BI Desktop:
- Abra o relatório no Power BI Desktop
- Vá em **Exibir** → **Layout para dispositivos móveis**
- Configure os visuais para mobile
- Publique o relatório novamente

### 2. **Power BI detecta pelo tamanho REAL do iframe**
O Power BI pode estar verificando o tamanho real do iframe, não apenas o CSS. O Streamlit pode estar criando um container maior que envolve nosso componente.

### 3. **Cache do Power BI**
O Power BI pode estar usando cache e não detectar mudanças de tamanho dinamicamente.

### 4. **API JavaScript não está sendo usada**
Atualmente estamos apenas mudando o tamanho do iframe. Pode ser necessário usar a API JavaScript do Power BI para forçar o layout.

## Soluções a Tentar

### Solução 1: Verificar se o layout mobile existe
1. Acesse o relatório diretamente no Power BI
2. Redimensione a janela para < 768px
3. Se NÃO trocar para mobile → O layout mobile não está configurado no Power BI Desktop

### Solução 2: Usar API JavaScript do Power BI
Em vez de apenas mudar o tamanho, usar a API para forçar o layout:
```javascript
// Usar powerbi.embed() com config específica
powerbi.embed(iframeElement, config, {
    type: 'report',
    embedUrl: url,
    settings: {
        layoutType: models.LayoutType.MobilePortrait
    }
});
```

### Solução 3: Adicionar parâmetro na URL
Tentar adicionar parâmetro que force mobile:
```
&config={"settings":{"layoutType":"MobilePortrait"}}
```

### Solução 4: Verificar tamanho real do iframe
No console do navegador, verificar:
```javascript
document.getElementById('powerbi-iframe').offsetWidth
```
Se estiver > 767px, o Power BI não vai detectar como mobile.

