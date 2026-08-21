from TOOLS.capacity_model_tool import model_capacity
from TOOLS.cost_model_tool import assess_cost
from TOOLS.reliability_tool import assess_reliability
from TOOLS.topology_tool import validate_topology


def test_capacity_model_handles_zero_capacity():
    result = model_capacity(10, 0)
    assert result["sufficient"] is False
    assert result["utilization"] == 1.0


def test_cost_model_reports_variance():
    result = assess_cost(1200, 1000)
    assert result["over_budget"] is True
    assert result["variance"] == 200


def test_reliability_requires_restore_test():
    result = assess_reliability(3, 3, True, False)
    assert result["resilient"] is False


def test_topology_normalizes_and_detects_missing():
    result = validate_topology(["api", "queue", "api"], ["api"])
    assert result["missing_capabilities"] == ["queue"]
