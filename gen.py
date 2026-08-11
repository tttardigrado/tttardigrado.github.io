import pypandoc
from pathlib import Path
import shutil
import datetime
import yaml
from feedgen.feed import FeedGenerator

def read_frontmatter(md_file: Path) -> dict:
    text = md_file.read_text()
    if text.startswith("---"):
        _, fm, *_ = text.split("---", 2)
        return yaml.safe_load(fm)
    return {}

def make_post(file: Path, dest: Path) -> None:
    pypandoc.convert_file(
        str(file), "html", outputfile=str(dest), extra_args=[
        "--standalone",
        "--mathml",
        "--bibliography", "./template/bibliography.bib",
        "--csl", "./template/bibstyle.csl",
        "--metadata-file", "./template/config.yaml",
        "--highlight-style=monochrome",
        "--css", "/style.css",
        "--template", "./template/template.html",
        ]
    )

def make_index(dir: Path):
    posts = []
    for file in dir.glob("*.md"):
        fm = read_frontmatter(file)
        posts.append({
            "title": fm.get("title", file.stem.capitalize()),
            "date":  fm.get("date", datetime.date.min),
            "href":  file.with_suffix(".html").name,
        })
    posts.sort(key=lambda p: p["date"], reverse=True)
    items = "\n".join(f'* [{p["title"]}]({p["href"]})' for p in posts)
    (dir / "index.md").write_text(f"---\ntitle: {dir.stem.capitalize()}\n---\n\n{items}\n")

def make_rss(posts_dir: Path, public_dir: Path, content_dir: Path):
    fg = FeedGenerator()
    fg.title("tttardigrado's Feed")
    fg.link(href="https://tttardigrado.github.io")
    fg.description("Latest posts from tttardigrado")
    fg.language("en")

    entries = []
    for file in posts_dir.glob("*.md"):
        if file.name == "index.md":
            continue
        fm = read_frontmatter(file)
        rel_href = file.relative_to(content_dir).with_suffix(".html")
        entries.append({
            "title": fm.get("title", file.stem.capitalize()),
            "date": datetime.datetime.combine(fm.get("date", datetime.date.min), datetime.time.min).replace(tzinfo=datetime.timezone.utc),
            "link": f"https://tttardigrado.github.io/{rel_href}",
            "description": fm.get("description", ""),
        })

    entries.sort(key=lambda e: e["date"], reverse=True)

    for entry in entries:
        fe = fg.add_entry()
        fe.title(entry["title"])
        fe.link(href=entry["link"])
        fe.description(entry["description"])
        fe.pubDate(entry["date"])
        fe.guid(entry["link"])

    dest = public_dir / "rss.xml"
    fg.rss_file(str(dest))


def main():
    content_dir = Path("./content")
    public_dir = Path("./public")

    # clear old site
    shutil.rmtree(public_dir, ignore_errors=True)
    for f in content_dir.rglob("index.md"):
        f.unlink()
   
    # generate index files for each category
    for dir in {f.parent for f in content_dir.rglob("*.md")}:
        make_index(dir)

    # generate posts
    for file in content_dir.rglob("*.md"):
        dest = public_dir / file.relative_to(content_dir).with_suffix(".html")
        dest.parent.mkdir(parents=True, exist_ok=True)
        make_post(file, dest)
 
    for f in content_dir.rglob("index.md"):
        f.unlink()

    # generate main page
    make_post(Path("./about.md"), public_dir / "index.html")

    make_rss(content_dir / "posts", public_dir, content_dir)
    
    # copy assets to public
    shutil.copy("./template/style.css", public_dir / "style.css")
    shutil.copytree("./assets/", public_dir / "assets/")



if __name__ == "__main__":
    main()
