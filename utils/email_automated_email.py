import json
import uuid
from pathlib import Path


def generate_unique_suffix(suffix_length=8):
    """Generate a random suffix that will keep created data unique across runs."""
    return uuid.uuid4().hex[:suffix_length]


def generate_unique_email(base_email, suffix_length=8):
    """Generate a unique email while preserving the original email domain."""
    local_part, domain = base_email.split("@", 1)
    unique_suffix = generate_unique_suffix(suffix_length)
    return f"{local_part}{unique_suffix}@{domain}"


def generate_unique_name(base_name, suffix_length=8):
    """Generate a unique name by appending a random suffix."""
    return f"{base_name}{generate_unique_suffix(suffix_length)}"


def generate_unique_password(base_password, suffix_length=8):
    """Generate a unique password by appending a random suffix."""
    return f"{base_password}{generate_unique_suffix(suffix_length)}"


def build_unique_user_record(base_user, suffix_length=8):
    """Return a new user dict with unique email, password, and name values."""
    return {
        "email": generate_unique_email(base_user["email"], suffix_length),
        "password": generate_unique_password(base_user["password"], suffix_length),
        "name": generate_unique_name(base_user["name"], suffix_length),
    }


def refresh_register_user_file(file_path="data/test_register_user.json", suffix_length=8):
    """Read the register-user JSON file, generate new unique values, and write them back in place."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    if isinstance(records, dict):
        records = [records]

    updated_records = [
        build_unique_user_record(record, suffix_length)
        for record in records
    ]

    with path.open("w", encoding="utf-8") as file:
        json.dump(updated_records, file, indent=4)
        file.write("\n")

    return updated_records
