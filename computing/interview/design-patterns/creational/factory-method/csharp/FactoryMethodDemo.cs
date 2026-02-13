using System;

namespace Interview.DesignPatterns.Creational.FactoryMethod
{
    public abstract class Report
    {
        public abstract void Export();
    }

    public sealed class PdfReport : Report
    {
        public override void Export() => Console.WriteLine("Exporting PDF report");
    }

    public sealed class CsvReport : Report
    {
        public override void Export() => Console.WriteLine("Exporting CSV report");
    }

    public abstract class ReportCreator
    {
        public void BuildReport()
        {
            var report = CreateReport();
            report.Export();
        }

        protected abstract Report CreateReport();
    }

    public sealed class PdfReportCreator : ReportCreator
    {
        protected override Report CreateReport() => new PdfReport();
    }

    public sealed class CsvReportCreator : ReportCreator
    {
        protected override Report CreateReport() => new CsvReport();
    }

    public static class Demo
    {
        public static void Main()
        {
            ReportCreator pdfCreator = new PdfReportCreator();
            ReportCreator csvCreator = new CsvReportCreator();

            pdfCreator.BuildReport();
            csvCreator.BuildReport();
        }
    }
}
