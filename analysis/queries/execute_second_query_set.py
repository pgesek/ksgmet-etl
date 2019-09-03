from specification.doc_spec import DocSpec
from specification.sheet_spec import SheetSpec
from specification.table_spec import TableSpec
from specification.region_spec import RegionSpec
from specification.hours_spec import HoursSpec
from specification.hour_spec_list import HourSpecList
from restrictions.acm_total_percip_restriction import AcmTotalPercipRestriction

DEST_PATH = 'D:\\workspace\\MGR\\second_analysis'
MAP_DIR = 'D:\\workspace\\MGR\\ksgmet-etl\\maps'
MAP_IMG_DIR = 'D:\\workspace\\MGR\\maps\\second_analysis'
OVERVIEW_MAP_PATH = 'D:\\workspace\\MGR\\maps\\regions'


def run(db, table, rain_restriction):

    print('Executing second query set')

    map_img_dir = MAP_IMG_DIR
    dest_path = DEST_PATH

    restrictions = []
    if rain_restriction:
        restrictions.append(AcmTotalPercipRestriction(rain_restriction))

    for restriction in restrictions:
        map_img_dir += restriction.suffix()
        dest_path += restriction.suffix()

    hour_specs = HourSpecList(hour_specs=[
        HoursSpec(
            override_header='Wszystkie dane',
        ),

        HoursSpec(
            time_header='00:00 - 05:59',
            length_header='4h-12h',
            made_on_hour_range=(0, 360),
            prediction_length_range=(4, 12)
        ),
        HoursSpec(
            time_header='00:00 - 05:59',
            length_header='13h-20h',
            made_on_hour_range=(0, 360),
            prediction_length_range=(13, 20)
        ),
        HoursSpec(
            time_header='00:00 - 05:59',
            length_header='21h-28h',
            made_on_hour_range=(0, 360),
            prediction_length_range=(21, 28)
        ),
        HoursSpec(
            time_header='00:00 - 05:59',
            length_header='29h-41h',
            made_on_hour_range=(0, 360),
            prediction_length_range=(29, 41)
        ),

        HoursSpec(
            time_header='06:00 - 11:59',
            length_header='4h-12h',
            made_on_hour_range=(361, 720),
            prediction_length_range=(4, 12)
        ),
        HoursSpec(
            time_header='06:00 - 11:59',
            length_header='13h-20h',
            made_on_hour_range=(361, 720),
            prediction_length_range=(13, 20)
        ),
        HoursSpec(
            time_header='06:00 - 11:59',
            length_header='21h-28h',
            made_on_hour_range=(361, 720),
            prediction_length_range=(21, 28)
        ),
        HoursSpec(
            time_header='06:00 - 11:59',
            length_header='29h-41h',
            made_on_hour_range=(361, 720),
            prediction_length_range=(29, 41)
        ),

        HoursSpec(
            time_header='12:00 - 17:59',
            length_header='4h-12h',
            made_on_hour_range=(721, 1080),
            prediction_length_range=(4, 12)
        ),
        HoursSpec(
            time_header='12:00 - 17:59',
            length_header='13h-20h',
            made_on_hour_range=(721, 1080),
            prediction_length_range=(13, 20)
        ),
        HoursSpec(
            time_header='12:00 - 17:59',
            length_header='21h-28h',
            made_on_hour_range=(721, 1080),
            prediction_length_range=(21, 28)
        ),
        HoursSpec(
            time_header='12:00 - 17:59',
            length_header='29h-41h',
            made_on_hour_range=(721, 1080),
            prediction_length_range=(29, 41)
        ),

        HoursSpec(
            time_header='18:00 - 23:59',
            length_header='4h-12h',
            made_on_hour_range=(1081, 1440),
            prediction_length_range=(4, 12)
        ),
        HoursSpec(
            time_header='18:00 - 23:59',
            length_header='13h-20h',
            made_on_hour_range=(1081, 1440),
            prediction_length_range=(13, 20)
        ),
        HoursSpec(
            time_header='18:00 - 23:59',
            length_header='21h-28h',
            made_on_hour_range=(1081, 1440),
            prediction_length_range=(21, 28)
        ),
        HoursSpec(
            time_header='18:00 - 23:59',
            length_header='29h-41h',
            made_on_hour_range=(1081, 1440),
            prediction_length_range=(29, 41)
        ),
    ])

    doc_spec = DocSpec(
        db_name=db,
        db_table=table,
        use_mocks=True,
        map_dir=map_img_dir,
        restrictions=restrictions,
        sheet_specs=[
            SheetSpec(
                name='Wszystkie dane',
                description='Placeholder',
                region_spec=RegionSpec(
                    name=None,
                    map_dir=MAP_DIR
                ),
                table_specs=[
                    TableSpec(
                        field='t2mean2m'
                    ),
                    TableSpec(
                        field='tmin2m'
                    ),
                    TableSpec(
                        field='tmax2m'
                    )
                ],
                hour_spec_list=hour_specs,
                include_maps=True
            ),
            SheetSpec(
                name='Góry',
                description='Placeholder',
                region_spec=RegionSpec(
                    name='mountains',
                    map_dir=MAP_DIR,
                    overview_map_path=OVERVIEW_MAP_PATH + '\\mountains.png'
                ),
                table_specs=[
                    TableSpec(
                        field='t2mean2m'
                    ),
                    TableSpec(
                        field='tmin2m'
                    ),
                    TableSpec(
                        field='tmax2m'
                    )
                ],
                hour_spec_list=hour_specs,
                include_maps=False
            ),
            SheetSpec(
                name='Wybrzeże',
                description='Placeholder',
                region_spec=RegionSpec(
                    name='shoreline',
                    map_dir=MAP_DIR,
                    overview_map_path=OVERVIEW_MAP_PATH + '\\shoreline.png'
                ),
                table_specs=[
                    TableSpec(
                        field='t2mean2m'
                    ),
                    TableSpec(
                        field='tmin2m'
                    ),
                    TableSpec(
                        field='tmax2m'
                    )
                ],
                hour_spec_list=hour_specs,
                include_maps=False,
            ),
            SheetSpec(
                name='Teren wiejski',
                description='Placeholder',
                region_spec=RegionSpec(
                    name='rural',
                    map_dir=MAP_DIR,
                    overview_map_path=OVERVIEW_MAP_PATH + '\\rural.png'
                ),
                table_specs=[
                    TableSpec(
                        field='t2mean2m'
                    ),
                    TableSpec(
                        field='tmin2m'
                    ),
                    TableSpec(
                        field='tmax2m'
                    )
                ],
                hour_spec_list=hour_specs,
                include_maps=False
            ),
        ]
    )

    doc_spec.execute()

    print('Saving results')

    doc_spec.write_to_doc(dest_path)
