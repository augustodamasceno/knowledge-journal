from __future__ import annotations
from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def export(self) -> None:
        ...


class PdfReport(Report):
    def export(self) -> None:
        print("Exporting PDF report")


class CsvReport(Report):
    def export(self) -> None:
        print("Exporting CSV report")


class ReportCreator(ABC):
    def build_report(self) -> None:
        report = self.create_report()
        report.export()

    @abstractmethod
    def create_report(self) -> Report:
        ...


class PdfReportCreator(ReportCreator):
    def create_report(self) -> Report:
        return PdfReport()


class CsvReportCreator(ReportCreator):
    def create_report(self) -> Report:
        return CsvReport()


def main() -> None:
    PdfReportCreator().build_report()
    CsvReportCreator().build_report()


if __name__ == "__main__":
    main()
