#include <iostream>
#include <memory>
#include <string>

class Report {
public:
    virtual ~Report() = default;
    virtual void export_report() const = 0;
};

class PdfReport : public Report {
public:
    void export_report() const override { std::cout << "Exporting PDF report\n"; }
};

class CsvReport : public Report {
public:
    void export_report() const override { std::cout << "Exporting CSV report\n"; }
};

class ReportCreator {
public:
    virtual ~ReportCreator() = default;
    void build_report() const {
        auto report = create_report();
        report->export_report();
    }

protected:
    virtual std::unique_ptr<Report> create_report() const = 0;
};

class PdfReportCreator : public ReportCreator {
protected:
    std::unique_ptr<Report> create_report() const override { return std::make_unique<PdfReport>(); }
};

class CsvReportCreator : public ReportCreator {
protected:
    std::unique_ptr<Report> create_report() const override { return std::make_unique<CsvReport>(); }
};

int main() {
    PdfReportCreator pdf_creator;
    CsvReportCreator csv_creator;

    pdf_creator.build_report();
    csv_creator.build_report();
}
