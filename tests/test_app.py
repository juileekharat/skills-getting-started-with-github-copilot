from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_them_from_activity():
    response = client.delete("/activities/Chess Club/participants/michael@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"

    activities_response = client.get("/activities")
    activities = activities_response.json()["Chess Club"]
    assert "michael@mergington.edu" not in activities["participants"]


def test_unregister_participant_returns_404_when_not_found():
    response = client.delete("/activities/Chess Club/participants/does-not-exist@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
