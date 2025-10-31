# 📊 Aplicação Responsiva de Painel Power BI

Aplicação web desenvolvida com Streamlit para incorporação responsiva de painéis Power BI, otimizada para visualização em dispositivos móveis e desktop.

## 🎯 Objetivos

Esta aplicação foi desenvolvida com os seguintes objetivos:

1. **Incorporação Responsiva de Power BI**: Fornecer uma interface web que permite incorporar painéis do Power BI de forma responsiva, adaptando-se automaticamente a diferentes tamanhos de tela.

2. **Suporte Multi-dispositivo**: Garantir que o painel Power BI seja visualizado corretamente tanto em dispositivos móveis (smartphones, tablets) quanto em desktops, através de CSS responsivo e media queries.

3. **Indicador Visual de Dispositivo**: Exibir um indicador visual que identifica automaticamente se a visualização está otimizada para desktop ou mobile, facilitando o teste e validação da responsividade.

4. **Interface Limpa e Moderna**: Prover uma interface limpa e moderna, utilizando o framework Streamlit para uma experiência de usuário intuitiva.

5. **Facilidade de Deploy**: Permitir fácil deploy na plataforma Streamlit Cloud, facilitando o compartilhamento e acesso ao painel Power BI incorporado.

## 🚀 Como Testar o Projeto

### Pré-requisitos

- Python 3.7 ou superior instalado
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou baixe o projeto**:
   ```bash
   # Se estiver usando Git
   git clone <url-do-repositorio>
   cd powerbi_embed_app
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

   Isso instalará o Streamlit e suas dependências.

### Execução Local

1. **Inicie a aplicação Streamlit**:
   ```bash
   streamlit run app.py
   ```

2. **Acesse a aplicação**:
   - A aplicação será aberta automaticamente no navegador
   - URL padrão: `http://localhost:8501`

### Teste de Responsividade

#### Método 1: DevTools do Navegador (Recomendado para testes rápidos)

1. Abra a aplicação no navegador
2. Pressione `F12` ou `Ctrl+Shift+I` para abrir as Ferramentas de Desenvolvedor
3. Clique no ícone de dispositivo móvel ou pressione `Ctrl+Shift+M` para ativar o modo de dispositivo
4. Selecione um dispositivo móvel (ex: iPhone, Samsung Galaxy) ou defina uma largura customizada (ex: 375px, 768px)
5. Verifique:
   - O banner muda para "Visualização Mobile (Ajuste de Layout)"?
   - O layout do Power BI se ajusta corretamente?
   - Os controles e visualizações ficam legíveis?

#### Método 2: Teste em Dispositivo Real

1. **Encontre o IP da sua máquina**:
   ```bash
   # No Windows (PowerShell)
   ipconfig
   
   # Procure pelo endereço IPv4 (ex: 192.168.1.100)
   ```

2. **Acesse pelo dispositivo móvel**:
   - Certifique-se de que o dispositivo móvel está na mesma rede Wi-Fi
   - No navegador do dispositivo, acesse: `http://[SEU_IP]:8501`
   - Exemplo: `http://192.168.1.100:8501`

3. **Verifique a responsividade**:
   - O banner deve mostrar "Visualização Mobile"
   - O painel Power BI deve se ajustar ao tamanho da tela
   - A navegação deve ser intuitiva em touch

### Teste de Desktop

1. Abra a aplicação em uma janela de navegador com largura maior que 768px
2. Verifique:
   - O banner mostra "Visualização Desktop (Layout Otimizado)"
   - O painel Power BI ocupa o espaço disponível de forma otimizada
   - A visualização está clara e bem formatada

## 📁 Estrutura do Projeto

```
powerbi_embed_app/
│
├── app.py                 # Aplicação principal Streamlit
├── requirements.txt       # Dependências do projeto
├── README.md             # Este arquivo
├── .gitignore            # Arquivos ignorados pelo Git
└── templates/            # (Legado - não utilizado no Streamlit)
    └── index.html
```

## ⚙️ Configuração

### URL do Power BI

A URL de incorporação do Power BI está configurada no arquivo `app.py`:

```python
POWER_BI_EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=..."
```

Para usar um painel Power BI diferente, edite a variável `POWER_BI_EMBED_URL` no arquivo `app.py`.

### Parâmetros da URL Power BI

A URL atual inclui os parâmetros:
- `autoAuth=true`: Autenticação automática
- `ctid`: Tenant ID do Power BI

**Nota**: Em ambiente de produção, considere usar métodos de autenticação mais seguros, como:
- Power BI Embedded com Service Principal
- Master User authentication

## 🌐 Deploy no Streamlit Cloud

### Preparação

1. **Certifique-se de que o projeto está no Git**:
   ```bash
   git add .
   git commit -m "Preparação para deploy"
   git push origin main
   ```

2. **Crie um arquivo `.streamlit/config.toml`** (opcional):
   ```toml
   [server]
   headless = true
   port = 8501
   ```

### Deploy

1. Acesse [Streamlit Cloud](https://streamlit.io/cloud)
2. Conecte seu repositório GitHub/GitLab/Bitbucket
3. Selecione o repositório e branch
4. Configure o comando de execução: `streamlit run app.py`
5. Clique em "Deploy"

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework web para aplicações Python
- **Power BI Embedded**: Serviço de incorporação de relatórios Power BI
- **HTML/CSS**: Para estilização responsiva e media queries
- **Python 3**: Linguagem de programação

## 📝 Notas Importantes

- **Autenticação**: A URL atual usa autenticação automática (`autoAuth=true`). Em produção, implemente autenticação adequada.
- **Responsividade**: A responsividade é alcançada através de CSS media queries que detectam a largura da tela (breakpoint em 768px).
- **Performance**: O painel Power BI é carregado em um iframe, que pode ter algum tempo de carregamento inicial dependendo do tamanho do relatório.

## 🤝 Contribuindo

Sinta-se à vontade para fazer fork, criar issues e pull requests para melhorar este projeto.

## 📄 Licença

Este projeto é fornecido "como está" para fins educacionais e de demonstração.

---

**Desenvolvido para testar responsividade mobile de painéis Power BI**

