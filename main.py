from crew import VideoCrew

if __name__ == "__main__":
    tema = "Melhores jogos de 2020"  # exemplo de input
    print(f"🎮 Iniciando execução para tema: {tema}\n")

    resultado = VideoCrew.kickoff(inputs={"query": tema})

    print("\n✅ Resultado Final:")
    print(resultado)
