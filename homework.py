class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
        pass

    def show_info_message(self) -> str:
        """Вернуть строку с информацией о тренировке."""

        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance} км; '
                f'Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        # формула расчёта: action * LEN_STEP / M_IN_KM
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # формула расчёта: преодоленная_дистанция_за_трени-
        # ровку / время_тренировки
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # в базовом классе не нужно описывать поведение метода, в его
        # теле останется ключевое слово pass
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        # возвращает объект класса сообщения
        pass


class Running(Training):
    """Тренировка: бег."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        super().__init__(action, duration, weight)

    # Все свойства и методы этого класса без изменений наследуются
    # от базового класса. Исключение составляет только метод расчёта калорий,
    # его нужно переопределить.

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # формула: (18 * средняя_скорость - 20) * вес_спортсме-
        # на / M_IN_KM * время_тренировки_в_минутах
        pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес) * вре-
        # мя_тренировки_в_минута
        pass
    pass


class Swimming(Training):
    """Тренировка: плавание."""

    # Есть и ещё один параметр, который надо переопределить,
    # ведь расстояние, преодолеваемое за один гребок, отличается
    # от длины шага. Значит, необходимо переопределить атрибут
    # базового класса.

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # (средняя_скорость + 1.1) * 2 * вес
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # длина_бассейна * count_pool / M_IN_KM / время_тренировки
        pass

    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
