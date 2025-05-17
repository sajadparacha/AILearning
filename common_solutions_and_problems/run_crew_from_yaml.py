import os
from crewai import Crew, Task, Agent
# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
import yaml
import warnings
warnings.filterwarnings('ignore')

class CrewFromYAML:
    def __init__(self, yaml_path: str, openai_api_key: str):
        os.environ["OPENAI_API_KEY"] = openai_api_key
        self.yaml_path = yaml_path
        self.agents = self.load_agents()

    def load_agents(self):
        with open(self.yaml_path, 'r') as file:
            data = yaml.safe_load(file)

        agents = []
        for agent_data in data.get('agents', []):
            llm_config = agent_data.get("llm", {})
            llm = ChatOpenAI(
                model_name=llm_config.get("model", "gpt-4"),
                temperature=llm_config.get("temperature", 0.3)
            )
            agent = Agent(
                name=agent_data["name"],
                role=agent_data["role"],
                goal=agent_data["goal"],
                backstory=agent_data["backstory"],
                llm=llm,
                allow_delegation=False
            )
            agents.append(agent)
        return agents

    def define_tasks(self):
        return [
            Task(
                description="Analyze the user query: 'How do I upload drilling reports in the portal?'",
                expected_output="Identify user intent and relevant documentation area.",
                agent=self.agents[0]
            ),
            Task(
                description="Provide an accurate solution using document knowledge.",
                expected_output="Concise answer with explanation.",
                agent=self.agents[1]
            ),
            Task(
                description="Verify that the solution is accurate and based on source documents.",
                expected_output="Corrected or validated version of the response.",
                agent=self.agents[2]
            ),
            Task(
                description="Polish the final response to be clear, professional, and polite.",
                expected_output="Polished user-facing response.",
                agent=self.agents[3]
            )
        ]

    def run(self):
        crew = Crew(
            agents=self.agents,
            tasks=self.define_tasks(),
            verbose=True
        )
        result = crew.kickoff()
        print("\n=== Final Output ===\n")
        print(result)


# ==== Run the Crew ====
if __name__ == "__main__":
    # Replace with your actual OpenAI key or ensure it’s in the environment
    # OPENAI_API_KEY = "your-openai-api-key-here"
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    yaml_path = "agents.yaml"

    runner = CrewFromYAML(yaml_path, openai_api_key=OPENAI_API_KEY)
    runner.run()