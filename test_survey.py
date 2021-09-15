import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """test for AnonymousSurvey class."""

    def test_store_single_response(self):
        """Checking if single answer is correctly stored."""
        question = "What is your native language?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('english')
        self.assertIn('english', my_survey.responses)


if __name__ == '__main__':
    unittest.main()
