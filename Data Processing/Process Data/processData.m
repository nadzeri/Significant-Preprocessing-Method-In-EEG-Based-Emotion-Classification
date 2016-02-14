function processData(dataset_path)
    dataset_path = 'D:\TUGAS AKHIR\Datasets';
    project_path = strcat(pwd,'\..\..');
    %%%%%%%%%%%%%
    
    cutData(dataset_path,project_path);
    divideFiveSeconds(dataset_path,project_path);
end