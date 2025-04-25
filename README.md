# 🎬 Transcrição de Vídeo com Whisper

Este projeto realiza **extração de áudio de vídeos** e a posterior **transcrição automática do conteúdo falado**, utilizando o modelo Whisper da OpenAI.

## 📌 O que o projeto faz

A aplicação:
1. Carrega um vídeo local.
2. Extrai o áudio do vídeo em formato `.mp3`.
3. Usa o modelo Whisper para transcrever o áudio.
4. Salva a transcrição em um arquivo `.txt`.

Simples, direto e funcional — ideal para gerar legendas, anotações ou facilitar a análise de vídeos com conteúdo falado.

## 🧠 Tecnologias e bibliotecas

- [`moviepy`](https://zulko.github.io/moviepy/) – para carregar o vídeo e extrair o áudio.
- [`whisper`](https://github.com/openai/whisper) – modelo de transcrição automática desenvolvido pela OpenAI.

## 🚀 Como usar

1. Instale as dependências:

```bash
pip install moviepy openai-whisper

2. No código, defina o caminho do seu vídeo na variável video_path:
video_path = "seu_video.mp4"

3. Execute o script:
python main.py

4. A transcrição será salva em um arquivo transcricao.txt no mesmo diretório.

⚙️ Modelos disponíveis

O Whisper permite escolher entre diferentes tamanhos de modelos:
  tiny, base, small, medium, large

Quanto maior o modelo, maior a precisão — mas também o tempo de execução.
model = whisper.load_model("medium")

💡 Exemplo de saída
Transcrição salva.
