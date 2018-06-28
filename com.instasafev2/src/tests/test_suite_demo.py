import unittest
from tests.login_tests import LoginTests
# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)