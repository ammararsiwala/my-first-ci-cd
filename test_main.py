import hello

def test_output(capfd):
    # Run the script
    hello.main()

    # Capture the output
    out, err = capfd.readouterr()

    # Check the output using pytest's assert statement
    assert out.strip() == (
        "Hello World\n"
        "I MADE MY FIRST CHANGE\n"
        "NOW LET'S SEE IF I GET AN ERROR OR NO"
    )
