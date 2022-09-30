    
## data is du=ictionary contains all input from the user
def preprocess_data(data) :

    radius_mean = data['radius_mean']
    perimeter_mean = data['perimeter_mean']
    area_mean = data['area_mean']
    symmetry_mean = data['symmetry_mean']
    compactness_mean = data['compactness_mean']
    concave_points_mean = data['concave points_mean']
    
    final_data = ['radius_mean','perimeter_mean','area_mean','symmetry_mean',
    'compactness_mean','concave points_mean']
    
    return final_data
