import unittest
import requests
from nanoleaf import Nanoleaf

class TestNanoleafMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # INSERT YOUR OWN VALUES HERE
        ip = ''
        auth_token = ''
        self.nl = Nanoleaf(ip, auth_token, True)

    def test_power_on(self):
        self.assertTrue(self.nl.power_on())

    def test_power_off(self):
        self.assertTrue(self.nl.power_off())

    def test_toggle_power(self):
        self.assertTrue(self.nl.toggle_power())

    def test_set_color(self):
        self.assertTrue(self.nl.set_color((255, 255, 255)))
        self.assertFalse(self.nl.set_color((255, 255, 276)))
        self.assertFalse(self.nl.set_color((255, 255, -234)))

    def test_set_brightness(self):
        self.assertTrue(self.nl.set_brightness(100))
        with self.assertRaises(ValueError):
            self.nl.set_brightness(-10)

    def test_increment_brightness(self):
        self.assertTrue(self.nl.increment_brightness(10))
        self.assertTrue(self.nl.increment_brightness(-20))
        self.assertTrue(self.nl.increment_brightness(200))
        self.assertTrue(self.nl.increment_brightness(-300))

    def test_identify(self):
        self.assertTrue(self.nl.identify())

    def test_set_hue(self):
        self.assertTrue(self.nl.set_hue(100))
        with self.assertRaises(ValueError):
            self.nl.set_hue(-10)

    def test_increment_hue(self):
        self.assertTrue(self.nl.increment_hue(10))
        self.assertTrue(self.nl.increment_hue(-20))
        self.assertTrue(self.nl.increment_hue(200))
        self.assertTrue(self.nl.increment_hue(-300))

    def test_set_saturation(self):
        self.assertTrue(self.nl.set_saturation(100))
        with self.assertRaises(ValueError):
            self.nl.set_saturation(-10)

    def test_increment_saturation(self):
        self.assertTrue(self.nl.increment_saturation(10))
        self.assertTrue(self.nl.increment_saturation(-20))
        self.assertTrue(self.nl.increment_saturation(200))
        self.assertTrue(self.nl.increment_saturation(-300))

    def test_set_color_temp(self):
        self.assertTrue(self.nl.set_color_temp(6500))
        with self.assertRaises(ValueError):
            self.nl.set_color_temp(1100)

    def increment_color_temp(self):
        self.assertTrue(self.nl.increment_color_temp(10))
        self.assertTrue(self.nl.increment_color_temp(-20))
        self.assertTrue(self.nl.increment_color_temp(200))
        self.assertTrue(self.nl.increment_color_temp(-300))

    def test_set_effect(self):
        self.assertTrue(self.nl.set_effect('Color Burst'))
        self.assertFalse(self.nl.set_effect('non-existent-effect'))

    def test_get_panel_info(self):
        self.assertTrue(self.nl.get_panel_info())

    def test_get_power(self):
        self.assertTrue(str(self.nl.get_power()))

    def test_get_brightness(self):
        self.assertTrue(self.nl.get_brightness())

    def test_get_hue(self):
        self.assertTrue(self.nl.get_hue())

    def test_get_saturation(self):
        self.assertTrue(self.nl.get_saturation())

    def test_get_color_temp(self):
        self.assertTrue(self.nl.get_color_temp())

    def test_get_color_mode(self):
        self.assertTrue(self.nl.get_color_mode())

    def test_get_current_effect(self):
        self.assertTrue(self.nl.get_current_effect())

    def test_list_effects(self):
        self.assertTrue(self.nl.list_effects())

    def test_effect_exists(self):
        self.assertTrue(self.nl.effect_exists('Color Burst'))
        self.assertFalse(self.nl.effect_exists('non-existent-effect'))

    def test_get_layout(self):
        self.assertTrue(self.nl.get_layout())

    def __helper_function(self, dictionary):
        self.assertTrue(True)

    def test_register_event(self):
        with self.assertRaises(Exception):
            register_event(self.__helper_function, [5])
        with self.assertRaises(Exception):
            register_event(self.__helper_function, [1, 2, 3, 3, 4])
        self.nl.register_event(self.__helper_function, [1])
        self.nl.toggle_power()
