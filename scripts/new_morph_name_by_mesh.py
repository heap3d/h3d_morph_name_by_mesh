#!/usr/bin/python
# ================================
# (C)2025 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python

import lx
import modo
import modo.constants as c


NEW_MAP_PREFIX = 'Morph '
DUPLICATE_NAME_SUFFIX = ' (2)'


def main():
    meshes: list[modo.Mesh] = modo.Scene().selectedByType(itype=c.MESH_TYPE)

    for mesh in meshes:
        name = f'{NEW_MAP_PREFIX}{mesh.name}'
        names = get_existing_morph_names()
        while name in names:
            name += DUPLICATE_NAME_SUFFIX

        create_morph_map(mesh, name)


def get_existing_morph_names() -> tuple[str]:
    indexes = [int(i) for i in lx.evalN('query layerservice vmaps ? morph')]  # type: ignore
    return tuple([lx.eval(f'query layerservice vmap.name ? {i}') for i in indexes])  # type: ignore


def create_morph_map(mesh: modo.Mesh, name: str):
    mesh.select(replace=True)
    lx.eval(f'vertMap.new "{name}" morf')


if __name__ == '__main__':
    main()
