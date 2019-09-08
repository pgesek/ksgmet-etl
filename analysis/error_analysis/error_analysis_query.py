from error_analysis.model.error_analysis_doc import ErrorAnalysisDoc
from error_analysis.model.error_analysis_sheet import ErrorAnalysisSheet
from error_analysis.model.error_analysis_table import ErrorAnalysisTable
from error_analysis.model.analysis_field import AnalysisField

DEST_PATH = 'D:\\workspace\\MGR\\error_analysis'


def run():
    print('Executing error analysis query set')

    tables = [
        ErrorAnalysisTable(field='t2mean2m'),
        ErrorAnalysisTable(field='tmin2m'),
        ErrorAnalysisTable(field='tmax2m'),
    ]

    doc = ErrorAnalysisDoc(
        analysis_fields=[
            AnalysisField(
                field='COUNT(*)',
                alias='count',
                header='Ilość prognoz'
            ),
            AnalysisField(
                field='AVG({field}_delta)',
                alias='average_{field}_delta',
                header='Średnia błędu'
            ),
            AnalysisField(
                field='AVG(ABS({field}_delta))',
                alias='average_abs_{field}_delta',
                header='Średnia bezwzględna błędu'
            ),
            AnalysisField(
                field='AVG(acm_total_percip_actual)',
                alias='average_actual_total_percip',
                header='Średni opad całkowity właściwy'
            ),
            AnalysisField(
                field='AVG(acm_total_percip_predicted)',
                alias='average_predicted_total_percip',
                header='Średni opad całkowity przewidziany'
            ),
            AnalysisField(
                field='AVG(acm_convective_percip_actual)',
                alias='average_actual_convective_percip',
                header='Średni opad atmosferyczny właściwy'
            ),
            AnalysisField(
                field='AVG(acm_convective_percip_predicted)',
                alias='average_predicted_convective_percip',
                header='Średni opad atmosferyczny przewidziany'
            ),
            AnalysisField(
                field='AVG(prediction_length)',
                alias='average_prediction_length',
                header='Średnia długość prognozy'
            ),
            AnalysisField(
                field='AVG({field}_predicted)',
                alias='avg_{field}_predicted',
                header='Średnia wartość przewidziana'
            ),
            AnalysisField(
                field='AVG({field}_actual)',
                alias='avg_{field}_actual',
                header='Średnia wartość właściwa'
            ),
            AnalysisField(
                field='ABS({field}_delta) > 2.0',
                alias='{field}_delta_gt_2',
                header='Delta absolutna większa niż 2.0'
            )
        ],
        sheets=[
            ErrorAnalysisSheet(
                db_name='ksgmet-november',
                table_name='november',
                description='Analiza pod względem błędu dla danych z 15.11.2018 - 15.12.2018',
                tables=tables
            ),
            ErrorAnalysisSheet(
                db_name='ksgmet-may',
                table_name='may',
                description='Analiza pod względem błędu dla danych z 15.05.2019 - 15.06.2019',
                tables=tables
            ),
            ErrorAnalysisSheet(
                db_name='ksgmet-june',
                table_name='june',
                description='Analiza pod względem błędu dla danych z 15.06.2019 - 15.07.2019',
                tables=tables
            )
        ]
    )

    doc.execute_and_write(DEST_PATH)
