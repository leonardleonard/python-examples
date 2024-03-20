from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Geolocation:
    id: int
    street: str
    postal_code: str
    city: str
    province: str
    latitude: float
    longitude: float


@dataclass
class Location:
    id: int
    message_id: str
    raw_data: str
    date: datetime
    priority: int
    geolocation: list[Geolocation] = field(default_factory=list)


def generate_breadcrumbs(location: Location) -> dict[str, str]:
    breadcrumbs: dict[str, str] = {}
    main_url = "https://myapi.com"
    if location.geolocation[0]:
        if location.geolocation[0].postal_code:
            breadcrumbs["postal_code_url"] = (
                f"{main_url}/postal_code/{location.geolocation[0].postal_code}/"
            )
        if location.geolocation[0].city:
            city_slug = location.geolocation[0].city.lower().replace(" ", "-")
            breadcrumbs["city_url"] = f"{main_url}/region/{city_slug}/"
        if location.geolocation[0].province:
            breadcrumbs["province_url"] = (
                f"{main_url}/region/province/{location.geolocation[0].province.lower()}/"
            )
    return breadcrumbs


def main() -> None:
    location = Location(
        id=1,
        message_id="123",
        raw_data="raw",
        date=datetime.now(),
        priority=1,
        geolocation=[
            Geolocation(
                id=1,
                street="123 Main St",
                postal_code="12345",
                city="Toronto",
                province="ON",
                latitude=43.123,
                longitude=-79.123,
            )
        ],
    )
    print(generate_breadcrumbs(location))


if __name__ == "__main__":
    main()
