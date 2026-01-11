class Agent:
    def __init__(self, name, weight, agent_type="support"):
        """
        agent_type:
            - "support": 支持阳性（Pneumonia）
            - "oppose": 支持阴性（Normal）
        """
        self.name = name
        self.weight = weight
        self.agent_type = agent_type
        self.belief = 0.0      # 对“阳性”的支持度（score）
        self.weight = 1.0      # 在 global belief 中的权重

    def update_weight(self, shared_beliefs):
        """
        根据与其他 agent 的 belief 差异调整权重
        """
        if len(shared_beliefs) <= 1:
            return

        avg_other = sum(
            v for k, v in shared_beliefs.items() if k != self.name
        ) / (len(shared_beliefs) - 1)

        diff = self.belief - avg_other

        # 差异越大，权重变化越明显（但受限）
        self.weight += 0.1 * diff
        self.weight = max(0.1, min(self.weight, 2.0))

    def act(self, visual_state, dialogue, global_belief):
        """
        根据视觉、对话和 global belief 更新 belief
        """
        delta = 0.0

        # ===== 1. 视觉证据 =====
        intensity = visual_state.get("mean_intensity", 0)

        if self.agent_type == "support":
            # 异常 → 支持阳性
            if intensity > 150:
                delta += 0.3
            else:
                delta -= 0.2

        elif self.agent_type == "oppose":
            # 正常 → 反对阳性
            if intensity < 120:
                delta -= 0.3
            else:
                delta += 0.2

        # ===== 2. 对话证据（示意）=====
        if dialogue:
            if self.agent_type == "support":
                delta += 0.05
            else:
                delta -= 0.05

        # ===== 3. global belief 影响（关键）=====
        if global_belief is not None:
            if self.agent_type == "support":
                # 顺应主流
                delta += 0.1 * global_belief
            else:
                # 抵抗主流
                delta -= 0.1 * global_belief

        # ===== 4. 更新 belief =====
        self.belief += delta
        return self.belief
