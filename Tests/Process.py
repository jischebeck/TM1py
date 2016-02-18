from TM1py import TM1Queries, Process
import uuid
import unittest


class TestAnnotationMethods(unittest.TestCase):
    q = TM1Queries(ip='', port=8008, user='admin', password='apple', ssl=True)
    random_string = str(uuid.uuid4()).replace('-', '_')

    # none process
    p_none = Process(name='unittest_none_' + random_string, datasource_type='None')

    # ascii process
    p_ascii = Process(name='unittest_ascii_' + random_string, datasource_type='ASCII',
                      datasource_ascii_delimiter_type='Character',
                      datasource_ascii_delimiter_char=',',
                      datasource_ascii_header_records=2,
                      datasource_ascii_quote_character='^',
                      datasource_ascii_thousand_separator='~',
                      prolog_procedure=Process.auto_generated_string() + ' test prolog procedure',
                      metadata_procedure=Process.auto_generated_string() + ' test metadata procedure',
                      data_procedure=Process.auto_generated_string() + ' test data procedure',
                      epilog_procedure=Process.auto_generated_string() + ' test epilog procedure',
                      datasource_data_source_name_for_server='C:\Data\simple_csv.csv',
                      datasource_data_source_name_for_client='C:\Data\simple_csv.csv')
    # variables
    p_ascii.add_variable('v_1', 'Numeric')
    p_ascii.add_variable('v_2', 'Numeric')
    p_ascii.add_variable('v_3', 'Numeric')
    p_ascii.add_variable('v_4', 'Numeric')
    # parameters
    p_ascii.add_parameter('p_Year', 'year?', '2016')

    # view process
    p_view = Process(name='unittest_view_' + random_string, datasource_type='TM1CubeView', datasource_view='view1',
                     datasource_data_source_name_for_client='Plan_BudgetPlan',
                     datasource_data_source_name_for_server='Plan_BudgetPlan')

    # odbc process
    p_odbc = Process(name='unittest_odbc_' + random_string, datasource_type='ODBC', datasource_password='password',
                     datasource_user_name='user')

    # create Process
    def test1_create_process(self):
        self.q.create_process(self.p_none)
        self.q.create_process(self.p_ascii)
        self.q.create_process(self.p_view)
        self.q.create_process(self.p_odbc)

    # get Process
    def test2_get_process(self):
        p1 = self.q.get_process(self.p_ascii.name)
        self.assertEqual(p1.body, self.p_ascii.body)
        p2 = self.q.get_process(self.p_none.name)
        self.assertEqual(p2.body, self.p_none.body)
        p3 = self.q.get_process(self.p_view.name)
        self.assertEqual(p3.body, self.p_view.body)
        p4 = self.q.get_process(self.p_odbc.name)
        p4.datasource_password = None
        self.p_odbc.datasource_password = None
        self.assertEqual(p4.body, self.p_odbc.body)

    # update process
    def test3_update_process(self):
        # get
        p = self.q.get_process(self.p_ascii.name)
        # modify
        p.set_data_procedure(Process.auto_generated_string() + "x = 'Hi this is a test';")
        # update on Server
        self.q.update_process(p)
        # get again
        p_ascii_updated = self.q.get_process(p.name)
        # assert
        self.assertNotEqual(p_ascii_updated.data_procedure, self.p_ascii.data_procedure)

    # delete process
    def test4_delete_process(self):
        self.q.delete_process(self.p_none.name)
        self.q.delete_process(self.p_ascii.name)
        self.q.delete_process(self.p_view.name)
        self.q.delete_process(self.p_odbc.name)

    def test5_logout(self):
        self.q.logout()


if __name__ == '__main__':
    unittest.main()