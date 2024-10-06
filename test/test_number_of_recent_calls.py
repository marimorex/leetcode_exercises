import unittest

from queues.number_of_recent_calls import RecentCounter


class TestNumberOfRecentCalls(unittest.TestCase):
    def test_single_request(self):
        recent_counter = RecentCounter()
        self.assertEqual(recent_counter.ping(1), 1)  # First request, should return 1

    def test_multiple_requests_within_range(self):
        recent_counter = RecentCounter()
        self.assertEqual(recent_counter.ping(1), 1)  # First request
        self.assertEqual(recent_counter.ping(100), 2)  # Second request within range
        self.assertEqual(
            recent_counter.ping(3001), 3
        )  # Third request still within 3000ms window

    def test_requests_expiring(self):
        recent_counter = RecentCounter()
        self.assertEqual(recent_counter.ping(1), 1)  # First request
        self.assertEqual(recent_counter.ping(100), 2)  # Second request
        self.assertEqual(recent_counter.ping(3001), 3)  # Third request
        self.assertEqual(recent_counter.ping(3002), 3)  # Still 3 within range
        self.assertEqual(
            recent_counter.ping(6001), 3
        )  # The first request expired, so only 2 remain

    def test_all_requests_expire(self):
        recent_counter = RecentCounter()
        self.assertEqual(recent_counter.ping(1), 1)  # First request
        self.assertEqual(recent_counter.ping(3000), 2)  # Second request
        self.assertEqual(
            recent_counter.ping(6001), 1
        )  # The first request expired, so only 1 remains
