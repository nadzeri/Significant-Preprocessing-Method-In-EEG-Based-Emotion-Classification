function Datasets = saveDatasets(project_path,method,class)
    if strcmp(method,'fft')
        basePath = strcat(project_path,'\FFT_EEG_',upper(class),'\');
    elseif strcmp(method,'swt')
        basePath = strcat(project_path,'\SWT_EEG_',upper(class),'\');
    elseif strcmp(method,'ica_fft')
        basePath = strcat(project_path,'\ICA_FFT_EEG_',upper(class),'\');
    elseif strcmp(method,'ica_swt')
        basePath = strcat(project_path,'\ICA_SWT_EEG_',upper(class),'\');
    end
    
    all_files = dir(basePath);
    all_files = all_files(3:end);
    all_dir = all_files([all_files(:).isdir]);
    subject = numel(all_dir);

    counterDatasets = 1;

    for h=1:subject
        directory = sprintf('S%02d',h);
        allList = dir( strcat(basePath,directory ));
        allFiles = { allList(3:end).name };
        trial = length(allFiles);

        for i = 1:trial
            rawData = csvread(strcat(basePath,directory,'\T',num2str(i),'.csv'));
            Datasets(counterDatasets,:) = rawData;
            counterDatasets=counterDatasets+1;
        end
    end

    csvwrite(strcat(project_path,'\Metadata\datasets_',method,'_',class,'.csv'),Datasets);
end