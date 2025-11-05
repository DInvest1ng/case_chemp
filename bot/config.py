# bot/config.py


from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"


class Tg_Config(BaseSettings):
    bot_token: str

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8"
    )


if __name__ == "__main__":
    print(Tg_Config())