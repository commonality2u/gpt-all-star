from gpt_all_star.core.respond import Respond
from gpt_all_star.core.steps.steps import StepType


class GptAllStar:
    def __init__(self):
        pass

    def chat(self, project_name: str, step: StepType = None, message=None):
        respond = Respond(step=step, project_name=project_name)
        return respond.chat(message=message)

    def execute(self, project_name: str):
        respond = Respond(step=StepType.NONE, project_name=project_name)
        return respond.execute()
