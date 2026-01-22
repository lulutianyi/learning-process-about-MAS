class Agent:
    def __init__(self, name):
        self.name = name

    def plan(self):
        return f"{self.name} is planning."

    def execute(self, task):
        return f"{self.name} is executing {task}."

    def evaluate(self, result):
        return f"{self.name} evaluates: {result}"

# Initialize multiple agents
agents = [Agent(f"Agent-{i}") for i in range(3)]

# Example of planning phase
for agent in agents:
    print(agent.plan())

# Define a simple task and agents execute it
task = "calculate 42"
execution_results = []
for agent in agents:
    result = agent.execute(task)
    execution_results.append(result)

# Each agent evaluates the execution results
for agent in agents:
    for result in execution_results:
        print(agent.evaluate(result))