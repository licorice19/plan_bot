from app.validators import ChatValidator


class Chat:
    def __init__(self, chat_id):
        self._id = None
        self._amount = 0
        self._plan = None
        self._nal = None
        self._beznal = None
        self.id = chat_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = ChatValidator.validate_type_integer(value, "ID чата")

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = ChatValidator.validate_non_negative_number(value, "Общая выручка")
        self._beznal = None
        self._nal = None

    @property
    def plan(self):
        return self._plan

    @plan.setter
    def plan(self, value):
        self._plan = ChatValidator.validate_non_negative_number(value, "План")

    @property
    def nal(self):
        return self._nal

    @nal.setter
    def nal(self, value):
        self._nal = ChatValidator.validate_non_negative_number(
            value, "Сумма наличных")
        self._calculate_amount()

    @property
    def beznal(self):
        return self._beznal

    @beznal.setter
    def beznal(self, value):
        self._beznal = ChatValidator.validate_non_negative_number(
            value, "Сумма безналичных")
        self._calculate_amount()

    def _calculate_amount(self):
        if self._nal is not None and self._beznal is not None:
            self._amount = self._nal + self._beznal

    def set_new_plan(self, new_plan):
        self.plan = ChatValidator.validate_type_integer(new_plan, "План")
        return new_plan

    def get_plan(self):
        if self._plan is None:
            return "План не установлен."
        diff_plan = self.plan - self.amount
        sign = self._get_sign(diff_plan)
        reply = "Наличные: {}\nБезнал: {}\nВсего: {} \nПо плану: {}{}".format(self.nal if self.nal is not None else "-",
                                                                             self.beznal if self.beznal is not None else "-",
                                                                             self.amount, sign, abs(diff_plan))
        return reply

    def _get_sign(self, diff):
        if diff > 0:
            return "-"
        elif diff == 0:
            return ""
        else:
            return "+"


class User:
    pass
