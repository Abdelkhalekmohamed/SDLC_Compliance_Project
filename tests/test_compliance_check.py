import os
import subprocess
import unittest

class TestComplianceCheck(unittest.TestCase):

    def setUp(self):
        # Ensure the data directory is clean before each test
        if os.path.exists('data/compliance_report.csv'):
            os.remove('data/compliance_report.csv')

    def test_compliance_check(self):
        result = subprocess.run(['python', 'compliance_check.py'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Compliance check failed: {result.stderr}")
        self.assertTrue(os.path.exists('data/compliance_report.csv'), "Compliance report not generated")

if __name__ == '__main__':
    unittest.main()
