from crewai import Crew, Process
from agents.roteirista import Roteirista
from agents.thumbnail_creator import ThumbnailCreator
from agents.revisor import Revisor

# Definição das tarefas
tarefas = [
    {
        "description": "Gerar um roteiro detalhado para o vídeo",
        "agent": Roteirista
    },
    {
        "description": "Criar 3 opções de thumbnails inspiradas no roteiro",
        "agent": ThumbnailCreator
    },
    {
        "description": "Revisar o roteiro e escolher a melhor thumbnail",
        "agent": Revisor
    }
]

# Criar a crew
VideoCrew = Crew(
    agents=[Roteirista, ThumbnailCreator, Revisor],
    tasks=tarefas,
    process=Process.sequential,  # execução em sequência
    verbose=True
)
