import unittest

from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests
from tests.home.login_tests import LoginTests


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_Login)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)