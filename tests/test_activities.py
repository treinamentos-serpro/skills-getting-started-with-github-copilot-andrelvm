def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert len(activities) == 9
    assert "Chess Club" in activities
    assert activities["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_each_activity_has_expected_fields(client):
    activities = client.get("/activities").json()

    for activity in activities.values():
        assert {"description", "schedule", "max_participants", "participants"} <= activity.keys()