import basic

while True:

    text = input('basic > ')
    if(text == "break loop"):
        break
    result, error = basic.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)
