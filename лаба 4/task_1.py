class Game:
    """Класс, представляющий общую игру."""
    def __init__(self, title: str, year: int) -> None:
        """ title: Название игры.
            year: Год выпуска игры."""
        self._title = title
        self._year = year

    @property
    def title(self) -> str:
        """Возвращает название игры."""
        return self._title

    @property
    def year(self) -> int:
        """Возвращает год выпуска игры."""
        return self._year

    def __str__(self) -> str:
        """Возвращает строковое представление игры."""
        return f"Игра: {self.title} ({self.year})"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"{type(self).__name__}(title={self.title!r}, year={self.year!r})"


class BoardGame(Game):
    """Класс, представляющий настольную игру."""
    def __init__(self, title: str, year: int, player_count: int) -> None:
        """ title: Название игры.
            year: Год выпуска игры.
            player_count: Количество игроков в игре."""
        super().__init__(title, year)
        if player_count < 1:
            raise ValueError("Количество игроков должно быть больше 0.")
        self._player_count = player_count

    @property
    def player_count(self) -> int:
        """Возвращает количество игроков в настольной игре."""
        return self._player_count

    def set_player_count(self, count: int) -> None:
        """Устанавливает количество игроков в настольной игре.

        Аргументы:
            count (int): Новое количество игроков. Должно быть больше 0.

        Исключения:
            ValueError: Если количество игроков меньше 1.
        """
        if count < 1:
            raise ValueError("Количество игроков должно быть больше 0.")
        self._player_count = count

    def __str__(self) -> str:
        """Перегруженный метод __str__ для отображения информации о настольной игре.

        Возвращает строку с названием игры, годом выпуска и количеством игроков.
        """
        return f"{super().__str__()} - Количество игроков: {self.player_count}"

    @property
    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"{type(self).__name__}(title={self.title!r}, year={self.year!r}, player_count={self.player_count!r})"

    def play(self) -> str:
        """Запускает игру и сообщает количество игроков.

        Возвращает строку с информацией о начале игры.
        """
        return f"Начинаем играть в {self.title} с {self.player_count} игроками."


class VideoGame(Game):
    def __init__(self, title: str, year: int, platform: str) -> None:
        """  title: Название игры.
            year : Год выпуска игры.
            platform: Платформа, на которой доступна игра."""
        super().__init__(title, year)
        self._platform = platform

    @property
    def platform(self) -> str:
        """Возвращает платформу видеоигры."""
        return self._platform

    def __str__(self) -> str:
        """Перегруженный метод __str__ для отображения информации о видеоигре.

        Возвращает строку с названием игры, годом выпуска и платформой.
        """
        return f"{super().__str__()} - Платформа: {self.platform}"

    @property
    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"{type(self).__name__}(title={self.title!r}, year={self.year!r}, platform={self.platform!r})"

    def play(self) -> str:
        """Запускает игру на определенной платформе.

        Возвращает строку с информацией о начале игры на платформе.
        """
        return f"Играем в {self.title} на платформе {self.platform}"
