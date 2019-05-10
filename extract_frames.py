import sys
import os
import json
import copy

import click
import xmltodict

def get_children(node):
    for tag, element in node.items():
        if isinstance(element, list):
            return tag, element
    return None, []

@click.command()
@click.option("--input-file", default=sys.stdin)
@click.option("--output-directory")
def extract_frames(input_file, output_directory):
    tree = xmltodict.parse(input_file.read())
    os.makedirs(output_directory, exist_ok=True)

    children_key, children = get_children(tree["svg"])
    group_indices = [index for index, child in enumerate(children) if "@data-name" in child]
    for active_group_index in group_indices:
        # for each group, make a copy of the tree that doesn't have the dict
        working_tree = copy.deepcopy(tree)
        name = children[active_group_index]["@data-name"]
        working_tree["svg"][children_key] = [child for index, child in enumerate(children) if index is active_group_index]
        unparsed = xmltodict.unparse(working_tree, pretty=True)
        output_file = os.path.join(output_directory, f"{name}.svg")
        with open(output_file, "w") as output_pointer:
            output_pointer.write(unparsed)
        
if __name__ == "__main__":
    extract_frames()
