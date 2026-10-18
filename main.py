import asyncio
from client import main
from llm import GenReport

if __name__ == "__main__":
    session_summaries, analytics, logs = asyncio.run(main())
    obj = GenReport()
    report = obj.analyze(session_summaries, analytics, logs)
    with open("diagnostic_report.txt", "w") as f:
        f.write(report)
