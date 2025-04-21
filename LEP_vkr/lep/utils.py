from math import pi, sqrt
from numpy import roots, isreal, real


class LepCalculator:
    def __init__(self, city, wire, span_length):
        self.city = city
        self.t_min = self.city.min_temp
        self.t_max = self.city.max_temp
        self.t_avg = self.city.avg_year_temp
        self.e = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30, 6: 35}.get(self.city.ice_zone)
        self.q = {1: 400, 2: 500, 3: 650, 4: 800, 5: 1000, 6: 1250}.get(self.city.wind_zone) / 9.80665
        self.wire = wire
        self.F0 = self.wire.gen_cross_sec
        self.d = self.wire.diametr
        self.p = self.wire.weight
        self.a0 = self.wire.coef_lin_exp * 10**-6
        self.E0 = self.wire.mod_elast_mat
        self.o_r = self.wire.max_vol
        self.o_h = self.o_r
        self.o_c = self.wire.avg_vol
        self.l = span_length
        self.q0 = 0.9
        self.Cx = 1.2 if self.d < 20 else 1.1
        self.t_led = -5
        self.t_c = 15

    def y4_func(self):
        interpolation_table = {
            200: 1.0,
            240: 0.94,
            280: 0.88,
            300: 0.85,
            320: 0.83,
            360: 0.80,
            400: 0.76,
            500: 0.71,
            580: 0.70
        }

        q_pa = self.q * 9.80665

        keys = list(interpolation_table.keys())
        X1 = None
        X2 = None
        for i in range(len(keys)):
            if q_pa <= keys[i]:
                X1 = keys[i - 1]
                X2 = keys[i]
                break
        else:
            X1 = keys[-2]
            X2 = keys[-1]

        f_X1 = interpolation_table[X1]
        f_X2 = interpolation_table[X2]

        a = f_X1 + (((f_X2 - f_X1) * (q_pa - X1)) / (X2 - X1))

        return round(a * self.Cx * self.q * self.d, 2)

    def lnk_func(self, o_n, o_t, y_n, y1, t_n, t_m):
        numerator = (o_n - o_t) + self.a0 * self.E0 * (t_n - t_m)
        denominator = ((y_n ** 2 * self.E0) / (24 * o_n ** 2)) - ((y1 ** 2 * self.E0) / (24 * o_t ** 2))

        return int(sqrt(abs(numerator) / denominator) * 1000)

        # numerator = 6 * ((o_n - o_t) * (1 / self.E0) + 19.2 * (t_n - t_m))
        # denominator = (y_n / y1)**2 - (o_n / o_t)**2
        #
        # return ((2 * o_n) / y1) * sqrt(numerator/denominator)

    def clim_func(self, y_n, y_m, t_n, t_m):
        A = (self.l**2 * (y_n * 10**-3)**2 * self.E0) / 24
        B = self.o_r - (self.l ** 2 * (y_m * 10 ** -3) ** 2 * self.E0) / (24 * self.o_r ** 2) - self.a0 * self.E0 * (t_n - t_m)

        coefficients = [1, -B, 0, -A]
        roots_ = roots(coefficients)
        real_roots = [root for root in roots_ if isreal(root)]

        return round(float(max(real(real_roots))), 2)

    def f(self, y, o):
        return round(((self.l ** 2 * y) / (8 * o)) / 1000, 2)

    def calculate_all(self):
        y1 = round(self.p / self.F0, 2)
        y2 = round((pi * self.q0 * (self.e / 10) * ((self.d / 10) + (self.e / 10))) / self.F0, 2)
        y3 = y1 + y2
        y4 = self.y4_func()
        y5 = round((self.Cx * self.q * (self.d + self.e)) / self.F0, 2)
        y6 = round(sqrt(y4**2 + y1**2), 2)
        y7 = round(sqrt(y3**2 + y5**2), 2)

        l1k = self.lnk_func(self.o_c, self.o_h, y1, y1, self.t_avg, self.t_min)
        l2k = self.lnk_func(self.o_r, self.o_h, y7, y1, self.t_led, self.t_min)
        l3k = self.lnk_func(self.o_r, self.o_c, y7, y1, self.t_led, self.t_led)

        if self.l < l2k:
            if l1k < l2k:
                y_calc = y1
                t_calc = self.t_min
            else:
                y_calc = y7
                t_calc = self.t_led
        else:
            if self.l < l3k:
                y_calc = y1
                t_calc = self.t_avg
            else:
                y_calc = y7
                t_calc = self.t_led

        clim_1 = self.clim_func(y7, y_calc, self.t_led, t_calc)
        clim_2 = self.clim_func(y3, y_calc, self.t_led, t_calc)
        clim_3 = self.clim_func(y6, y_calc, self.t_avg, t_calc)
        clim_4 = self.clim_func(y1, y_calc, self.t_avg, t_calc)
        clim_5 = self.clim_func(y1, y_calc, self.t_c, t_calc)
        clim_6 = self.clim_func(y1, y_calc, self.t_min, t_calc)
        clim_7 = self.clim_func(y1, y_calc, self.t_max, t_calc)

        f_all = {
            self.f(y7, clim_1): ('I', 'провода покрыты гололёдом'),
            self.f(y3, clim_2): ('II', 'провода покрыты гололёдом, ветра нет'),
            self.f(y6, clim_3): ('III', f'скоростной напор – {self.q:.2f} кг/см^3; при -5ºС; гололёда нет'),
            self.f(y1, clim_4): ('IV', 'гололёда и ветра нет; среднегодовая температура: 5ºС'),
            self.f(y1, clim_5): ('V', '15ºС, ветра и гололёда нет'),
            self.f(y1, clim_6): ('VI', f'{self.t_min} режим низшей температуры; ветра и гололёда нет'),
            self.f(y1, clim_7): ('VII', f'{self.t_max} режим высшей температуры; ветра и гололёда нет')
        }

        f_max_key = max(f_all)
        f_max_value = f_all[f_max_key]

        return f_max_value[0], f_max_value[1], f_max_key


class LepCalculatorManual(LepCalculator):
    def __init__(self, t_min, t_max, t_avg, e, q, span_length, F0, diameter, weight, a0, E0, o_r, o_c):
        self.t_min = t_min
        self.t_max = t_max
        self.t_avg = t_avg
        self.e = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30, 6: 35}.get(e)
        self.q = {1: 400, 2: 500, 3: 650, 4: 800, 5: 1000, 6: 1250}.get(q) / 9.80665
        self.l = span_length
        self.F0 = F0
        self.d = diameter
        self.p = weight
        self.a0 = a0
        self.E0 = E0
        self.o_r = o_r
        self.o_h = self.o_r
        self.o_c = o_c
        self.q0 = 0.9
        self.Cx = 1.2 if self.d < 20 else 1.1
        self.t_led = -5
        self.t_c = 15