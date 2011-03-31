import unittest

def problema_para_resolver():
    return True

class ProblemaParaResolverTest(unittest.TestCase):
    def test_simples(self):
        self.assertEqual(True, problema_para_resolver())

if __name__ == '__main__':
    unittest.main()
