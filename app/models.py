from app.validators import ChatValidator

class Chat:
    def __init__(self, chat_id):
        self._id = None
        self._amount = 0
        self._plan = None
        self._nal = 0
        self._beznal = 0
        self._vozvrat = 0
        self._schet = 0
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
        self._amount = ChatValidator.validate_non_negative_number(
            value, "Общая выручка")

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

    @property
    def schet(self):
        return self._schet

    @schet.setter
    def schet(self, value):
        self._schet = ChatValidator.validate_non_negative_number(
            value, "Оплаты по счетам"
        )
        self._calculate_amount()

    @property
    def vozvrat(self):
        return self._vozvrat

    @vozvrat.setter
    def vozvrat(self, value):
        self._vozvrat = ChatValidator.validate_non_negative_number(
            value, "Возвраты"
        )
        self._calculate_amount()

    def _calculate_amount(self):
        if self._nal is not None and self._beznal is not None and self._schet is not None and self._vozvrat is not None:
            self.amount = self._nal + self._beznal + self._schet - self._vozvrat

    def set_new_plan(self, new_plan):
        self.plan = ChatValidator.validate_type_integer(new_plan, "План")
        return new_plan

    def reset_values(self, reset_plan: bool=False):
        self._nal = 0
        self._beznal = 0
        self._schet = 0
        self._vozvrat = 0
        self._amount = 0
        if reset_plan:
            self._plan = None
            
    def get_plan(self):
        if self._plan is None:
            return "План не установлен."
        diff_plan = self.plan - self.amount
        sign = self._get_sign(diff_plan)
        # reply = "Наличные: {}\nБезнал: {}\nПо счету: {}\nВозвраты: {}\nВсего: {} \nПо плану: {}{}".format(self.nal if self.nal is not None and self.nal > 0 else "-",
        #                                                                                                   self.beznal if self.beznal is not None and self.beznal > 0 else "-",
        #                                                                                                   self.schet if self.schet is not None and self.schet > 0 else "-",
        #                                                                                                   self.vozvrat if self.vozvrat is not None and self.vozvrat > 0 else "-",
        #                                                                                                   self.amount, sign, abs(diff_plan))
        reply = f"{self.amount}\n{sign}{abs(diff_plan)}"
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
