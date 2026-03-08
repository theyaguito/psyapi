from __future__ import annotations
import enum
from fastapi import FastAPI, Response
from series import FibonacciSeries
from series import ArithmeticSeries
import csv
import io

app: FastAPI = FastAPI()


@app.get("/fibonacci_csv")
def fibonacci_csv(n: int):
    fib: FibonacciSeries = FibonacciSeries(n)
    result: List[int] = fib.gen()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Index", "Number"])
    for index, number in enumerate(result):
        writer.writerow([index, number])
    csv_data = output.getvalue()
    output.close()
    return Response(csv_data, media_type="text/csv")


@app.get("/arithmetic_csv")
def arithmetic_csv(n: int, start: int, diff: int):
    ari: ArithmeticSeries = ArithmeticSeries(n, start, diff)
    result: List[int] = ari.gen()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Index", "Number"])
    for index, number in enumerate(result):
        writer.writerow([index, number])
    csv_data = output.getvalue()
    output.close()
    return Response(csv_data, media_type="text/csv")
