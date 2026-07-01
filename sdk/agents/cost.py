from pydantic import BaseModel


class AgentCost(BaseModel):
    """
    Tracks and limits the financial API spend for the agent.
    """

    total_tokens_used: int = 0
    total_spend_usd: float = 0.0
    budget_limit_usd: float = 5.0
