package interview.designpatterns.creational.factorymethod;

abstract class Report {
    abstract void export();
}

final class PdfReport extends Report {
    @Override
    void export() {
        System.out.println("Exporting PDF report");
    }
}

final class CsvReport extends Report {
    @Override
    void export() {
        System.out.println("Exporting CSV report");
    }
}

abstract class ReportCreator {
    public void buildReport() {
        Report report = createReport();
        report.export();
    }

    protected abstract Report createReport();
}

final class PdfReportCreator extends ReportCreator {
    @Override
    protected Report createReport() {
        return new PdfReport();
    }
}

final class CsvReportCreator extends ReportCreator {
    @Override
    protected Report createReport() {
        return new CsvReport();
    }
}

public final class FactoryMethodDemo {
    private FactoryMethodDemo() {}

    public static void main(String[] args) {
        ReportCreator pdf = new PdfReportCreator();
        ReportCreator csv = new CsvReportCreator();
        pdf.buildReport();
        csv.buildReport();
    }
}
