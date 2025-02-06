import main

def test_output(capfd):
    # Run the script
    main.main()
    
    # Capture the output
    out, err = capfd.readouterr()
    
    # Check the output
    assert out == "Hello World\nI MADE MY FIRST CHANGE\n"
