import os
##### Define final output files #####
rule final:
	input:	functions=expand("output/geneInfo.txt"),
		sequences=expand("output/sequences.txt"),
		pubmed=expand("output/pubmedids.txt"),
		kegg=expand("output/kegg.txt"),
		gcplots=expand("output/gcplots/"),
		report=expand("Gene_report.txt")

rule get_functions:
	input: "RNA-Seq-test.txt"
	output: "output/geneInfo.txt"

	message: "Retrieving gene functions"
	run: 
		shell('python ./src/get_geneInfo.py')

rule get_sequence:
	input: "RNA-Seq-test.txt"
	output: "output/sequences.txt"

	message: "retrieving nucleotide sequences"
	run:
		shell('python ./src/get_sequence.py')

rule get_pubmed:
	input: "RNA-Seq-test.txt"
	output: "output/pubmedids.txt"

	message: "retrieving pubmed identifiers"
	run:
		shell('python ./src/get_pubmed.py')

rule get_kegg:
	input: "RNA-Seq-test.txt"
	output: "output/kegg.txt"

	message: "retrieving kegg pathways"
	run:
		shell('Rscript ./src/get_kegg.R')

rule get_GCplots:
	input: rules.get_sequence.output
	output: "output/gcplots/"

	message: "generating GC plots"
	run:
		shell('Rscript ./src/get_GCplots.R')

rule write_report:
	input:	rules.get_sequence.output,
		rules.get_kegg.output,
		rules.get_pubmed.output,
		rules.get_functions.output
	output: "Gene_report.txt"
	run:
		shell('python ./src/write_report.py')






