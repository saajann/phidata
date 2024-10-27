from phi.agent import Agent
from phi.tools.linear_tools import LinearTool

agent = Agent(
    name="Linear Tool Agent",
    tools=[LinearTool()],
    show_tool_calls=True,
    markdown=True,
)


agent.print_response("Show all the assigned to user id '69069")
agent.print_response("Show the issue with the issue id '6969'")
agent.print_response("Update the issue with the issue id '42069'")