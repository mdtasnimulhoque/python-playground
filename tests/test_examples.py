import subprocess
import sys


def run_code(source: str) -> str:
    result = subprocess.run(
        [sys.executable, "-c", source],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def test_first_lesson_expected_output():
    output = run_code(
        'print("Hello, future programmer!")\n'
        'print("I am learning to give computers instructions.")\n'
        'print(2 + 3)\n'
    )
    assert output == (
        "Hello, future programmer!\n"
        "I am learning to give computers instructions.\n"
        "5\n"
    )


def test_string_concatenation_differs_from_addition():
    assert run_code('print(4 + 6)\nprint("4" + "6")\n') == "10\n46\n"
