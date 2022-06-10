# Metabolomics_to_Single_Cell
## Introduction
Here is a experimental pipeline, to help biologist understand samples from 2 different view. The goal is to validate or invalidate single cell RNA seq conclusion with metabolomics data. Let's say you have extract RNA from patient sample and you now have raw data. A first step is to analyzeyoure data, and you can go here for that purpose : https://github.com/Nathan-bioinfo/SingR. This is an shiny R application that i have develloped and it will help you to find particular RNA, or biological pathways involved in youre study. The next step could be a metabolomic confirmation, to double check the results and maybe get additional informations.<br/>
## Data
The demonstration is based on .mzml files, raw data from LC-HRMS Thermo Q-Exactive (Liquid Chromatography for Mass Spectrometry), but if you are lucky and you have a metbolite list, you can jump to FELLA part.<br/>
It is very important to remind that the method we will explain here only gives ideas of real metabolites. It's based on m/z and retetntion time, but with a lot of inference and prediction. You will probably obtain a metabolite list with our pipeline, but keep in mind these are prediction, maybe some annotations are accurate, but these are not 100% sure results. As biologist, we have tried to do annotation job for metabolites, but for a reaaly accurate job, you will need chimist ability. <br/>
## Inference on molecular mass
CAMERA is an R package for metabolites annotation : https://www.bioconductor.org/packages/devel/bioc/vignettes/CAMERA/inst/doc/CAMERA.pdf <br/>
You will find the R code in the code folder: CAMERA_pipe.R file. If everything went well with the code, you chould obtain a csv file : <img src="./figs/csv_fig.png" width="1000" height="600"> <br/>
The last columns contains the graal you need for the following steps: molecular mass of the molecules. It's not surprising if all lines are not filled, because there are multiple similar molecules, and some molecules the programm have not find information.
## Comparing mass to public database metabolites
This is the tricky part, and the most questionable. The theory is that every molecule have it's own molecular mass. If we have acess to database that contains molecule names AND molecular mass, it's easy to compare those mass with the one we infer before with CAMERA. In a perfect world, 2 identical masses should be describe the same molecule. But reality is more complicated and some times, a molecular mass will hit with dozens of molecules. Let's accept the weaknesses of this method and still try to convert masses to names. You will find a python script in the code folder: mass_comparison.py. Please download and run it on youre machine. Please remind to change the path to youre corresponding files (line 3 for the csv you have created with CAMERA, line 13 for the reference file you want to use and line 33 to the folder you want to write results file). For the reference file, we have used urine_metabolites_hmdb.csv, because our mzml files contain urine metabolites (you can choose an ohter file if it make more sense : https://hmdb.ca/downloads. The results should be a txt file with a list of molecules names. The default corresponding mass difference is 0.0001 g/mol, but you can change it if nothing appears (line  24 of the python file). Reminds that the more you raise this number, the more chance you have to get matches from different molecules.<br/>
<img src="./figs/match_list_metabo.png" width="150" height="150"> <br/>
## Convert molecules names to KEGG names
As FELLA (the R packages we will use to infer biological pathways) only recognize KEGG names, we need to convert our list first. Please go there : https://www.metaboanalyst.ca/MetaboAnalyst/upload/ConvertView.xhtml and follow the instructions. Notice that not all compound can be converted to kegg names so don't be surpised if you get less items afetr conversion. Download the csv file created and copy paste the kegg colum in a separate text file. <br/>
<img src="./figs/match_list_kegg.png" width="150" height="150"> <br/>
## Infer pathways with molecules names: FELLA
FELLA need to be installed with the following R command : BiocManager::install("FELLA") <br/>
After running library(FELLA), you can lauch the shiny app by running: FELLA:::launchApp(host = "127.0.0.1", port = 8888)<br/>
The only thing to do is to import a KEGG compound name file : 
<img src="./figs/FELLA1.png" width="600" height="400"> <br/>
Results are Interactive map, with all the compound (enzyme and molecules) and pathways connected to your metabolites. Youre metabolites are green, enzymes are orange, reactions are blue and biological pathways are red. <br/>
<img src="./figs/FELLA2.png" width="600" height="600"> <br/>
You can zoom in and out and rearrange label position. You can aslo select or highlight specific items. For more option, go to the advanced options panel. Here you can modify the number of nodes and the precision. Finally, you can download the map, part of the map or compound table in the export result panel. <br/>
<img src="./figs/FELLA3.png" width="600" height="400"> <br/>
## Compare with SingR results
Now that you have targeted some pathways, you can compare with the results guven by the gene onthology panels of SingR app.
