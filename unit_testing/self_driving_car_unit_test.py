from self_driving_car import  SelfDrivingCar
from unittest import TestCase


class SelfDrivingCarTest(TestCase):
    def setUp(self):
        self.car = SelfDrivingCar()

    def test_stop(self):
        self.speed = 5
        self.car.stop()

    # Verify the speed is 0 after stopping
        self.assertEquals(1, self.car.speed)


if __name__ == '__main__':
    TestCase.main()
