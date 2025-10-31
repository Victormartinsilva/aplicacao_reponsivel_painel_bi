# -*- coding: utf-8 -*-
"""
Mini Aplicação Web com Flask para Incorporação de Painel Power BI.

Este script Python utiliza o framework Flask para criar um servidor web simples.
O objetivo é servir uma única página HTML que incorpora um painel do Power BI
e é responsiva para visualização em dispositivos móveis e desktop.
"""

from flask import Flask, render_template

# Inicializa a aplicação Flask
app = Flask(__name__)

# URL de incorporação (embed) do painel do Power BI fornecida pelo usuário.
# É importante notar que esta URL já contém os parâmetros de autenticação
# (autoAuth=true e ctid), o que simplifica a incorporação, mas em um
# ambiente de produção real, seria necessário um método de autenticação
# mais seguro (como o Power BI Embedded com Service Principal ou Master User).
POWER_BI_EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=461bfacf-024d-4a61-8149-7f8966c1ee3b&autoAuth=true&ctid=04e74123-4ede-4a84-89ef-b7c6dfe29df8"

@app.route('/')
def index():
    """
    Define a rota principal ('/') da aplicação.

    Esta função renderiza o template 'index.html', passando a URL de
    incorporação do Power BI para que o template possa exibi-lo.
    """
    # Renderiza o template 'index.html' e passa a variável
    # 'power_bi_url' com o valor da URL de embed.
    return render_template('index.html', power_bi_url=POWER_BI_EMBED_URL)

# Bloco de execução principal.
# Garante que o servidor web só inicie se o script for executado
# diretamente (e não importado como um módulo).
if __name__ == '__main__':
    # Inicia o servidor Flask.
    # debug=True é útil para desenvolvimento, pois reinicia o servidor
    # automaticamente ao detectar mudanças no código.
    # host='0.0.0.0' permite que o servidor seja acessível externamente
    # dentro do ambiente de sandbox.
    app.run(debug=True, host='0.0.0.0', port=5000)
