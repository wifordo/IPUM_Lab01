import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    # Ładowanie .env
    env_path = f"config/.env.{environment}"
    load_dotenv(dotenv_path=env_path, override=True)

    if os.path.exists("secrets.yaml"):
        with open("secrets.yaml", "r") as f:
            secrets = yaml.safe_load(f)
            if secrets:
                for key, value in secrets.items():
                    os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()
    export_envs(args.environment)

    settings = Settings()
    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("SECRET: ", settings.SUPER_SECRET_KEY)
