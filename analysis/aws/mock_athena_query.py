
class MockAthenaQuery:
    counter = 0

    def __init__(self, db, sql, output_key):
        self.db = db
        self.sql = sql
        self.output_key = output_key

    def execute_and_wait_for_results(self):
        self.execute()
        return self.retrieve_result()

    def execute(self):
        print('Executing SQL: ' + self.sql)

    def wait_to_complete(self):
        return

    def retrieve_result(self):
        return dict()

    def get_downloaded_result(self):
        return self.retrieve_result()
