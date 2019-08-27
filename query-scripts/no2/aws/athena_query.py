import boto3
import time

WAIT = 10


class AthenaQuery:
    def __init__(self, db, sql, output_key):
        self.db = db
        self.sql = sql
        self.output_key = output_key

        self.client = boto3.client('athena')
        self.query_id = None

    def execute_and_wait_for_result(self):
        self.execute()
        self.wait_to_complete()
        return self.retrieve_result()

    def execute(self):
        response = self.client.start_query_execution(
            QueryString=self.sql,
            QueryExecutionContext={
                'Database': self.db
            },
            ResultConfiguration={
                'OutputLocation': 's3://ksgmet-query-results/' + self.output_key
            }
        )

        self.query_id = response['QueryExecutionId']

    def wait_to_complete(self):

        print('Waiting for query to complete: ' + self.query_id)

        finished = False
        while not finished:
            time.sleep(WAIT)

            response = self.client.get_query_execution(
                QueryExecutionId=self.query_id
            )

            print(response)
            query_execution = response['QueryExecution']
            status = query_execution['Status']

            state = status['State']

            if state == 'FAILED' or state == 'CANCELLED':
                raise Exception('Query execution failed: ' +
                                status['StateChangeReason'])
            elif state == 'SUCCEEDED':
                finished = True

    def retrieve_result(self):
        if self.query_id is None:
            raise Exception("Cannot retrieve results for query that has not executed")

        response = self.client.get_query_results(
            QueryExecutionId=self.query_id
        )

        print(response)

        rows = response['ResultSet']['Rows']
        parsed_rows = [row['Data']['VarCharValue'] for row in rows[1:]]

        return parsed_rows
