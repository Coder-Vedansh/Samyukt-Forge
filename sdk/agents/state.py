from enum import Enum


class AgentState(str, Enum):
    """
    The current operational status of the Agent in the Orchestrator.
    """

    IDLE = "idle"
    THINKING = "thinking"
    EXECUTING = "executing"
    WAITING_FOR_HUMAN = "waiting_for_human"
    TERMINATED = "terminated"
    ERROR = "error"
