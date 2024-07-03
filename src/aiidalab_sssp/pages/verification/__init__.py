"""This Page takes an extra argument, meaning that it can cache urls like /tabular/titanic
and pass the last part of the url as argument to the Page component, so we can render content
dynamically.
"""
from typing import Optional

import solara
import textwrap
from solara.components.file_drop import FileInfo



@solara.component
def Page(name: Optional[str] = None, page: int = 0, page_size=100):
    with solara.ColumnsResponsive(12) as main:
        solara.HTML(unsafe_innerHTML="""<h3>More detailed verification instructions</h3> 
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
""")
        with solara.ColumnsResponsive([6, 6]):
            with solara.Card(title="UPF file upload"):
                UpfFileDrop()
            with solara.Card(title="Verification setup"):
                DetailSetup()

    return main

@solara.component
def DetailSetup():
    with solara.Column() as main:
    # buttons for tuning protocol, dry-run (inspect the PP) or real-run of verification
    # ComputationalResourcesWidget from AWB (can I??)
        solara.HTML(unsafe_innerHTML="""PLACEHOLDER""")
        UpfFileDrop()
    return main


@solara.component
def UpfFileDrop():
    content, set_content = solara.use_state(b"")
    filename, set_filename = solara.use_state("")
    # size, set_size = solara.use_state(0)

    # TODO: should read as a stream. Should stop and raise when the file is too large. 

    def on_file(f: FileInfo):
        set_filename(f["name"])
        set_size(f["size"])
        set_content(f["file_obj"].read())

    solara.FileDrop(
        label="Drag and drop a UPF file here to run verification.",
        on_file=on_file,
        lazy=True, # XXX: check the detail, UPF file can be big ~1MB so lazy is the better choice?
    )

    # TODO: check it is a valide UPF file, by checking extension is not enough, should be a txt not a binary
    # Should be able to be parsed.
    # Raise on error if it is not valid

    # TODO: warning if it is not a PBE or relativistic PP.

    if content:
        solara.Info(f"UPF {filename} is uploaded.")
        solara.Preformatted("\n".join(textwrap.wrap(repr(content))))

html_content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

@solara.component
def Overview():
    with solara.Card(title="Verification") as main:
        with solara.Column():
            solara.HTML(unsafe_innerHTML=html_content)
            with solara.Card(title="UPF file upload"):
                UpfFileDrop()

    return main
