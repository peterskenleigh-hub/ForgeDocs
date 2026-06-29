from src.models.profile import Profile


def main():
    profile = Profile(
        full_name="Kenleigh Peters",
        professional_title="Business Systems & Technology Specialist",
        email="peterskenleigh@gmail.com",
        phone="078 659 0158",
        location="East London, South Africa",
        summary="Passionate about solving business problems through technology."
    )

    print(profile)


if __name__ == "__main__":
    main()
    