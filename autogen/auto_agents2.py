from openai import OpenAI

client = OpenAI()

class Agent:
    def __init__(self, name):
        self.name = name

    def plan(self):
        prompt = f"You are {self.name}. Generate a plan for calculating the factorial of a number."
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def execute(self, task):
        prompt = f"You are {self.name}. Execute the task: {task}. Limit the output to 50 lines."
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def evaluate(self, result):
        prompt = f"You are {self.name}. Evaluate the following result:\n{result}. Limit the evaluation to 50 words."
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content


# ====== demo ======

agents = [Agent(f"Agent-{i}") for i in range(1)]

for agent in agents:
    print("PLAN:", agent.plan())

task = "Write a Python program to calculate the factorial of a number."
results = []

for agent in agents:
    r = agent.execute(task)
    results.append(r)

for agent in agents:
    for r in results:
        print("EVAL:", agent.evaluate(r))
