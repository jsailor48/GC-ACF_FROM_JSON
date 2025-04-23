# GC-ACF_FROM_JSON
Extract Green Kubo Conductivity ACF from Pylat output.json file 
This is a breif Python script to extract the green kubo ionic conductivity autocorelation function from a PyLAT output.json file
The script works by taking an appriximation of the derivative of the green kubo integral values using a combination of central differnece method for interior points, and and forward/backwards difference method for the edges. 
I plan on adding more functionality eventually, so this will not be the final version. 
Hope this helps with your reasearch. 
