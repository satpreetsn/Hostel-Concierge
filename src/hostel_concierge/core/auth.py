import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Guest:
    guest_id: str
    name: str
    email: str

def load_guests() -> list[dict[str, str]]:
    """
    Load guest records from the CSV file.
    """

    csv_path = (
        Path(__file__).resolve().parents[3]
        / "data"
        / "guests.csv"
    )

    with csv_path.open(mode = "r",
                       newline = "",
                       encoding= "utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def authenticate_guest(email: str,
                       password: str) -> Guest | None:

    """
    Authenticate a guest using their email and password.

    Returns:
        Guest object if credentials are valid.
        None if Authentication fails.
    """

    guests = load_guests()

    normalized_email = email.strip().lower()

    for record in guests:
        if(
            record["email"].strip().lower() == normalized_email
            and record["password"] == password
        ):
            return Guest(
                guest_id= record["guest_id"],
                name = record["name"],
                email = record["email"],
            )
    return None

