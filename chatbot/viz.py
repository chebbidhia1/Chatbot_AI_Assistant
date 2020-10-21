from IPython.display import Image
from rasa_core.agent import Agent


agent = Agent('domain.yml')
agent.visualize("data/stories.md", "story_graph.png", max_history=10)
Image(filename="story_graph.png")