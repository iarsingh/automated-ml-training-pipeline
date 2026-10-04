from fastapi.testclient import TestClient
from trainpipe.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'rows': 20, 'target': 'churned'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'rows': 2, 'target': 'churned'}).json()
    assert bad["passed"] is False
    assert "too_few_rows" in bad["failed"]
