# Wiki Index

Use this page as the main navigation point for reviewed wiki content.

## Core Pages

- [[overview]] - Project overview.
- [[log]] - Chronological wiki activity log.
- [[categories/README]] - Category navigation guidance.

## Sources

- [[sources/SRC-0001-karpathy-llm-knowledge-base]] - Source note introducing the LLM-maintained wiki pattern.
- [[sources/SRC-0002-project-design-note]] - Project design note for local-first personal/work wiki organization, metadata, and privacy controls.
- [[sources/SRC-0003-training-a-force-field-from-scratch]] - Paper on Garnet, a graph-neural-network force field trained from scratch.
- [[sources/SRC-0004-automated-cytoskeletal-network-segmentation]] - Review of automated and semi-automated cytoskeletal network image segmentation and tracing.
- [[sources/SRC-0005-times-square-sampling-free-energy]] - Main paper introducing Times Square Sampling for adaptive on-the-fly free energy estimation.
- [[sources/SRC-0006-times-square-sampling-supplement]] - Supplement with TSS derivations, proofs, implementation recursions, and molecular-dynamics numerics.

## Concepts

- [[concepts/persistent-llm-wiki]] - A durable, interlinked Markdown wiki maintained by an LLM.
- [[concepts/local-first-personal-work-knowledge-base]] - Local Markdown knowledge base for personal and work contexts.
- [[concepts/raw-wiki-schema-layers]] - The `raw/`, `wiki/`, and `schema/` architecture.
- [[concepts/source-ingestion]] - Workflow for compiling one source into wiki updates.
- [[concepts/wiki-index-and-log]] - Roles of the content index and chronological log.
- [[concepts/wiki-linting]] - Structural and content health checks for the wiki.
- [[concepts/multi-category-wiki-organization]] - Frontmatter-driven organization across multiple categories.
- [[concepts/wiki-page-metadata]] - Metadata fields for areas, categories, tags, related pages, sources, sensitivity, and encryption.
- [[concepts/optional-encryption-and-sensitivity-metadata]] - Selective privacy controls without mandatory repository-wide encryption.
- [[concepts/reusable-codex-task-contracts]] - Shared Codex task constraints and report formats.
- [[concepts/garnet-force-field]] - GNN-based force field for proteins and small molecules.
- [[concepts/automated-force-field-training]] - Data-driven training of molecular mechanics force fields.
- [[concepts/double-exponential-potential]] - Non-bonded potential used by Garnet instead of Lennard-Jones.
- [[concepts/relative-binding-free-energy-benchmarking]] - Benchmarking ligand binding predictions against experimental data.
- [[concepts/cytoskeletal-network-image-analysis]] - Microscopy-based analysis of cytoskeletal filament network geometry, topology, and dynamics.
- [[concepts/cytoskeleton-segmentation-and-tracing]] - Methods for extracting masks, centrelines, graphs, and tracked filament instances from cytoskeleton images.
- [[concepts/deep-learning-cytoskeleton-image-analysis]] - Deep-learning-assisted segmentation, enhancement, reconstruction, and tracking for cytoskeletal microscopy.
- [[concepts/times-square-sampling]] - Adaptive on-the-fly algorithm for free energy estimation.
- [[concepts/free-energy-estimation]] - Estimating free energy differences as ratios of partition functions or normalizing constants.
- [[concepts/adaptive-enhanced-sampling]] - Sampling methods that use on-the-fly estimates to allocate computational effort.
- [[concepts/on-the-fly-estimation-versus-mbar]] - Comparison between adaptive on-the-fly estimation and the multistate Bennett acceptance ratio estimator.
- [[concepts/tss-implementation-patterns]] - Practical implementation patterns for Times Square Sampling.

## Questions

- [[questions/optional-tooling-for-llm-wiki]] - Whether to adopt optional tools or formats from SRC-0001 or SRC-0002 later.
- [[questions/garnet-validation-scope]] - Validation gaps before treating Garnet as broadly transferable.
- [[questions/tss-generalization-scope]] - Validation boundaries for Times Square Sampling claims beyond analyzed settings.
