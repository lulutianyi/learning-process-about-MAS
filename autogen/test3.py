from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

llm_config = {
    "config_list": [
        {
            "model": "gpt-4o-mini",
            "api_key": "sk-xxxxx",
        }
    ],
    "temperature": 0.7,
}

# 這邊故意不設定 code_execution_config，就不會觸發 python 執行相關的東西
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
     code_execution_config={"use_docker": False} ,
    max_consecutive_auto_reply=12,
    # 關鍵：完全不寫 code_execution_config
)

planner = AssistantAgent(
    name="Planner",
    llm_config=llm_config,
    code_execution_config={"use_docker": False} ,
    system_message="你是冷靜、結構化的規劃專家，總是用編號列表回應。"
)

critic = AssistantAgent(
    name="Critic",
    llm_config=llm_config,
    code_execution_config={"use_docker": False} ,
    system_message="你是尖銳但有建設性的批評者，專門找出邏輯漏洞、風險、反方觀點。"
)

writer = AssistantAgent(
    name="Writer",
    llm_config=llm_config,
    system_message="你是文筆優美、說服力強的寫作者，負責把討論結果整理成流暢的文章。"
)

groupchat = GroupChat(
    agents=[user_proxy, planner, critic, writer],
    messages=[],
    max_round=15,
)

manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(
    manager,
    message="""辯論題目：2030年前，私人太空旅行會成為像現在坐飛機一樣普遍的交通方式嗎？

請大家輪流發言，最後由 Writer 總結成一篇 400-600 字的立場清晰文章。"""
)