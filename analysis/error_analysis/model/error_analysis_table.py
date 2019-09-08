from uuid import uuid4


class ErrorAnalysisTable:
    def __init__(self, field):
        self.field = field

    def execute_and_write(self, analysis_fields, sql_builder, athena_builder, xlsx_doc):
        sql_builder\
            .fields([field.to_sql_field(self.field) for field in analysis_fields])\
            .group_by('ABS({}_delta) > 2.0'.format(self.field)) \
            .order_by('ABS({}_delta) > 2.0 ASC'.format(self.field))

        athena_query = athena_builder.build(
            sql=sql_builder.build(),
            output_key=str(uuid4())
        )

        result = athena_query.execute_and_wait_for_result()

        content = []
        for row in result:
            content_row = []

            for field in analysis_fields:
                content_row.append(row.get(field.get_alias(self.field), 0))

            content.append(content_row)

        data = dict([
            ('title', 'Pole: ' + self.field),
            ('col_headers', [field.header for field in analysis_fields]),
            ('row_headers', ['Wartość', 'Błąd < 2.0', 'Błąd > 2.0']),
            ('content', content)
        ])

        xlsx_doc.write_table(data)
