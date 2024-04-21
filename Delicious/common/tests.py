# custom_test_runner.py

from django.test.runner import DiscoverRunner


class CustomTestRunner(DiscoverRunner):
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        # Your custom implementation here
        pass
