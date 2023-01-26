import unittest
import unittestreport

suite = unittest.defaultTestLoader.discover(".", pattern="Test*")

runner = unittestreport.TestRunner(suite=suite)
runner.run()
