from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit, ToolConfiguration
from superagi.types.key_type import ToolConfigKeyType
from docker_client_tool import DockerClientTool

class DockerToolkit(BaseToolkit, ABC):
    name: str = "Docker Toolkit"
    description: str = "Docker Toolkit contains all tools related to Docker"

    def get_tools(self) -> List[BaseTool]:
        return [DockerClientTool()]

    def get_env_keys(self) -> List[ToolConfiguration]:
        return [
            ToolConfiguration(key="DOCKER_IMAGE", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=False),
            ToolConfiguration(key="DOCKER_TAG", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=False)
        ]

