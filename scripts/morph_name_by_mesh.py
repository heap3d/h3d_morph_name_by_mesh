#!/usr/bin/python
# ================================
# (C)2025 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python

import modo
import modo.constants as c


NEW_MAP_PREFIX = 'Morph '
DUPLICATE_NAME_SUFFIX = ' (2)'


def main():
    meshes: list[modo.Mesh] = modo.Scene().selectedByType(itype=c.MESH_TYPE)

    for mesh in meshes:
        map_name = f'{NEW_MAP_PREFIX}{mesh.name}'
        morph_maps: tuple = get_morph_maps(mesh)

        if len(morph_maps) != 1:
            create_morph_map(mesh, map_name)
            continue

        morph_maps[0].name = map_name


def get_morph_maps(mesh: modo.Mesh) -> tuple:
    vmaps = get_vmaps(mesh)
    return vmaps.morphMaps


def create_morph_map(mesh: modo.Mesh, name: str):
    vmaps = get_vmaps(mesh)

    names = [map.name for map in vmaps.morphMaps]
    while name in names:
        name += DUPLICATE_NAME_SUFFIX

    morph_map = vmaps.addMorphMap(name)
    mesh.geometry.setMeshEdits()

    return morph_map


def get_vmaps(mesh: modo.Mesh):
    geo = mesh.geometry
    if not geo:
        raise TypeError('Error getting geometry')
    vmaps = geo.vmaps
    if not vmaps:
        raise TypeError('Error getting vertex maps')

    return vmaps


if __name__ == '__main__':
    main()
