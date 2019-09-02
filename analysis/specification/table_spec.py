from .field_keys import map_keys


class TableSpec:
    def __init__(self, field):
        self.field = field

    def write_to_doc(
            self,
            doc,
            hour_spec_list,
            results,
            img_dir,
            include_maps):
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

        if include_maps:
            for key in map_keys(self.field):
                img_path = img_dir + '\\' + key + '.png'

                doc.write_image(img_path)
