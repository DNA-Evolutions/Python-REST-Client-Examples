Build models:
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate  -i '/local/swagger/touroptimizer/spec/touroptimizer_spec.json' -g python  -o /local/generated/jopt-touroptimizer-py-client  --package-name=touroptimizer_py_client --additional-properties="useOneOfDiscriminatorLookup=true"

Apply fix:
Fix generated models -> See git history

Unistall and Install:
pip uninstall touroptimizer_py_client
python setup.py install