# Go-Smart Simulation Architecture - Docker Workflows

This workflow consists of a per-[family](../families.md) Python module setting up
configuration and a solver wrapped in a Docker image. Strictly, there are
currently two Docker workflows: one entirely inside Docker and one using
[GSSF](https://go-smart.github.io/gssf/mesher) volumetric meshing prior to running a Docker instance.

## Definition

Definitions for families in this workflow should include a `start.py` file. This
will be called with Python in an environment containing the
[Python container module](container-module.md).

## Variants

### Docker-only Workflow

Any volumetric meshing must take place inside the Docker instance. This means
that the image must contain both a solver and a mesher (if meshing is required).

### Docker+CGAL Workflow

This hybrid scheme configures the [GSSF mesher](https://go-smart.github.io/gssf/mesher/) as would be the
case in [GSSF](https://go-smart.github.io/gssf/overview/), but stops after the volumetric
([CGAL](https://go-smart.github.io/gssf/tools/mesher-cgal/)) meshing step. This [MSH](http://gmsh.info) file is
provided as input to a simulation-only Docker instance. Combining these is
achieved by use of a family mixin, a module that generates only
[mesher-cgal](https://go-smart.github.io/gssf/mesher/) relevant parts of [GSSF-XML](https://go-smart.github.io/gssf/xml/),
`gssa.families.mesher_gssf.MesherGSSFMixin`.
This is included into, for instance, `gssa.families.fenics.FenicsFamily`. (In
fact, the same mix-in is used by GSSF itself for meshing configuration).
