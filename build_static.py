import os
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape

from app import PROFILE

BASE_URL = "https://sandeepchavan16082024-prog.github.io/Myportfolio"


def url_for(endpoint, **kwargs):
    if endpoint == "static":
        filename = kwargs.get("filename", "")
        if kwargs.get("_external"):
            return f"{BASE_URL}/static/{filename}"
        return f"static/{filename}"
    return "#"


env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html", "xml"]),
)
env.globals["url_for"] = url_for

html = env.get_template("index.html").render(p=PROFILE)

os.makedirs("docs", exist_ok=True)
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

if os.path.isdir("docs/static"):
    shutil.rmtree("docs/static")
shutil.copytree("static", "docs/static")

print("Static build written to docs/")