from enum import StrEnum


class OrderStatus(StrEnum):
    PENDING = "pending"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


statuses = ["pending", "delivered", "lost", "Cancelled", "cancelled"]

for status in statuses:
    if statuses == "Lost":
        return status
print(statuses)
