import unittest
from io import StringIO
from unittest.mock import patch
from snippets_oo import Car, process_the_data, get_the_data, start_the_engine

class TestCarClass(unittest.TestCase):
    def test_car_initialization(self):
        car = Car("Tesla", "2023", "Model Y", "517000", "22500")
        self.assertEqual(car.make, "Tesla")
        self.assertEqual(car.year, "2023")
        self.assertEqual(car.model, "Model Y")
        self.assertEqual(car.price, "517000")
        self.assertEqual(car.milage, "22500")

    def test_display_info(self):
        car = Car("Tesla", "2023", "Model Y", "517000", "22500")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            car.display_info()
            self.assertEqual(fake_out.getvalue().strip(), "2023 Tesla Model Y 22500")

    def test_update_model(self):
        car = Car("Tesla", "2023", "Model Y", "517000", "22500")
        car.update_model("30000")
        self.assertEqual(car.milage, "30000")

class TestProcessTheData(unittest.TestCase):
    def test_process_the_data(self):
        data = "Tesla,2023,Model Y,517000,22500"
        car = process_the_data(data)
        self.assertIsInstance(car, Car)
        self.assertEqual(car.make, "Tesla")
        self.assertEqual(car.year, "2023")
        self.assertEqual(car.model, "Model Y")
        self.assertEqual(car.price, "517000")
        self.assertEqual(car.milage, "22500")

class TestGetTheData(unittest.TestCase):
    @patch('builtins.open')
    def test_get_the_data(self, mock_open):
        mock_open.return_value.__enter__.return_value = StringIO("Tesla,2023,Model Y,517000,22500\nFord,2022,Mustang,450000,15000")
        data = get_the_data()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], "Tesla,2023,Model Y,517000,22500")
        self.assertEqual(data[1], "Ford,2022,Mustang,450000,15000")

class TestStartTheEngine(unittest.TestCase):
    @patch('snippets_oo.get_the_data')
    @patch('sys.stdout', new_callable=StringIO)
    def test_start_the_engine(self, mock_stdout, mock_get_data):
        mock_get_data.return_value = ["Tesla,2023,Model Y,517000,22500", "Ford,2022,Mustang,450000,15000"]
        start_the_engine()
        output = mock_stdout.getvalue()
        self.assertIn("2023 Tesla Model Y 22500", output)
        self.assertIn("2022 Ford Mustang 15000", output)
        self.assertIn("number of cars:  2", output)
        self.assertIn("we have updated the milage on one of the cars", output)
        self.assertIn("2022 Ford Mustang 99999", output)

if __name__ == '__main__':
    unittest.main()