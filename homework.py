class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
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

        return(f'Тип тренировки: {self.training_type}; '
               f'Длительность: {self.duration:.1f} ч.; '
               f'Дистанция: {self.distance:.1f} км; '
               f'Ср. скорость: {self.speed:.1f} км/ч; '
               f'Потрачено ккал: {self.calories:.1f}.')


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 training_type,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.training_type = training_type
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = 0.65
        self.M_IN_KM = 1000

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance()
        mean_speed = distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        message = InfoMessage(self.training_type,
                              self.duration,
                              distance,
                              speed,
                              calories)
        return message


class Running(Training):
    """Тренировка: бег."""

    def __init__(self,
                 training_type: str,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        super().__init__(training_type, action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_1 = 18
        coeff_2 = 20
        mean_speed = super().get_mean_speed()
        return ((coeff_1 * mean_speed - coeff_2)
                * self.weight / self.M_IN_KM
                * self.duration)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self,
                 training_type: str,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(training_type, action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_1 = 0.035
        coeff_2 = 2
        coeff_3 = 0.029
        mean_speed = super().get_mean_speed()
        spent_calories = ((coeff_1 * self.weight + (mean_speed ** coeff_2
                          // self.height) * coeff_3 * self.weight)
                          * self.duration)
        return spent_calories
    pass


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self,
                 training_type: str,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(training_type, action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        mean_speed = self.get_mean_speed()
        spent_calories = ((mean_speed + coeff_calorie_1)
                          * coeff_calorie_2 * self.weight)
        return spent_calories

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return mean_speed


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workouts = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return workouts[workout_type](workout_type, *data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.show_info_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
