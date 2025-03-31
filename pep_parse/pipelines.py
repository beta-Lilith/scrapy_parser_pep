import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from .settings import RESULTS

BASE_DIR = Path(__file__).parent.parent
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS = 'Status'
QUANTITY = 'Quantity'
TOTAL = 'Total'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        filename = 'status_summary_{date}.csv'.format(
            date=datetime.now().strftime(DT_FORMAT))
        with open(
            f'{self.results_dir}/{filename}',
            'w',
            encoding='utf-8',
            newline=''
        ) as csvfile:
            csv.writer(csvfile, dialect=csv.excel).writerows((
                (STATUS, QUANTITY),
                *self.statuses.items(),
                (TOTAL, sum(self.statuses.values()))
            ))
