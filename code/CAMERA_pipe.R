BiocManager::install("CAMERA")
library(CAMERA)
file = "path_to_your_file_to_read.mzML"
xs <- xcmsSet(file,method="centWave",ppm=30,peakwidth=c(5,10))
xsa <- xsAnnotate(xs)
an = xsa
# Group based on RT
anF <- groupFWHM(an, perfwhm = 0.6)
# Annotate isotopes
anI <- findIsotopes(anF, mzabs = 0.01)
# Verify grouping
anIC <- groupCorr(anI, cor_eic_th = 0.75)
# Annotate adducts
anFA <- findAdducts(anIC, polarity="positive")
peaklist <- getPeaklist(anFA)
# write information in a csv file on your pc
write.csv(peaklist, file='path_to_youre_file_to_write.csv')
