from pathlib import Path


def check_project():
    root = Path(".")
    paths = [
        root / "frontend" / "templates" / "pages" / "login.html",
        root / "frontend" / "templates" / "layouts" / "base.html",
        root / "frontend" / "static" / "css" / "input.css",
        root / "frontend" / "static" / "css" / "output.css",
        root / "package.json",
    ]

    print("=== File Existence Check ===")
    for p in paths:
        status = "✅ FOUND" if p.exists() else "❌ MISSING"
        print(f"{status}: {p}")

    input_css = root / "frontend" / "static" / "css" / "input.css"
    if input_css.exists():
        print("\n=== input.css Content ===")
        print(input_css.read_text().strip())

    output_css = root / "frontend" / "static" / "css" / "output.css"
    if output_css.exists():
        print("\n=== output.css Stats ===")
        lines = len(output_css.read_text().splitlines())
        print(
            f"Total lines: {lines} (If under ~50 lines, Tailwind hasn't detected your HTML classes)"
        )


if __name__ == "__main__":
    check_project()
