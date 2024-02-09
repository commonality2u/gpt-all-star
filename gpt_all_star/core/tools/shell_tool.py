import logging
import platform
import subprocess
import warnings
from typing import Optional, Type, Union

from langchain_core.callbacks import (
    CallbackManagerForToolRun,
)
from langchain_core.pydantic_v1 import BaseModel, Field, root_validator
from langchain_core.tools import BaseTool

logger = logging.getLogger(__name__)


class ShellInput(BaseModel):
    """Commands for the Bash Shell tool."""

    commands: Union[str, list[str]] = Field(
        ...,
        description="List of shell commands to run. Deserialized using json.loads",
    )
    """List of shell commands to run."""

    @root_validator
    def _validate_commands(cls, values: dict) -> dict:
        """Validate commands."""
        # TODO: Add real validators
        commands = values.get("commands")
        if not isinstance(commands, list):
            values["commands"] = [commands]
        # Warn that the bash tool is not safe
        warnings.warn(
            "The shell tool has no safeguards by default. Use at your own risk."
        )
        return values


def _get_platform() -> str:
    """Get platform."""
    system = platform.system()
    if system == "Darwin":
        return "MacOS"
    return system


class ShellTool(BaseTool):
    name: str = "terminal"
    """Name of tool."""

    description: str = f"Run shell commands on this {_get_platform()} machine."
    """Description of tool."""

    args_schema: Type[BaseModel] = ShellInput
    """Schema for input arguments."""

    ask_human_input: bool = False
    """
    If True, prompts the user for confirmation (y/n) before executing
    a command generated by the language model in the bash shell.
    """

    root_dir: str = "./"
    """If specified, all file operations are made relative to root_dir."""

    verbose: bool = False
    """If True, print the stdout."""

    def _run(
        self,
        commands: Union[str, list[str]],
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Run commands and return final output."""

        print(f"Executing command:\n {commands}")

        try:
            if self.ask_human_input:
                user_input = input("Proceed with command execution? (y/n): ").lower()
                if user_input == "y":
                    process = subprocess.Popen(
                        commands,
                        shell=True,
                        cwd=self.root_dir,
                        text=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                    )
                    stdout, stderr = process.communicate()
                    if process.returncode != 0:
                        logger.error(f"Error during command execution: {stderr}")
                        return None
                    if self.verbose:
                        print(stdout)
                    return stdout
                else:
                    logger.info("Invalid input. User aborted command execution.")
                    return None
            else:
                process = subprocess.Popen(
                    commands,
                    shell=True,
                    cwd=self.root_dir,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                stdout, stderr = process.communicate()
                if process.returncode != 0:
                    logger.error(f"Error during command execution: {stderr}")
                    return None
                if self.verbose:
                    print(stdout)
                return stdout

        except Exception as e:
            logger.error(f"Error during command execution: {e}")
            return None
