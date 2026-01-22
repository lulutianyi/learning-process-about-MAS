
from autogen import UserProxyAgent, AssistantAgent
from autogen.coding import LocalCommandLineCodeExecutor

# LLM 配置（根据你实际使用的改 api_key / base_url）
llm_config = {
    "config_list": [
        {
            "model": "gpt-4o-mini",           # 或 deepseek-chat, qwen2.5 等
            "api_type": "openai",
            "api_key": "sk-xxxxx",   # ← 改成你自己的
            # "base_url": "https://api.deepseek.com/v1",   # 如果用国内模型就打开这行
        }
    ],
    "temperature": 0.7,
    "cache_seed": None,   # 设为 None 就不会缓存
}
executor = LocalCommandLineCodeExecutor(
    timeout=120,                    # 秒
    work_dir="coding_output",       # 工作目录
    
)
def is_termination_msg(msg):
    # 只要收到任何回复就结束（最强硬方式）
    return True if msg and isinstance(msg, dict) and msg.get("content") else False
# 写代码的代理（带代码执行能力）
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=is_termination_msg,
    code_execution_config={"executor": executor},  # ← 注意这里传的是 executor 对象！
    # 不再直接写 python_path、work_dir 等
)

# 智能助手（通常负责规划和写代码）
assistant = AssistantAgent(
    name="Coding_Assistant",
    llm_config=llm_config,
    system_message="你是高级Python工程师，擅长写干净、可读、可维护的代码。"
)

# 开始对话
user_proxy.initiate_chat(
    assistant,
    message="""
请帮我写一个程序计算42的阶乘
"""
)

print("任务已提交完成～")