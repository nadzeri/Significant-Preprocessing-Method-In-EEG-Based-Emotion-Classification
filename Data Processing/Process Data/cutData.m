function cutData(dataset_path,project_path)
    addpath(genpath('..\Global Code'));
    
    dataset_eeg_path = strcat(dataset_path,'\EEG');

    len1 = 640;
    len2 = 3200;

    allList = dir(dataset_eeg_path);
    allDir = { allList(3:end).name };
    
    if exist(strcat(project_path,'\EEG"'), 'dir')
        system(strcat('rmdir /S /Q "',project_path,'\EEG"'));
    end
    createFolder(length(allDir),strcat(project_path,'\EEG'));
    
    for i=1:length(allDir)
        dataOneDir = allDir{i};
        allFileList = dir(strcat(dataset_eeg_path,'\',dataOneDir));
        allFileName = { allFileList(3:end).name };

        for j = 1:length(allFileName)
            dataOneFile = allFileName{j};
            dataEEG = csvread(strcat(dataset_eeg_path,'\',dataOneDir,'\',dataOneFile),1,0);
            start = mod(length(dataEEG),4)+1;
            dataEEG = dataEEG(start:end,3:16);
            L = length(dataEEG);

            if L>=len2
                used = (L - len2)/2;
            elseif L>=len1
                used = (L - len1)/2;
            else
                continue;
            end

            start = used+1;
            stop = L - used;

            rawData = transpose(dataEEG(start:stop,:));

            fileNewName = dataOneFile(5:end-22);
           
            csvwrite(strcat(project_path,'\EEG\',dataOneDir,'\',fileNewName,'.csv'),rawData);
        end
    end
end