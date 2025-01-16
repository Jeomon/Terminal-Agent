from src.agent.terminal.views import Action,ActionResult
from src.tool import Tool

class Registry:
    def __init__(self,actions:list[Tool]):
        self.actions=actions
        self.registry=self.action_registry()
    
    def actions_prompt(self):
        actions_prompt=[action.prompt() for action in self.actions]
        return '\n\n'.join(actions_prompt)
    
    def action_registry(self)->dict[str,Action]:
        return {action.name : Action(name=action.name,description=action.description,params=action.params,function=action.func) for action in self.actions}
    
    def execute(self,name:str,params:dict)->ActionResult:
        action=self.registry.get(name)
        try:
            if action is None:
                raise ValueError('Tool not found')
            content=action.function(**params)
            return ActionResult(name=name,content=content)
        except Exception as e:
            return ActionResult(name=name,content=str(e))

        
    
