import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

input_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'sparql-queries.json'))
output_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'sparql-queries-parsed.json'))


from sqparser import SQParser
import json

class TestSQParserMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_json(self):
        target_component = None
        has_title = True
        SQParser.parse_sq_json(input_, output_path=output_, target_component=target_component, has_title=has_title)

    def test_parse(self):
        text = "PREFIX qpr: <http://istresearch.com/qpr> SELECT ?business  (count(?ad) AS ?count)(group_concat(?ad;separator=',') AS ?ads) WHERE { ?ad a qpr:Ad ; qpr:location 'Vermont' ; qpr: business_type ?bt . FILTER(?bt = 'Spa' || ?bt = 'Massage Parlor') ?ad qpr:services 'sex' . OPTIONAL { ?ad qpr:business_name ?business_name} OPTIONAL { ?ad qpr:physical_address ?physical_address } BIND( IF(BOUND(?business_name) && BOUND(?physical_address), CONCAT(?business_name, \",\", ?physical_address), IF(BOUND(?business_name), ?business_name, ?physical_address)) AS ?business) } GROUP BY ?business ORDER BY DESC(?count) LIMIT 1"
        print json.dumps(SQParser.parse(text), indent=4)

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestSQParserMethods('test_parse_json'))
        # suite.addTest(TestSQParserMethods('test_parse'))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



