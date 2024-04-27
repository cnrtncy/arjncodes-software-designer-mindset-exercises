""" This module contains the solution for the exercise related to the dataclasses module. It creates a system for managing the customers' phone plans."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import random
import string


""" 
EXERCISE -> The mobile phone company PhonyPhones needs to create a system for managing their customers' phone plans 
and they need to get better insight into the data that they need to store. 
Because their CEO knows a bit of Python, he asks you to write a few dataclasses representing the data structure of their application. 
In short, they have customers (name, address, email address), phones (brand, model, price, serial number) and plans (which refer to a customer, 
a phone, a start date, the total number of months in the contract, 
a monthly price, and whether the phone is included in the contract).
Write dataclasses that can represent this data. You may take some freedom in how things like addresses etc. are represented.
"""


def generate_serial_number(brand: str, model: str) -> str:
    """Generate a random serial number for a phone."""

    digits = "".join(random.choices(string.digits, k=8))
    return f"{brand[0]}-{model[0:3]}-{digits}"


@dataclass
class Address:
    """Dataclass representing an address."""

    street: str
    number: int
    city: str
    postal_code: str

    def __str__(self) -> str:
        """Return the address in a human-readable format."""

        return f"{self.street} {self.number}, {self.city} {self.postal_code}"


class Brand(Enum):
    """Enum representing the phone brands that the Company has the inventory."""

    APPLE = "Apple"
    SAMSUNG = "Samsung"
    GOOGLE = "Google"
    HUAWEI = "Huawei"
    XIAOMI = "Xiaomi"
    MOTOROLA = "Motorola"


class Contract(Enum):
    """Enum representing the contract duration in months."""

    MINIMUM = 6
    MEDIUM = 12
    MAXIMUM = 24


class Currency(Enum):
    """Enum representing the currency that the Company uses for the plans. Accepted values are USD, EUR, GBP, JPY."""

    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"


@dataclass
class Customer:
    """Dataclass representing a customer which is neccessary for creating a plan. It can be extended with more fields."""

    name: str
    address: Address
    email: str


@dataclass
class Phone:
    """Dataclass representing a phone that the Company has in the inventory."""

    brand: Brand
    model: str
    price: float
    serial_number: str = field(init=False)

    def __post_init__(self):
        """Generate a serial number for the phone when it is created."""

        self.serial_number = generate_serial_number(self.brand.value, self.model)


@dataclass
class Plan:
    """Dataclass representing a plan that the Company offers to the customers. It prints the details of the plan when it is created."""

    customer: Customer
    phone: Phone
    monthly_price: float
    phone_included: bool = True
    start_date: datetime = datetime.now()
    total_months: Contract = Contract.MEDIUM
    currency: Currency = Currency.USD

    def __post_init__(self):
        """Print the details of the plan when it is created."""

        print(f"Plan for {self.customer.name} created.")
        print(f"Plan details: {self}")

    def total_price(self) -> float:
        """Calculate the total price of the plan."""

        return self.monthly_price * self.total_months.value


def main() -> None:
    """Create a plan for a customer with a phone included."""

    customer = Customer(
        name="John Doe",
        address=Address(
            street="Main Street",
            number=123,
            city="New York",
            postal_code="10001",
        ),
        email="johndoe@example.com",
    )

    Plan(
        customer=customer,
        phone=Phone(brand=Brand.APPLE, model="iPhone 12", price=999.99),
        monthly_price=99.99,
        phone_included=True,
        total_months=Contract.MEDIUM,
        currency=Currency.USD,
    )


if __name__ == "__main__":
    main()
