"""Report generation helpers."""

import csv
import json


class Reporter:
    """Print or save scan results."""

    def print_report(self, results, quiet=False):
        if not quiet:
            print(json.dumps(results, indent=2))

    def save_report(self, results, output, output_format="json"):
        if output_format == "json":
            with open(output, "w", encoding="utf-8") as report:
                json.dump(results, report, indent=2)
        elif output_format == "txt":
            with open(output, "w", encoding="utf-8") as report:
                report.write(json.dumps(results, indent=2))
        elif output_format == "csv":
            with open(output, "w", newline="", encoding="utf-8") as report:
                writer = csv.DictWriter(report, fieldnames=results[0].keys())
                writer.writeheader()
                writer.writerows(results)
