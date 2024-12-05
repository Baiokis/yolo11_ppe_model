from datetime import datetime
import requests
from requests.auth import HTTPDigestAuth

def obter_token():
    # Definindo o intervalo de tempo para exibição dos dados
    agora = datetime.now()
    hora_inicio = agora.replace(hour=0, minute=0, second=0).strftime('%Y-%m-%d %%20%H:%M:%S')
    hora_fim = agora.replace(hour=23, minute=59, second=59).strftime('%Y-%m-%d %%20%H:%M:%S')

    # URL base para obter o token
    url_token = (
        f"http://192.168.1.108/cgi-bin/videoStatServer.cgi?"
        f"action=startFind&channel=1&condition.StartTime={hora_inicio}&condition.EndTime={hora_fim}&condition.Granularity=Hour"
    )

    # Efetuando a requisição na API
    resposta = requests.get(url_token, auth=HTTPDigestAuth("admin", "autvix123456"), verify=False)

    # Converte o resultado JSON para texto UTF-8
    texto_resposta = resposta.content.decode('utf-8')
    token = None
    total_count = None

    # Filtragem para encontrar o token e o totalCount
    for linha in texto_resposta.split('\n'):
        if 'token=' in linha:
            token = linha.split('=')[1].strip()
        elif 'totalCount=' in linha:
            total_count = linha.split('=')[1].strip()

    # Retorna o token e o total_count
    return token, int(total_count)


def obter_dados(token, total_count):
    # URL base para obter os resultados
    url_dados = f"http://192.168.1.108/cgi-bin/videoStatServer.cgi?action=doFind&channel=1&token={token}&beginNumber=0&count={total_count}"

    # Efetua a requisição na API
    resposta = requests.get(url_dados, auth=HTTPDigestAuth("admin", "autvix123456"), verify=False)

    # Retorna os resultados
    return resposta.content.decode('utf-8')

if __name__ == "__main__":
    token, total_count = obter_token()
    print(f"Token: {token}, Total de Contagem: {total_count}")
    dados = obter_dados(token, total_count)
    print(dados)
