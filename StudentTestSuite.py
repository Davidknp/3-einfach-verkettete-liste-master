import unittest
import solution

class StudentTestSuite(unittest.TestCase):
	def setUp(self):
		self.os1 = solution.OperatingSystem("Unics", 1969)
		self.os2 = solution.OperatingSystem("Windows 95", 1995)
		self.os3 = solution.OperatingSystem("Mac OS X", 2000)
		self.timeline = solution.OSTimeline()
		self.timeline.head = self.os1
		self.timeline.head.next = self.os2
		self.os2.next = self.os3

	def testExample1(self):
		self.assertTrue(self.timeline.insert("Linux 0.1", 1990))
		self.assertEqual(self.timeline.traverse(), [("Unics", 1969), ("Linux 0.1", 1990), ("Windows 95", 1995), ("Mac OS X", 2000)])

	def testExample2(self):
		self.assertFalse(self.timeline.insert("Red Hat Linux 6.2E",2000))

	def testInsertCase1(self):
		self.assertTrue(self.timeline.insert("IBSYS", 1960))
		self.assertEqual(self.timeline.traverse(), [("IBSYS", 1960), ("Unics", 1969), ("Windows 95", 1995), ("Mac OS X", 2000)])

	def testInsertCase2(self):
		self.assertTrue(self.timeline.insert("Windows 98", 1998))
		self.assertEqual(self.timeline.traverse(), [("Unics", 1969), ("Windows 95", 1995), ("Windows 98", 1998), ("Mac OS X", 2000)])

	def testInsertCase3(self):
		self.assertTrue(self.timeline.insert("macOS Catalina", 2019))
		self.assertEqual(self.timeline.traverse(), [("Unics", 1969), ("Windows 95", 1995), ("Mac OS X", 2000), ("macOS Catalina", 2019)])
