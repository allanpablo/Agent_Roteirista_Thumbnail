# 🎮 Desafio Agentes IA – CrewAI

## 📌 Objetivo
Criar um sistema multiagente para **gerar roteiros e thumbnails para vídeos de videogames**.

## 🛠 Estrutura
- **Roteirista de Vídeo** → pesquisa e cria o roteiro.
- **Criador de Thumbnail** → gera 3 opções de thumbnails.
- **Revisor** → revisa o roteiro e escolhe a melhor thumbnail.

## 🚀 Como rodar
1. Instalar dependências
   ```bash
   pip install crewai
  ``` 

(adicione outras libs como duckduckgo-search se quiser busca real)

Rodar
```bash
python main.py
```

Input:

```bash
inputs={"query": "Melhores jogos de 2020"}
```
