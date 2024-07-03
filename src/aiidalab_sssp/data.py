import dataclasses
from pathlib import Path
from typing import Any, Dict

import vaex.datasets
import yaml


@dataclasses.dataclass
class DataFrame:
    title: str
    df: Any
    image_url: str


dfs = {
    "titanic": DataFrame(
        df=vaex.datasets.titanic(),
        title="Titanic",
        image_url="https://images.unsplash.com/photo-1561625116-df74735458a5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3574&q=80",  # noqa
    ),
    "iris": DataFrame(
        df=vaex.datasets.iris(),
        title="Iris",
        image_url="https://images.unsplash.com/photo-1540163502599-a3284e17072d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3870&q=80",  # noqa
    ),
    # uncomment for a larger dataset to be included
    # "taxi": DataFrame(
    #     df=vaex.datasets.taxi(),
    #     title="New York Taxi",
    #     image_url="https://images.unsplash.com/photo-1514749204155-24e484635226?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1587&q=80",  # noqa
    # ),
}

names = list(dfs)
# def load(name):
#     if name == "titanic"

HERE = Path(__file__)


@dataclasses.dataclass
class Article:
    markdown: str
    title: str
    description: str
    image_url: str


articles: Dict[str, Article] = {}

for file in (HERE.parent / "content/articles").glob("*.md"):
    content = file.read_text()
    lines = [k.strip() for k in content.split("\n")]
    frontmatter_start = lines.index("---", 0)
    frontmatter_end = lines.index("---", frontmatter_start + 1)
    yamltext = "\n".join(lines[frontmatter_start + 1 : frontmatter_end - 2])
    metadata = yaml.safe_load(yamltext)
    markdown = "\n".join(lines[frontmatter_end + 1 :])
    articles[file.stem] = Article(markdown=markdown, title=metadata["title"], description=metadata["description"], image_url=metadata["image"])

# XXX:: move me to static html file
html_cite = """
Please always cite the library you are using as:
<ul class="links">
    <br>
    <li> In the main text, you can refer to the library as <code>SSSP [xc] [acc] [version]</code>, for example: "SSSP PBEsol Precision v1.3.0" 
         <br><i>&nbsp&nbsp In the string above: <code>[xc]</code> is the functional (PBE or PBEsol), <code>[acc]</code> is the SSSP library variant (either Efficency or Precision), and <code>[version]</code> is the SSSP version (in this example, version 1.3.0).</i>
        <br>
        <br>In addition, in the reference please also cite the link to the SSSP paper and to the SSSP website:  
        <br>&nbsp&nbsp G. Prandini, A. Marrazzo, I. E. Castelli, N. Mounet and N. Marzari, <a href="https://www.nature.com/articles/s41524-018-0127-2" target="_blank">npj Computational Materials <b>4</b>, 72</a> (2018)
        <br>&nbsp&nbsp <a href="http://materialscloud.org/sssp"> http://materialscloud.org/sssp</a>
        <br>or combining the two references as:
        <br>&nbsp&nbsp G. Prandini, A. Marrazzo, I. E. Castelli, N. Mounet and N. Marzari, <a href="https://www.nature.com/articles/s41524-018-0127-2" target="_blank">npj Computational Materials <b>4</b>, 72</a> (2018), <a href="http://materialscloud.org/sssp"> http://materialscloud.org/sssp</a> 
    </li>
    <li>
        <p>You can use the following BibTeX entry for the combined reference:</p>

        <p>@article{prandini2018precision,<br>
         &nbsp&nbsp title={Precision and efficiency in solid-state pseudopotential calculations},<br>
         &nbsp&nbsp author={Prandini, Gianluca and Marrazzo, Antimo and Castelli, Ivano E and Mounet, Nicolas and Marzari, Nicola},<br>
         &nbsp&nbsp journal={npj Computational Materials},<br>
         &nbsp&nbsp volume={4},<br>
         &nbsp&nbsp number={1},<br>
         &nbsp&nbsp pages={72},<br>
         &nbsp&nbsp year={2018},<br>
         &nbsp&nbsp issn = {2057-3960},<br>
         &nbsp&nbsp url = {https://www.nature.com/articles/s41524-018-0127-2},<br>
         &nbsp&nbsp doi = {10.1038/s41524-018-0127-2},<br>
         &nbsp&nbsp note = {\href{http://materialscloud.org/sssp}{http://materialscloud.org/sssp}},<br>
         &nbsp&nbsp publisher={Nature Publishing Group UK London}<br>
        }</p>
    </li>
    <br>
</ul>

<p>
    <b> Please make an effort to acknowledge original authors and to ensure
    reproducibility of your calculations by listing or citing all
    pseudopotentials used, and being compliant with the corresponding licenses.

    Click <a data-dismiss="modal" data-toggle="collapse" data-target="#ackWindow" href="#" aria-expanded="true" aria-controls="ackWindow">here</a>
        for the acknowledgements list.
    </b>
</p>
"""

html_about = """

"""

html_ack = """

"""

html_old_version = """

"""

html_license = """
<p>
    The SSSP efficiency and precision pseudopotential libraries are a collection of pseudopotentials generated
    by different authors with different methodologies, selected according to the SSSP protocol.
    Each single pseudopotential is distributed with its original license (e.g. GPL or Creative Commons)
    as chosen by its authors.
</p>
<p>
    By downloading the SSSP efficiency or precision libraries, you accept the
    terms and conditions of the original licenses.
</p>
<p>
    Please make an effort to acknowledge original authors and to ensure reproducibility of your calculations
    by listing or citing all pseudopotentials used, and being compliant with the corresponding licenses.

    Click <a data-toggle="collapse" data-target="#ackWindow"
             href="#" aria-expanded="true" aria-controls="ackWindow">here</a>
    for the acknowledgements list.
</p>
"""
