from __future__ import annotations
from fastapi import FastAPI, Response
from series import FibonacciSeries
from series import ArithmeticSeries
import sys
import enum
import csv
import io


# Be careful with this line, recommended up to 1,000,000
sys.set_int_max_str_digits(100000)

app: FastAPI = FastAPI()
MAX_DIGITS: int = 100000


@app.get("/fibonacci_csv")
def fibonacci_csv(n: int):
    if n > MAX_DIGITS:
        return Response(
            f"Requested n is too large, maximum currently allowed {MAX_DIGITS}"
        )
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


@app.get("/nthfibonacci")
def nthfibonacci(n: int):
    if n > MAX_DIGITS:
        return Response(
            f"Requested n is too large, maximum currently allowed {MAX_DIGITS}"
        )
    fib: FibonacciSeries = FibonacciSeries(n)
    result: int = fib.get()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([f"{n}th", f"{result}"])
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
