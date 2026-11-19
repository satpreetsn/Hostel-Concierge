from hostel_concierge.core.auth import authenticate_guest

def test_valid_guest_authentication():
    guest = authenticate_guest("alex@example.com", "sunrise123")

    assert guest is not None
    assert guest.guest_id == "GUEST001"
    assert guest.name == "Alex Johnson"

def test_invalid_password():
    
    guest = authenticate_guest("alex@example.com", "wrongpassword")
    
    assert guest is  None

def test_unknown_guest():
    guest = authenticate_guest("unknown@example.com", "sunrise123")
    
    assert guest is None

def test_email_is_case_insensitive():
    guest = authenticate_guest("ALEX@EXAMPLE.COM", "sunrise123")
    
    assert guest is not None
    assert guest.guest_id == "GUEST001"
    assert guest.name == "Alex Johnson"

def test_unknown_guest():
    guest = authenticate_guest("unknown@example.com", "sunrise123")

    assert guest is None


def test_email_is_case_insensitive():
    guest = authenticate_guest("ALEX@EXAMPLE.COM", "sunrise123")

    assert guest is not None
    assert guest.guest_id == "GUEST001"


def test_all_ten_guests_can_authenticate():
    guests = [
        ("alex@example.com", "sunrise123"),
        ("maya@example.com", "sunrise456"),
        ("john@example.com", "sunrise789"),
        ("emma@example.com", "sunrise101"),
        ("rahul@example.com", "sunrise202"),
        ("sophia@example.com", "sunrise303"),
        ("david@example.com", "sunrise404"),
        ("olivia@example.com", "sunrise505"),
        ("arjun@example.com", "sunrise606"),
        ("isabella@example.com", "sunrise707"),
    ]

    for email, password in guests:
        assert authenticate_guest(email, password) is not None