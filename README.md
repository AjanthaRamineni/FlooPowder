# FlooPowder
Upload files to NACC.
-----

Before running FlooPowder, use ssh-copy-id or equivalent to install your SSH key on the tools2 (or equivalent) server.

Use Upload_Config.example.yaml as a model to fill in the required information.

FlooPowder takes two arguments, the folder containing the files to be uploaded and the path to the Upload_Config file. The files to be uploaded must be at the top level of the folder.

```python floo_powder.py path/to/files/to/be/uploaded path/to/Upload_Config/file```