from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.fal_tools import FalTools

fal_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[FalTools()],
    description="You are an AI agent that can generate videos using the Fal API.",
    instructions=[
        "When the user asks you to create a video, use the `run` tool to create the video.",
        "Return the URL as raw to the user.",
        "Don't convert video URL to markdown or anything else.",
        "Use `fal-ai/hunyuan-video` model by default.",
        "Also pass the type of model of the tool, it can be either `image` or `video`.",
    ],
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
)

fal_agent.print_response("Generate video of ballon in the ocean")