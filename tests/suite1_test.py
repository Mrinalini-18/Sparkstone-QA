import unittest
from tests.home.addwishlist_test import AddWishlist
from tests.home.createopp_test import CreateOpp

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(AddWishlist)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CreateOpp)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)