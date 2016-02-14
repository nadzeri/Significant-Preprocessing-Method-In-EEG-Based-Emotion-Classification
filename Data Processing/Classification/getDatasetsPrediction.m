function Datasets = getDatasetsPrediction(project_path,method,class)
    Datasets = csvread(strcat(project_path,'\Metadata\datasets_',method,'_',class,'.csv'));
end