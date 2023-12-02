def read_input(textfile, cast=str):
    return [
        cast(line.rstrip("\n")) if line.rstrip("\n") else None
        for line in open(f"{textfile}.txt", "r")
    ]
