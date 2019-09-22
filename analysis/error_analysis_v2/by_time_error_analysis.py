from error_analysis_v2.docs.by_time_doc import ByTimeDoc

DEST_PATH = 'D:\\workspace\\MGR\\error_v2'


def run(error_threshold=2.0):
    doc = ByTimeDoc(error_threshold)
    doc.execute(dest_path=DEST_PATH)
