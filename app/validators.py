from app.errors import error_value_int_error, error_value_float_error

class ChatValidator:
    @staticmethod
    def validate_non_negative_number(value, attribute_name):
        """Валидация: неотрицательное число."""
        v = error_value_float_error(value, attribute_name)
        if isinstance(v, (int, float)) and v >= 0:
            return v
        else:
            raise ValueError(
                f"{attribute_name} должно быть неотрицательным числом.")

    @staticmethod
    def validate_positive_integer(value, attribute_name):
        """Валидация: положительное целое число."""
        v = error_value_int_error(value, attribute_name)
        if isinstance(v, int) and v > 0:
            return v
        else:
            raise ValueError(
                f"{attribute_name} должно быть положительным целым числом.")

    @staticmethod
    def validate_type_integer(value, attribute_name):
        """Валидация: число"""
        v = error_value_int_error(value, attribute_name)
        if isinstance(v, int):
            return v
        else:
            raise ValueError(f"{attribute_name} должно быть числом")
