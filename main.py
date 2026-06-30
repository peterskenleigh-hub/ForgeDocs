from src.loaders.profile_loader import load_profile


def main():

    profile = load_profile("kenleigh")

    print(profile)


if __name__ == "__main__":
    main()