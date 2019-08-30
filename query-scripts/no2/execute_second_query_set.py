from specification.doc_spec import DocSpec
from specification.sheet_spec import SheetSpec
from specification.table_spec import TableSpec
from specification.region_spec import RegionSpec
from specification.hours_spec import HoursSpec
from dotenv import load_dotenv

load_dotenv()

DB_TABLE = 'test'
DEST_PATH = 'D:\\workspace\\MGR\\ksgmet_analiza_sierpien.xlsx'
MAP_DIR = 'D:\\workspace\\MGR\\ksgmet-etl\\maps'

print('Executing second query set')

hour_specs = [
    HoursSpec(
        name='Wszystkie dane',
        made_on_hour_range=None,
        prediction_length_range=None
    ),

    HoursSpec(
        name='00:00 - 05:59 4h-12h',
        made_on_hour_range=(0, 360),
        prediction_length_range=(4, 12)
    ),
    HoursSpec(
        name='00:00 - 05:59 13h-20h',
        made_on_hour_range=(0, 360),
        prediction_length_range=(13, 20)
    ),
    HoursSpec(
        name='00:00 - 05:59 21h-28h',
        made_on_hour_range=(0, 360),
        prediction_length_range=(21, 28)
    ),
    HoursSpec(
        name='00:00 - 05:59 29h-40h',
        made_on_hour_range=(0, 360),
        prediction_length_range=(29, 40)
    ),

    HoursSpec(
        name='06:00 - 11:59 4h-12h',
        made_on_hour_range=(361, 720),
        prediction_length_range=(4, 12)
    ),
    HoursSpec(
        name='06:00 - 11:59 13h-20h',
        made_on_hour_range=(361, 720),
        prediction_length_range=(13, 20)
    ),
    HoursSpec(
        name='06:00 - 11:59 21h-28h',
        made_on_hour_range=(361, 720),
        prediction_length_range=(21, 28)
    ),
    HoursSpec(
        name='06:00 - 11:59 29h-40h',
        made_on_hour_range=(361, 720),
        prediction_length_range=(29, 40)
    ),

    HoursSpec(
        name='12:00 - 17:59  4h-12h',
        made_on_hour_range=(721, 1080),
        prediction_length_range=(4, 12)
    ),
    HoursSpec(
        name='12:00 - 17:59 13h-20h',
        made_on_hour_range=(721, 1080),
        prediction_length_range=(13, 20)
    ),
    HoursSpec(
        name='12:00 - 17:59 21h-28h',
        made_on_hour_range=(721, 1080),
        prediction_length_range=(21, 28)
    ),
    HoursSpec(
        name='12:00 - 17:59 29h-40h',
        made_on_hour_range=(721, 1080),
        prediction_length_range=(29, 40)
    ),

    HoursSpec(
        name='18:00 - 23:59  4h-12h',
        made_on_hour_range=(1081, 1440),
        prediction_length_range=(4, 12)
    ),
    HoursSpec(
        name='18:00 - 23:59 13h-20h',
        made_on_hour_range=(1081, 1440),
        prediction_length_range=(13, 20)
    ),
    HoursSpec(
        name='18:00 - 23:59 21h-28h',
        made_on_hour_range=(1081, 1440),
        prediction_length_range=(21, 28)
    ),
    HoursSpec(
        name='18:00 - 23:59 29h-40h',
        made_on_hour_range=(1081, 1440),
        prediction_length_range=(29, 40)
    ),
]

doc_spec = DocSpec(
    db_table=DB_TABLE,
    sheet_specs=[
        SheetSpec(
            name='Wszystkie dane',
            description='Placeholder',
            region_spec=RegionSpec(name=None, map_dir=MAP_DIR),
            table_specs=[
                TableSpec(
                    field='t2mean2m',
                    hour_specs=hour_specs
                ),
                TableSpec(
                    field='tmin2m',
                    hour_specs=hour_specs
                ),
                TableSpec(
                    field='tmax2m',
                    hour_specs=hour_specs
                )
            ]
        ),
        SheetSpec(
            name='Góry',
            description='Placeholder',
            region_spec=RegionSpec(name='mountains', map_dir=MAP_DIR),
            table_specs=[
                TableSpec(
                    field='t2mean2m',
                    hour_specs=hour_specs
                ),
                TableSpec(
                    field='tmin2m',
                    hour_specs=hour_specs
                ),
                TableSpec(
                    field='tmax2m',
                    hour_specs=hour_specs
                )
            ]
        ),
        SheetSpec(
            name='Wybrzeże',
            description='Placeholder',
            region_spec=RegionSpec(name='shoreline', map_dir=MAP_DIR),
            table_specs=[
                TableSpec(
                    field='t2mean2m',
                    hour_specs=hour_specs
                ),
                TableSpec(
                    field='tmin2m',
                    hour_specs=hour_specs
                ),
                TableSpec(
                    field='tmax2m',
                    hour_specs=hour_specs
                )
            ]
        ),
        SheetSpec(
            name='Teren wiejski',
            description='Placeholder',
            region_spec=RegionSpec(name='rural', map_dir=MAP_DIR),
            table_specs=[
                TableSpec(
                    field='t2mean2m',
                    hour_specs=hour_specs
                ),
                TableSpec(
                    field='tmin2m',
                    hour_specs=hour_specs
                ),
                TableSpec(
                    field='tmax2m',
                    hour_specs=hour_specs
                )
            ]
        )
    ]
)

doc_spec.execute()

doc_spec.write_to_doc(DEST_PATH)
