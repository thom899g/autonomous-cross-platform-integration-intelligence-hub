import logging
from typing import Any
from apilink.api_discovery import APIManager, APIService

class IntegrationWorkflow:
    def __init__(self):
        self.steps = []
    
    def add_step(self, function: callable, *args, **kwargs) -> None:
        self.steps.append((function, args, kwargs))
    
    async def execute_workflow(self) -> Any:
        result = None
        for func, args, kwargs in self.steps:
            try:
                result = await func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Workflow step failed: {e}")
                raise
        return result

class IntegrationEngine:
    def __init__(self):
        self.workflows = {}
    
    async def register_workflow(self, name: str, workflow: IntegrationWorkflow) -> None:
        self.workflows[name] = workflow
    
    async def run_workflow(self, name: str) -> Any:
        if name not in self.workflows:
            raise ValueError(f"Workflow {name} not registered")
        return await self.workflows[name].execute_workflow()