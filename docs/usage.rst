Usage Guide
===========

This section provides examples and instructions on how to use seqr in your workflow.

Basic Setup
-----------

To get started with seqr, you typically need to set up a project and load your genomic data.

Example: Loading Data
---------------------

Here is a simple example of how you might interact with the seqr API (assuming a client exists or using the internal modules).

.. code-block:: python

   from seqr.models import Project, Sample
   
   # Load a project
   project = Project.objects.get(name="MyGenomicProject")
   
   # List samples in the project
   for sample in project.samples.all():
       print(f"Sample ID: {sample.sample_id}")

Searching for Variants
----------------------

Search is a core component of seqr. You can use the search API to find specific variants.

.. code-block:: python

   from clickhouse_search.query import VariantSearch
   
   # Define search criteria
   search = VariantSearch(project_id=123)
   search.add_filter(gene="TTN", variant_type="missense")
   
   # Execute search
   results = search.execute()
   print(f"Found {len(results)} variants.")
