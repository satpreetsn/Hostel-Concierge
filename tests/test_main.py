from hostel_concierge.main import main

def test_application_starts_and_exits(monkeypatch, capsys):
    """Verify that the application starts and exits correctly."""

    monkeypatch.setattr("builtins.input", lambda _: "exit")

    main()

    captured = capsys.readouterr()

    assert "WELCOME TO HOSTEL-CONCIERGE" in captured.out
    assert "Goodbye" in captured.out