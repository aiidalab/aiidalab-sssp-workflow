"""This Page takes an extra argument, meaning that it can cache urls like /tabular/titanic
and pass the last part of the url as argument to the Page component, so we can render content
dynamically.
"""
from IPython.display import display
from typing import Optional

import solara
import textwrap
from solara.components.file_drop import FileInfo
from aiidalab_sssp.components.computational_resource import ComputationalResourcesWidget
import pandas as pd
import plotly

df = plotly.data.iris()

@solara.component
def Page():
    # XXX: used for showing all verifications
    # Must have:
    # 1. tickbox to show running and finished.
    # 2. filter and search by name
    # 3. redirect result to explore
    # 4. Back to home to submit new.
    solara.DataFrame(
        df, 
        items_per_page=20,
    )

@solara.component
def Overview():
    # XXX: consider not have a independent page but just a overview widget tool in the index page
    protocol = solara.reactive("quick")
    is_run_transferability = solara.reactive(True)
    is_run_convergence = solara.reactive(True)

    mode = 'mc'
    if mode == 'aiidalab':
        import aiida
        aiida.load_profile()

        crw = ComputationalResourcesWidget(enable_detailed_setup=False)
        crw_value = solara.use_reactive(None)

        def _update_code_label(change):
            crw_value.set(change['new'])

        crw.observe(_update_code_label)

    with solara.ColumnsResponsive(12) as main:
        with solara.Card(title="Verification setup"):
            solara.Markdown("Running verification, if .. if.. qucik for , standard for, trannnn")

            # Step 1
            UpfFileDrop()

            # Step 2
            with solara.VBox():
                solara.Markdown("### Protocol selection")
                with solara.ToggleButtonsSingle(value=protocol):
                    solara.Button("Quick", icon_name="mdi-run-fast", value="quick", text=True)
                    solara.Button("Standard", icon_name="mdi-standard-definition", value="standard", text=True)

                solara.Markdown("### Verification selection")
                with solara.Row():
                    solara.Checkbox(label="Transferability", value=is_run_transferability)
                    solara.Checkbox(label="Convergence test", value=is_run_convergence)

            # XXX: Improve me, very hacky.
            # The problem is when crw_value updated, this part of component will be rerendered.
            if mode == 'aiidalab':
                if crw_value.value is not None:
                    crw.value = crw_value.value
                    display(crw)
                else:
                    display(crw)

                solara.Markdown(f"**Code**: {crw_value.value}")
            else:
                pw_code = 'pw-7.2@eiger-hq'
                ph_code = 'ph-7.2@eiger-hq'
                
            # Step 3
            # Dry run will parse the UPF and display the basic info
            # Lanuch will submit the verification
            with solara.Row():
                solara.Button(label="Dry run", color="blue", icon_name="mdi-hair-dryer", outlined=True, text=True)
                solara.Button(label="Launch", color="green", icon_name="mdi-play", outlined=True, text=True)


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

# @solara.component
# def Overview():
#     with solara.Card(title="Verification") as main:
#         with solara.Column():
#             solara.HTML(unsafe_innerHTML=html_content)
#             with solara.Card(title="UPF file upload"):
#                 UpfFileDrop()
#
#     return main
