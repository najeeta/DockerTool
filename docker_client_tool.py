from docker import DockerClient
from superagi.tools.base_tool import BaseTool

class DockerClientTool(BaseTool):
    name: str = "Docker Tool"
    description: str = "Tool for interacting with Docker"

    def __init__(self, version='auto', timeout=None, max_pool_size=None, ssl_version=None, assert_hostname=None, environment=None, credstore_env=None, use_ssh_client=None):
        self.client = DockerClient(
            version=version,
            timeout=timeout,
            max_pool_size=max_pool_size,
            ssl_version=ssl_version,
            assert_hostname=assert_hostname,
            environment=environment,
            credstore_env=credstore_env,
            use_ssh_client=use_ssh_client
        )
    

    





