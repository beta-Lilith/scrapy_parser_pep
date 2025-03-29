import csv
from datetime import datetime
from collections import defaultdict
from pathlib import Path
from .settings import RESULTS

BASE_DIR = Path(__file__).parent.parent
DT_FORMAT = "%Y-%m-%d_%H-%M-%S"
STATUS = 'Status'
QUANTITY = 'Quantity'


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS
        results_dir.mkdir(exist_ok=True)
        filename = f'status_summary_{datetime.now().strftime(DT_FORMAT)}.csv'
        with open(
            f'{results_dir}/{filename}',
            'w',
            encoding='utf-8',
            newline=''
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[STATUS, QUANTITY])
            writer.writeheader()
            for status, quantity in self.statuses.items():
                writer.writerow({
                    STATUS: status,
                    QUANTITY: quantity
                })
            writer.writerow({
                STATUS: 'Total',
                QUANTITY: sum(self.statuses.values())
            })
