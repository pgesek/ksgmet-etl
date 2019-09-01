class TableSpec:
    def __init__(self, field):
        self.field = field

    def write_to_doc(self, doc, hour_spec_list, results):
        data = dict([
            ('title', 'Pole: ' + self.field),
            ('col_headers', hour_spec_list.header_list()),
            ('row_headers', [
                'Rodzaj prognozy',
                'Ilość analizowanych prognoz',
                'Średnia różnica',
                'Średnia różnica wartości bezwzględnych',
                'Odchylenie standardowe'
            ]),
            ('content', results)
        ])

        doc.write_table(data)

    @staticmethod
    def _transpose(array):
        return [[r[col] for r in array] for col in range(len(array[0]))]