from aws.athena_query import AthenaQuery
from dotenv import load_dotenv

load_dotenv()

print('Executing second query set')

result_key = 'test_result'
query = AthenaQuery(
    db='ksgmet-test',
    sql='SELECT count(*) FROM test',
    output_key=result_key)

query.execute_and_wait_for_result()
