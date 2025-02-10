# Script - Download Vídeos do YouTube em MP4

Este é um script em Python que permite baixar vídeos na melhor qualidade do YouTube em formato MP4 diretamente no seu computador.

## Pré-requisitos
Para rodar este script, você precisará ter o Python 3 e a biblioteca yt-dlp instalados no seu sistema.

1. Instalando Py3:
   ```bash
   sudo apt update
   sudo apt install python3

2. Instalando a biblitoeca yt-dlp
   ```bash
   python -m install yt-dlp

3. Gerenciador de pacote (opcional)
   ```bash
   sudo apt update && sudo apt install python3-pip

## Utilizando o Script

### 1. Baixando o Script

Faça o download do script ou clone o repositório diretamente para a pasta do seu computador.
```bash
git clone https://github.com/seu-usuario/repo-yt-download-mp4.git
```


### 2. Inicializando o Script
Abra o terminal e navegue até a pasta onde você salvou o script. No meu caso:
```bash
cd /home/junio/Documents/VSCODE/projetos
```

Para rodar o script e baixar um vídeo do YouTube, basta executar o comando:
   ```bash
   python3 yt-download-mp4.py
   ```


## 3. Personalizando o Local de Download

O vídeo será baixado no formato MP4 para a pasta `Videos/videos-baixados-pelo-script/`.

Caso queira alterar o local onde os vídeos serão salvos, basta modificar o caminho no script. O caminho padrão de download é:

```python
caminho_destino = "/home/usuario/Videos/videos-baixados-pelo-script"
```

Altere para o diretório desejado no seu sistema.


## 4. Problemas Comuns e Soluções

#### 1. Erro: "ModuleNotFoundError"
Se você encontrar o erro `ModuleNotFoundError`, isso significa que o Python não encontrou o módulo necessário. Tente instalar novamente a biblioteca com:

```bash
pip install yt-dlp
```

#### 2. Erro: "HTTP Error 403"
Se ocorrer um erro de permissão ao tentar acessar o YouTube (HTTP Error 403), isso pode ser causado por uma limitação do YouTube ou pela configuração do script. Certifique-se de estar utilizando uma versão recente da biblioteca yt-dlp.

```bash
python3 -m pip install --upgrade yt-dlp
```

#### 3. Erro: "Player AV1 Decoder"
Se ao reproduzir o vídeo ocorrer um erro informando a falta do "AV1 decoder", instale o codec necessário para reprodução de vídeos em formatos mais novos. Para sistemas Linux, isso pode ser feito através do seguinte comando:

```bash
sudo apt install ffmpeg
```

---


