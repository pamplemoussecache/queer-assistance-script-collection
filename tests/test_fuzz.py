import unittest

import complaints_generator


FUZZ_ITERATIONS = 100

class FuzzTest(unittest.TestCase):
    def test_complaints_generator(self):
        s = set()
        for i in range(FUZZ_ITERATIONS):
            s.add(complaints_generator.Complaint())

        assert len(s) > 50
