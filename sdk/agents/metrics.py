from pydantic import BaseModel


class AgentMetrics(BaseModel):
    """
    Telemetry and performance data.
    """

    total_invocations: int = 0
    success_rate: float = 1.0
    average_latency_ms: float = 0.0
    reasoning_depth_avg: float = 0.0
