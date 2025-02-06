import hello

def test_output(capfd):
    # Run the script
    hello.main()
    
    # Capture the output
    out, err = capfd.readouterr()
    
    # Check the output
    assert out.strip() == "Hello World\nI MADE MY FIRST CHANGE\nNOW LET'S SEE IF I GET AN ERROR OR NO"
