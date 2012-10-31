
dexterity_test
==============

This test demonstrates content type creation, with models exported from content types created through the web in Plone.

code vs. model_source vs. schema property
-----------------------------------------

There are at least 3 ways to define a schema:

- In Python code
- In a model_source property that contains the schema XML
- In a schema property that contains a Python module path that refers to an interface that loads the schema XML from a file

This test demonstrates the third approach.
