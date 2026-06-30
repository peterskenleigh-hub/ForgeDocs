from src.builders.cv_builder import CVBuilder
from src.loaders.profile_loader import load_profile


def main():

    profile = load_profile("kenleigh")

    builder = CVBuilder(profile)

    builder.build()

    print("CV Generated Successfully!")


if __name__ == "__main__":
    main()