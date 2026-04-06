from __future__ import annotations
from pathlib import Path
from time import perf_counter
from typing import Callable, Iterable


def read_numbers(file_path: Path) -> list[int]:
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    text = file_path.read_text(encoding="utf-8-sig").strip()
    if not text:
        return []

    try:
        return [int(token) for token in text.split()]
    except ValueError as exc:
        raise ValueError(f"O arquivo deve conter apenas números inteiros separados por espaços: {exc}") from exc


def bubble_sort(numbers: list[int]) -> list[int]:
    arr = numbers.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers.copy()

    pivot = numbers[len(numbers) // 2]
    less = [x for x in numbers if x < pivot]
    equal = [x for x in numbers if x == pivot]
    greater = [x for x in numbers if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def time_algorithm(
    name: str,
    sort_func: Callable[[list[int]], list[int]],
    numbers: list[int],
    runs: int = 5,
) -> tuple[list[float], list[int]]:
    times: list[float] = []
    sorted_result: list[int] = []

    print(f"Algoritmo: {name}")
    for run_index in range(1, runs + 1):
        start = perf_counter()
        sorted_result = sort_func(numbers)
        end = perf_counter()
        duration = end - start
        times.append(duration)
        print(f"Execução {run_index}: {duration:.6f}s")

    average = sum(times) / len(times)
    print(f"Média: {average:.6f}s\n")
    return times, sorted_result


def write_sorted_numbers(file_path: Path, numbers: Iterable[int]) -> None:
    file_path.write_text(" ".join(str(num) for num in numbers), encoding="utf-8")


def main() -> None:
    base_path = Path(__file__).resolve().parent
    input_path = base_path / "arq.txt"
    output_path = base_path / "arq-ordenado.txt"

    numbers = read_numbers(input_path)
    if not numbers:
        print("O arquivo não contém números para ordenar.")
        return

    _, _ = time_algorithm("Bubble Sort", bubble_sort, numbers)
    _, sorted_numbers = time_algorithm("Quick Sort", quick_sort, numbers)
    write_sorted_numbers(output_path, sorted_numbers)
    print(f"Números ordenados gravados em: {output_path}")


if __name__ == "__main__":
    main()
