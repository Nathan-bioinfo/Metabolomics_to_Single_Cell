# Metabolomics_to_Single_Cell
## Introduction
Here is a experimental pipeline, to help biologist understand samples from 2 different view. The goal is to validate or invalidate single cell RNA seq conclusion with metabolomics data. Let's say you have extract RNA from patient sample and you now have raw data. A first step is to analyzeyoure data, and you can go here for that purpose : https://github.com/Nathan-bioinfo/SingR. This is an shiny R application that i have develloped and it will help you to find particular RNA, or biological pathways involved in youre study. The next step could be a metabolomic confirmation, to double check the results and maybe get additional informations.<br/>
## Data
The demonstration is based on .mzml files, raw data from LC-HRMS Thermo Q-Exactive (Liquid Chromatography for Mass Spectrometry), but if you are lucky and you have a metbolite list, you can jump to FELLA part.<br/>
It is very important to remind that the method we will explain here only gives ideas of real metabolites. It's based on m/z and retetntion time, but with a lot of inference and prediction. You will probably obtain a metabolite list with our pipeline, but keep in mind these are prediction, maybe some annotations are accurate, but these are not 100% sure results. As biologist, we have tried to do annotation job for metabolites, but for a reaaly accurate job, you will need chimist ability. <br/>
## Inference on molecular mass
CAMERA is an R package for metabolites annotation : https://www.bioconductor.org/packages/devel/bioc/vignettes/CAMERA/inst/doc/CAMERA.pdf <br/>
You will find the R code in the CAMERA_pipe.R file.


