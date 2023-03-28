#import parser
import sprint1_cases_3_4 as parser
from unittest import TestCase


class test_birth_before_death(TestCase):
    def test_birth_before_death1(self):

        #individuals, _ = gedcom_parser(acceptfile)
        acceptfile="test_data.ged"
        self.assertTrue(parser.birth_before_death(acceptfile))

    def test_birth_before_death2(self):
        acceptfile="test_data.ged"
        #individuals, _ = gedcom_parser(acceptfile)
        self.assertEqual(parser.birth_before_death(acceptfile),True)

    def test_birth_before_death3(self):
        acceptfile="test_data.ged"
        #individuals, _ = gedcom_parser(acceptfile)
        self.assertIsNot(parser.birth_before_death(acceptfile),False)

    def test_birth_before_death4(self):
        acceptfile="test_data.ged"
        #individuals, _ = gedcom_parser(acceptfile)
        self.assertIsNotNone(parser.birth_before_death(acceptfile))

    def test_birth_before_death5(self):
        acceptfile="test_data.ged"
        #individuals, _ = gedcom_parser(acceptfile)
        self.assertIs(parser.birth_before_death(acceptfile),True)