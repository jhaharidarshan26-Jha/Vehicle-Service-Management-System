"""
Vehicle Service Management System
B.Tech CSE mini-project | Python 3

Features:
- Add, view, update, and delete vehicle service records (CRUD)
- Class-based design and dictionary storage
- Service cost + 18% GST calculation
- Save/load records from services.txt
"""

import json
import os

DATA_FILE = "services.txt"
GST_RATE = 0.18

SERVICE_PRICES = {
    "Oil Change": 1500,
    "Wheel Alignment": 800,
    "Full Service": 4500,
    "Brake Repair": 2200,
}

VALID_STATUSES = {"Pending", "In Progress", "Completed"}


class ServiceRecord:
    """Represents one vehicle service record."""

    def __init__(self, reg_no, owner, vehicle, service, status="Pending"):
        self.reg_no = reg_no.strip().upper()
        self.owner = owner.strip()
        self.vehicle = vehicle.strip()
        self.service = service.strip().title()
        self.status = status.strip().title()

    @property
    def base_cost(self):
        return SERVICE_PRICES[self.service]

    @property
    def total_cost(self):
        return self.base_cost * (1 + GST_RATE)

    def to_dict(self):
        return {
            "reg_no": self.reg_no,
            "owner": self.owner,
            "vehicle": self.vehicle,
            "service": self.service,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["reg_no"],
            data["owner"],
            data["vehicle"],
            data["service"],
            data.get("status", "Pending"),
        )

    def display(self):
        return (
            f"{self.reg_no} | Owner: {self.owner} | Vehicle: {self.vehicle} | "
            f"{self.service} | Cost incl. 18% GST: Rs. {self.total_cost:.2f} "
            f"| Status: {self.status}"
        )


class VehicleServiceManagementSystem:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        # Dictionary is keyed by vehicle registration number.
        self.records = {}
        self.load_records()

    @staticmethod
    def normalize_service(service):
        """Match a service name without depending on capitalization."""
        cleaned = " ".join(service.strip().lower().split())
        for valid_service in SERVICE_PRICES:
            if cleaned == valid_service.lower():
                return valid_service
        return None

    def load_records(self):
        """Load saved records. A missing/empty file starts with no records."""
        if not os.path.exists(self.filename):
            self.records = {}
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:
                    self.records = {}
                    return
                data = json.loads(content)
                self.records = {
                    item["reg_no"].upper(): ServiceRecord.from_dict(item)
                    for item in data
                }
        except (json.JSONDecodeError, KeyError, TypeError, OSError) as error:
            print(f"Warning: Could not load saved records ({error}). Starting empty.")
            self.records = {}

    def save_records(self):
        """Save the dictionary records as readable JSON in services.txt."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [record.to_dict() for record in self.records.values()],
                file,
                indent=4,
            )

    def add_record(self, reg_no, owner, vehicle, service):
        reg_no = reg_no.strip().upper()
        valid_service = self.normalize_service(service)

        if not reg_no or not owner.strip() or not vehicle.strip():
            return "Invalid input. Registration number, owner, and vehicle are required."
        if valid_service is None:
            choices = ", ".join(SERVICE_PRICES)
            return f"Invalid service type. Choose from: {choices}."
        if reg_no in self.records:
            return f"Record already exists for {reg_no}."

        record = ServiceRecord(reg_no, owner, vehicle, valid_service)
        self.records[reg_no] = record
        self.save_records()
        return (
            f"Record added. {record.reg_no} | {record.service} | "
            f"Cost incl. 18% GST: Rs. {record.total_cost:.2f} "
            f"| Status: {record.status}"
        )

    def view_records(self):
        if not self.records:
            return "No service records found."
        return "\n".join(record.display() for record in self.records.values())

    def update_status(self, reg_no, new_status):
        reg_no = reg_no.strip().upper()
        if reg_no not in self.records:
            return f"No record found for {reg_no}."
        normalized_status = " ".join(new_status.strip().lower().split()).title()
        if normalized_status not in VALID_STATUSES:
            return "Invalid status. Choose: Pending, In Progress, or Completed."
        old_status = self.records[reg_no].status
        self.records[reg_no].status = normalized_status
        self.save_records()
        return f"Status updated: {old_status} -> {normalized_status}"

    def delete_record(self, reg_no):
        reg_no = reg_no.strip().upper()
        if reg_no not in self.records:
            return f"No record found for {reg_no}."
        del self.records[reg_no]
        self.save_records()
        return f"Record for {reg_no} deleted."


def show_menu():
    print("\n===== VEHICLE SERVICE MANAGEMENT SYSTEM =====")
    print("1. Add record")
    print("2. View records")
    print("3. Update status")
    print("4. Delete record")
    print("5. Exit")


def main():
    system = VehicleServiceManagementSystem()
    print("Vehicle Service Management System started.")
    print(f"Available services and base prices (before GST): {SERVICE_PRICES}")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Add Service Record ---")
            reg_no = input("Registration number: ")
            owner = input("Owner name: ")
            vehicle = input("Vehicle type/model: ")
            print("Available service types:", ", ".join(SERVICE_PRICES))
            service = input("Service type: ")
            print(system.add_record(reg_no, owner, vehicle, service))

        elif choice == "2":
            print("\n--- Service Records ---")
            print(system.view_records())

        elif choice == "3":
            print("\n--- Update Service Status ---")
            reg_no = input("Registration number: ")
            print("Valid statuses: Pending, In Progress, Completed")
            new_status = input("New status: ")
            print(system.update_status(reg_no, new_status))

        elif choice == "4":
            print("\n--- Delete Service Record ---")
            reg_no = input("Registration number: ")
            print(system.delete_record(reg_no))

        elif choice == "5":
            print("Records saved. Goodbye!")
            break

        else:
            print("Invalid menu choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
