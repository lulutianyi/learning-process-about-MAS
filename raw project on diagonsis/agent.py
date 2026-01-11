# agent.py

class Agent:
    def __init__(self, name, weight=1.0, threshold=0.8):
        self.name = name
        self.weight = weight
        self.belief = 0.0
        self.threshold = threshold

    def act(self, visual_state, dialogue, global_belief):
        # 视觉证据：一次性提供初始 belief
        if len(dialogue) == 0:
            self.belief += visual_state["mean_intensity"] / 255.0 * 0.5

        # 参考系统全局态势
        if global_belief > 0.6:
            self.belief += 0.05
        else:
            self.belief += 0.15
        return self.belief
    def update_weight(self, shared_beliefs):
        
        if len(shared_beliefs) <= 1:
            return  # 无法沟通，保持原权重

        avg_other = sum(
            v for k, v in shared_beliefs.items() if k != self.name
        ) / (len(shared_beliefs) - 1)

        if avg_other > self.belief:
            self.weight *= 0.9
        else:
            self.weight *= 1.05

        self.weight = min(max(self.weight, 0.1), 1.0)

