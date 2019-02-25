import unittest
import requests


class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5005/fib"

    def test_fib(self):
        """ Test /fib/<nth> for all known lists"""
        for number, response in GOOD_RESPONSES.iteritems():
            reply = requests.get("{}/{}".format(self.url, number))
            actual_reply = reply.json()

            self.assertEqual(len(actual_reply), len(response),
                             "Got {} number but expected {}".format(
                                 len(actual_reply), len(response)
                             ))

            # Use set because the order doesn't matter
            self.assertEqual(set(actual_reply), set(response),
                             "Got {} but expected {}".format(
                                 actual_reply, response))

    def test_fib_negative(self):
        """ Test /fib/<nth> for non-existent users"""
        invalid_number = "-1"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_number))
        self.assertEqual(actual_reply.status_code, 400)

    def test_fib_string(self):
        """ Test /fib/<nth> for non-existent users"""
        invalid_string = "non-digit"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_string))
        self.assertEqual(actual_reply.status_code, 400)


GOOD_RESPONSES = {0: [], 1: [0], 2: [0, 1], 3: [0, 1, 1]}

if __name__ == "__main__":
    unittest.main()
