import unittest
import Experiment__


class RunnerTest(unittest.TestCase):
    def test_walk(self, name='Marat'):
        name = Experiment__.Runner(name)
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self, name='Mark'):
        name = Experiment__.Runner(name)
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    def test_challenge(self, name='Marat',name_ = 'Mark'):
        name = Experiment__.Runner(name)
        name_ = Experiment__.Runner(name_)
        for i in range(10):
            name.walk()
            name_.run()
        self.assertNotEqual(name.distance, name_.distance)


if __name__ == '__main__':
    unittest.main()
