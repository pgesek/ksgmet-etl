import boto3
import time

WAIT = 10


class AthenaQuery:

    VAR_CHAR_VAL = 'VarCharValue'

    def __init__(self, db, sql, output_key):
        self.db = db
        self.sql = sql
        self.output_key = output_key

        self.client = boto3.client('athena')
        self.query_id = None
        self.result_received = False
        self.result = None

    def execute_and_wait_for_result(self):
        self.execute()
        self.wait_to_complete()
        return self.retrieve_result()

    def execute(self):
        print('Executing: ' + self.sql)

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
        if self.result_received:
            return self.result

        if self.query_id is None:
            raise Exception("Cannot retrieve results for query that has not executed")

        response = self.client.get_query_results(
            QueryExecutionId=self.query_id
        )

        print('Response: ' + str(response))

        self.result_received = True
        self.result = self.parse_result(response)

        return self.result

    def get_downloaded_result(self):
        if self.result_received:
            return self.result
        else:
            raise Exception('No result downloaded for this query')

    @staticmethod
    def parse_result(response):
        rows = response['ResultSet']['Rows']

        header_list = rows[0]['Data']
        headers = [header_dict[AthenaQuery.VAR_CHAR_VAL] for header_dict in header_list]

        data_rows = rows[1:]

        result = []
        for data_row in data_rows:

            data_list = data_row['Data']
            values = [value_dict.get(AthenaQuery.VAR_CHAR_VAL, '') for value_dict in data_list]

            result_row = dict()
            for i in range(len(headers)):
                header = headers[i]
                value = values[i]

                result_row[header] = value

            result.append(result_row)

        return result

    @staticmethod
    def extract_varchar_values(rows):
        return [[dictionary.get('VarCharValue', '') for dictionary in row]
                for row in rows]
