from src import main


def test_main(capsys):
    main.main()
    captured = capsys.readouterr()
    assert (
        captured.out.strip() == "Hello from python-devops-example!"
    )  # Check if the output is as expected


# This test checks if the main function in main.py prints the expected output.
# It uses the `capsys` fixture to capture standard output and then asserts that the captured output matches the expected string.
