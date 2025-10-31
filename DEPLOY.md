# 🚀 Guia de Deploy no Streamlit Cloud

Este guia mostra como fazer o deploy desta aplicação no Streamlit Cloud e obter uma URL pública.

## 📋 Pré-requisitos

✅ **Concluído:**
- [x] Projeto no GitHub: `https://github.com/Victormartinsilva/aplicacao_reponsivel_painel_bi.git`
- [x] Arquivo `app.py` configurado
- [x] Arquivo `requirements.txt` com dependências
- [x] Arquivo `.streamlit/config.toml` criado
- [x] Todos os arquivos commitados e enviados para o GitHub

## 🌐 Passo a Passo - Deploy no Streamlit Cloud

### Passo 1: Acessar Streamlit Cloud

1. Acesse: **https://share.streamlit.io/**
2. Clique em **"Sign in"** ou **"Sign up"**
3. Faça login com sua conta GitHub (o mesmo usuário do repositório)

### Passo 2: Conectar Repositório

1. Na página inicial do Streamlit Cloud, clique em **"New app"**
2. Na seção **"Deploy an app"**, você verá uma lista dos seus repositórios GitHub
3. Se não aparecer, clique em **"Authorize Streamlit"** para dar permissão
4. Selecione o repositório: **`aplicacao_reponsivel_painel_bi`**
5. Selecione o branch: **`main`** (ou `master`)

### Passo 3: Configurar o Deploy

1. **Main file path:** Digite: `app.py`
   - Este é o arquivo principal da aplicação

2. **Advanced settings** (opcional):
   - **Python version:** Deixe o padrão (Python 3.11 ou superior)
   - **Secrets:** Deixe vazio por enquanto (não precisa para este projeto)

3. Clique em **"Deploy!"**

### Passo 4: Aguardar o Deploy

1. O Streamlit Cloud começará a fazer o deploy automaticamente
2. Você verá logs em tempo real do processo:
   - Instalando dependências
   - Executando `streamlit run app.py`
   - Iniciando o servidor
3. Isso pode levar 1-3 minutos na primeira vez

### Passo 5: Obter a URL

Após o deploy concluir, você terá:

✅ **URL da aplicação:** `https://[seu-app-name]-[hash].streamlit.app`

Exemplo:
```
https://aplicacao-reponsivel-painel-bi-xyz123.streamlit.app
```

**Importante:** A URL será exibida na interface do Streamlit Cloud e também será enviada por email.

## 📝 Atualizações Futuras

Para atualizar a aplicação após fazer mudanças:

1. **Faça as alterações no código local**
2. **Commit e push para o GitHub:**
   ```bash
   git add .
   git commit -m "Descrição das mudanças"
   git push origin main
   ```
3. **O Streamlit Cloud detecta automaticamente** e faz redeploy
4. **A URL permanece a mesma** - não muda após o primeiro deploy

## ⚙️ Configurações Adicionais

### Customizar a URL

1. No dashboard do Streamlit Cloud, clique no app
2. Clique nos **3 pontos** (menu) no canto superior direito
3. Selecione **"Settings"**
4. Em **"App URL"**, você pode escolher um nome customizado:
   - Exemplo: `powerbi-embed-responsivo`
   - URL final: `https://powerbi-embed-responsivo.streamlit.app`

### Gerenciar o App

- **Ver logs:** Clique em "Manage app" → "Logs"
- **Reiniciar:** "Manage app" → "Restart"
- **Deletar:** "Manage app" → "Settings" → "Delete app"

## 🔐 Configurações de Segurança

### Para URLs do Power BI (se necessário no futuro)

Se precisar usar variáveis de ambiente ou secrets:

1. No Streamlit Cloud, vá em **"Settings"** → **"Secrets"**
2. Adicione:
   ```toml
   [powerbi]
   embed_url_desktop = "https://app.powerbi.com/reportEmbed?..."
   embed_url_mobile = "https://app.powerbi.com/reportEmbed?..."
   ```
3. No código, use: `st.secrets["powerbi"]["embed_url_desktop"]`

## ✅ Checklist Final

Antes de fazer o deploy, verifique:

- [x] `app.py` está funcionando localmente (`streamlit run app.py`)
- [x] `requirements.txt` contém todas as dependências
- [x] Todos os arquivos foram commitados e enviados para GitHub
- [x] Não há erros de sintaxe no código
- [x] O repositório é público ou você tem acesso ao Streamlit Cloud (versão paga permite privados)

## 🐛 Solução de Problemas

### Erro: "Module not found"
- Verifique se todas as dependências estão em `requirements.txt`
- Execute `pip freeze > requirements.txt` localmente para garantir

### Erro: "App crashed"
- Verifique os logs no Streamlit Cloud (Manage app → Logs)
- Teste localmente primeiro para identificar o problema

### URL não funciona
- Verifique se o deploy foi concluído com sucesso
- Aguarde alguns minutos se acabou de fazer push
- Verifique se o branch está correto

## 📞 Suporte

- **Documentação Streamlit Cloud:** https://docs.streamlit.io/streamlit-community-cloud
- **Status do serviço:** https://status.streamlit.app
- **Comunidade:** https://discuss.streamlit.io

---

**Repositório GitHub:** https://github.com/Victormartinsilva/aplicacao_reponsivel_painel_bi

**Boa sorte com o deploy! 🚀**

