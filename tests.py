from solution import transitive_dependencies
import unittest

class Tests(unittest.TestCase):
    def test_should_not_contain_itself(self):
        self.assertFalse("A" in transitive_dependencies([["A", "B"], ["B", "A"]])["A"])
    def test_should_contain_all_elements(self):
        self.assertEqual({"B", "C"}, transitive_dependencies([["A", "B", "C"]])["A"])
    def test_should_contain_all_keys(self):
        self.assertEqual({"A", "B", "C"}, transitive_dependencies([["A"], ["B"], ["C"]]).keys())
    def test_should_contain_transitive_dependency(self):
        self.assertTrue("C" in transitive_dependencies([["A", "B"], ["B", "C"]])["A"])
    def test_should_contain_chained_dependencies(self):
        self.assertEqual({"B", "C","D"},transitive_dependencies([["A", "B"], ["B", "C"], ["C", "D"]])["A"])
    def test_should_give_transitive_dependencies(self):
        self.assertEqual({"A":{"B","C", "D"}, "B":{"C", "D"}, "C":{"D"}, "D":set()},transitive_dependencies([["A", "B"], ["B", "C"], ["C", "D"]]))
    def test_should_solve_the_exercise(self):
        self.assertEqual({"A": {"B", "C", "E", "F", "G", "H"}, "B": {"C", "E", "F", "G", "H"}, "C":{"G"}, "D":{"A", "B", "C", "E", "F", "G", "H"}, "E":{"F", "H"},"F":{"H"}, "G":set(), "H":set()}, transitive_dependencies([["A","B","C"], ["B", "C", "E"], ["C","G"],["D","A","F"], ["E", "F"],["F","H"]]))
if __name__ == '__main__':
    unittest.main()