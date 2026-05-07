import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_path = os.path.join("config", f".env.{environment}")
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path, override=True)
    else:
        raise FileNotFoundError(f"Environment file not found: {env_path}")

    if os.path.exists("secrets.yaml"):
        with open("secrets.yaml", "r") as f:
            secrets = yaml.safe_load(f)
            if secrets:
                for key, value in secrets.items():
                    os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        choices=["dev", "test", "prod"],
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    try:
        export_envs(args.environment)
        settings = Settings()

        print("APP_NAME: ", settings.APP_NAME)
        print("ENVIRONMENT: ", settings.ENVIRONMENT)
        print("SECRET: ", settings.SUPER_SECRET_KEY)
    except Exception as e:
        print(f"Error: {e}")
