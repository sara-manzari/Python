class Weapon:

    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value


class Gun(Weapon):

    def __init__(self, name, n_bullets):
        super().__init__(name)
        self.set_n_bullets(n_bullets)

    def get_n_bullets(self):
        return self._n_bullets

    def set_n_bullets(self, value):
        self._n_bullets = value
