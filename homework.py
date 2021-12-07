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

        print(f'Тип тренировки: {self.training_type}; '
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
        # Возвращает дистанцию в км, которую преодолел пользователь
        # за время тренировки
        LEN_STEP = '?????????????'
        M_IN_KM = 1000
        distance = self.action * (LEN_STEP / M_IN_KM)
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance()
        # формула расчёта: преодоленная_дистанция_за_трени-
        # ровку / время_тренировки
        # возвращает значение средней скорости движения во время тренировки
        mean_speed = distance / self.duration 
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # в базовом классе не нужно описывать поведение метода, в его
        # теле останется ключевое слово pass
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        message = InfoMessage(self.action,
                              self.duration,
                              distance,
                              speed,
                              calories
                             )
        return message.show_info_message()


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
        coeff_1 = 18
        coeff_2 = 20
        mean_speed = super().get_mean_speed()
        spent_calories = (coeff_1 * (mean_speed - coeff_2)) * self.weight / 1000 / self.duration
        return spent_calories

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
        coeff_1 = 0.035
        coeff_2 = 2
        coeff_3 = 0.029
        mean_speed = super().get_mean_speed()
        spent_calories = coeff_1 * self.weight + ((mean_speed ** coeff_2) // self.height) * coeff_3 * self.weight)
        return spent_calories
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
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        mean_speed = self.get_mean_speed()
        return (mean_speed + coeff_calorie_1) * coeff_calorie_2 * self.weight

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # длина_бассейна * count_pool / M_IN_KM / время_тренировки
        M_IN_KM = 1000
        return ((self.length_pool * self.count_pool) / M_IN_KM) / self.duration


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
