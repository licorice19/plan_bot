import os
import configparser
from typing import Dict, Any
basedir = os.path.abspath(os.path.dirname(__file__))

class AppConfig:
    """
    Универсальный класс конфигурации приложения
    """

    def __init__(self, config_file: str):
        """
        Инициализирует объект AppConfig.

        Args:
            config_file: Путь к файлу конфигурации.
        """

        self._config_file = config_file
        self._config = configparser.ConfigParser()
        self._config.read(self._config_file)

    def get_section(self, section: str) -> Dict[str, Any]:
        """
        Возвращает словарь с настройками для указанной секции.

        Args:
            section: Название секции.

        Returns:
            Словарь с настройками для указанной секции.

        Raises:
            KeyError: Если секция не найдена.
        """

        if section not in self._config:
            raise KeyError(f"Секция '{section}' не найдена в файле конфигурации.")
        return dict(self._config[section])

    def get_value(self, section: str, option: str, default: Any = None, type: type = str) -> Any:
        """
        Возвращает значение настройки по указанной секции и ключу.

        Args:
            section: Название секции.
            option: Название настройки.
            default: Значение по умолчанию, если настройка не найдена.
            type: Тип данных, к которому нужно привести значение.

        Returns:
            Значение настройки или значение по умолчанию, если настройка не найдена.
        """

        try:
            value = self._config.get(section, option)
            if type == bool:
                return self._config.getboolean(section, option)
            elif type == int:
                return self._config.getint(section, option)
            elif type == float:
                return self._config.getfloat(section, option)
            else:
                return type(value)
        except (configparser.NoOptionError, configparser.NoSectionError):
            return default

    def set_value(self, section: str, option: str, value: Any) -> None:
        """
        Устанавливает значение настройки по указанной секции и ключу.

        Args:
            section: Название секции.
            option: Название настройки.
            value: Новое значение настройки.
        """

        if not self._config.has_section(section):
            self._config.add_section(section)
        self._config.set(section, option, str(value))
        self.save()

    def save(self) -> None:
        """
        Сохраняет изменения в файле конфигурации.
        """

        with open(self._config_file, 'w') as configfile:
            self._config.write(configfile)

config = AppConfig('config.ini')

if not config._config.has_section('bot'):
    config._config.add_section('bot')
    config.set_value('bot', 'token', 'Default')
    config.set_value('bot', 'debug', True)
    config.save()
    
token = config.get_value('bot', 'token', 'Default')
debug = config.get_value('bot', 'debug', True)