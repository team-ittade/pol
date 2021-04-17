from pathlib import Path
import re
import typer

Arg = typer.Argument
Opt = typer.Option

app = typer.Typer(add_completion=False)
regex = r"([\w. :áéíóúÁÉÍÓÚ¿?,ñÑ%+\"“”-]+)\nSeleccione una:\na. ([\w. :áéíóúÁÉÍÓÚ¿?,ñÑ%+\"“”-]+)\nb. ([\w. :áéíóúÁÉÍÓÚ¿?,ñÑ%+\"“”-]+)\nc. ([\w. :áéíóúÁÉÍÓÚ¿?,ñÑ%+\"“”-]+)\nd. ([\w. :áéíóúÁÉÍÓÚ¿?,ñÑ%+\"“”-]+)\nRetroalimentación\nLa respuesta correcta es: ([\w. :áéíóúÁÉÍÓÚ¿?,ñÑ%+\"“”-]+)"


@app.command()
def main(
    lection: int = Opt(..., help="Lection of the test"),
    file: str = Arg("test.txt", exists=True, help="Path to the test's text"),
):

    output_path = Path(__file__).with_name("docs") / f"tests/tema-{lection}.md"
    data = Path(file).read_text("utf8")

    matches = re.finditer(regex, data)
    with output_path.open("wt", encoding="utf8") as fh:
        fh.write(f"# Test tema {lection}\n")
        for match in matches:
            q, a, b, c, d, sol = match.groups()
            a_sol = b_sol = c_sol = d_sol = " "
            if sol == a:
                a_sol = "x"
            elif sol == b:
                b_sol = "x"
            elif sol == c:
                c_sol = "x"
            elif sol == d:
                d_sol = "x"
            else:
                print("error")

            msg = f"\n**{q}**\n\n- [{a_sol}] {a}\n- [{b_sol}] {b}\n- [{c_sol}] {c}\n- [{d_sol}] {d}\n"
            fh.write(msg)


if __name__ == "__main__":
    app()
