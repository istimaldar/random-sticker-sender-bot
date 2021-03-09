from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    environments=False,
    envvar_prefix="RNDSTSND",
    settings_files=["settings.toml", ".secrets.toml"],
    merge_enabled=True,
    validators=[
        Validator("bot.token", must_exist=True, is_type_of=str),
        Validator("bot.packs", must_exist=True, is_type_of=list, len_min=1),
        Validator("bot.options", must_exist=True, is_type_of=int, gt=0, lte=10),
        Validator("messages.start", must_exist=True, is_type_of=str),
        Validator("messages.help", must_exist=True, is_type_of=str),
        Validator("messages.privacy", must_exist=True, is_type_of=str),
        Validator("messages.unknown", must_exist=True, is_type_of=str)
    ]
)