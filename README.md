# Causal-Inference
Causal inference can be defined as the process by which causes are inferred from the data. 
In this project, data from breast cancer diagnosis is analyzed and causes inferred from this analysis.

# Steps followed
1. Perform a causal inference task using Pearl’s framework;
2. Infer the causal graph from observational data and then validate the graph
3. Merge machine learning with causal inference;

# Data and Features
The data is extracted from Kaggle.. Features in the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

### Attribute Information:
1. ID number
2. Diagnosis (M = malignant, B = benign)
### The remaining (3-32)
1. Ten real-valued features are computed for each cell nucleus:
2. radius (mean of distances from center to points on the perimeter)
3. texture (standard deviation of gray-scale values)
4. Perimeter
5. Area
6. smoothness (local variation in radius lengths)
7. compactness (perimeter^2 / area - 1.0)
8. concavity (severity of concave portions of the contour)
9. concave points (number of concave portions of the contour)
10. Symmetry

The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features

# Data Exploration
Conducted an exploratory data analysis on the data & communicated useful insights. This includes: identification and treating all missing values and outliers in the dataset by using appropriate methods,performing feature extraction and scaling 
This is found on the notebooks folder


# Causal Learning
1. Split data into training and hold-out set 
2. Create a causal graph using all training data and get the insights (this will be considered the ground truth)
3. Create new causal graphs using increasing fractions of the data and compare with the ground truth graph
4. The comparison can be done with a Jaccard Similarity Index, measuring the intersection and union of the graph edges
5. After reaching a stable causal graph, select only variables that point directly to the target variable
6. Train one model using all variables and another using only the variables selected by the graph
7. Measure how much each of the models overfit the hold-out set created in step 
